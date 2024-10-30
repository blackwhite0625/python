import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, 
                             QLineEdit, QMessageBox, QTextEdit)
from binance.client import Client
from binance.enums import *
import threading
import time

class TradingBot(QWidget):
    def __init__(self):
        super().__init__()
        self.client = None
        self.api_key_input = QLineEdit(self)
        self.api_secret_input = QLineEdit(self)
        self.status_label = QLabel('未連接', self)
        self.balance_label = QLabel('帳戶餘額: ', self)
        self.log_text = QTextEdit(self)
        self.log_text.setReadOnly(True)
        self.start_button = QPushButton('開始交易', self)
        self.stop_button = QPushButton('停止交易', self)
        self.stop_button.setEnabled(False)
        self.running = False

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('API Key:'))
        layout.addWidget(self.api_key_input)
        layout.addWidget(QLabel('API Secret:'))
        layout.addWidget(self.api_secret_input)
        layout.addWidget(self.status_label)
        layout.addWidget(self.balance_label)
        layout.addWidget(self.log_text)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        
        self.setLayout(layout)
        
        self.start_button.clicked.connect(self.start_trading)
        self.stop_button.clicked.connect(self.stop_trading)
        
        self.setWindowTitle('智能交易機器人')
        self.setGeometry(100, 100, 400, 400)

    def start_trading(self):
        api_key = self.api_key_input.text()
        api_secret = self.api_secret_input.text()
        if not api_key or not api_secret:
            QMessageBox.warning(self, '錯誤', '請輸入API Key和Secret')
            return
        
        try:
            self.client = Client(api_key, api_secret)
            self.status_label.setText('連接成功')
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.running = True
            threading.Thread(target=self.trade_loop).start()
        except Exception as e:
            QMessageBox.critical(self, '錯誤', f'無法連接到Binance: {str(e)}')

    def stop_trading(self):
        self.running = False
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.status_label.setText('已停止')

    def trade_loop(self):
        symbol = 'BTCUSDT'
        quantity = 0.001
        while self.running:
            try:
                # 獲取即時價格
                price = float(self.client.get_symbol_ticker(symbol=symbol)["price"])
                self.balance_label.setText(f'即時價格: {price:.2f} USDT')

                # 獲取歷史價格資料進行技術分析
                klines = self.client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE, limit=100)
                closes = np.array([float(kline[4]) for kline in klines])

                # RSI 指標計算
                rsi = self.calculate_rsi(closes)
                # MACD 指標計算
                macd, signal = self.calculate_macd(closes)

                # 策略：RSI < 30 且 MACD 上穿訊號線，則買入；RSI > 70 且 MACD 下穿訊號線，則賣出
                if rsi < 30 and macd[-1] > signal[-1] and macd[-2] < signal[-2]:
                    self.place_order(symbol, SIDE_BUY, quantity)
                elif rsi > 70 and macd[-1] < signal[-1] and macd[-2] > signal[-2]:
                    self.place_order(symbol, SIDE_SELL, quantity)

                time.sleep(60)
            except Exception as e:
                self.log_text.append(f'錯誤: {str(e)}')

    def calculate_rsi(self, prices, period=14):
        delta = np.diff(prices)
        gain = np.where(delta > 0, delta, 0)
        loss = np.where(delta < 0, -delta, 0)
        avg_gain = np.mean(gain[:period])
        avg_loss = np.mean(loss[:period])
        rs = avg_gain / avg_loss if avg_loss != 0 else 0
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calculate_macd(self, prices, slow=26, fast=12, signal_period=9):
        ema_fast = np.mean(prices[-fast:])
        ema_slow = np.mean(prices[-slow:])
        macd = ema_fast - ema_slow
        signal = np.mean(macd[-signal_period:])
        return macd, signal

    def place_order(self, symbol, side, quantity):
        try:
            order = self.client.create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            self.log_text.append(f'{side} 訂單成功: {order["orderId"]}')
        except Exception as e:
            self.log_text.append(f'{side} 訂單失敗: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bot = TradingBot()
    bot.show()
    sys.exit(app.exec_())
