import sys
import yfinance as yf
import pandas as pd
import numpy as np
import statistics
import shelve
import unittest

import plotly.graph_objs as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, 
                            QPushButton, QTextEdit, QVBoxLayout, QWidget, 
                            QProgressBar, QComboBox, QListWidget, QMessageBox,
                            QTabWidget, QHBoxLayout, QGridLayout, QScrollArea,
                            QFrame, QSizePolicy,QDialog)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon

class DataFetchThread(QThread):
    finished = pyqtSignal(object)
    error = pyqtSignal(str)
    progress = pyqtSignal(int)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker

    def run(self):
        try:
            self.progress.emit(20)
            stock_data = self.get_stock_data(self.ticker)
            self.progress.emit(90)
            self.finished.emit(stock_data)
        except Exception as e:
            self.error.emit(str(e))

    def get_stock_data(self, ticker):
        stock = yf.Ticker(ticker)
        
        try:
            # 基本數據獲取
            info = stock.info
            hist_data = stock.history(period="5y")
            
            if hist_data.empty:
                raise ValueError(f"無法獲取股票 {ticker} 的歷史數據")
            
            # 計算技術指標
            hist_data['MA50'] = hist_data['Close'].rolling(window=50).mean()
            hist_data['MA200'] = hist_data['Close'].rolling(window=200).mean()
            hist_data['RSI'] = self.calculate_rsi(hist_data['Close'])
            
            # 獲取財務數據並進行同比增長計算
            financials = stock.financials
            revenue_growth = self.calculate_growth_rate(financials.loc['Total Revenue'])
            profit_growth = self.calculate_growth_rate(financials.loc['Net Income'])
            
            # 計算更多財務比率
            current_ratio = info.get('currentRatio', "N/A")
            debt_to_equity = info.get('debtToEquity', "N/A")
            return_on_equity = info.get('returnOnEquity', "N/A")
            
            # 獲取行業平均本益比
            industry_pe = self.get_industry_average_pe(info.get('sector'))
            
            # 獲取公司歷史本益比數據
            historical_pe = self.get_historical_pe(ticker)
                
            # 整合所有數據
            return {
                'ticker': ticker,
                'company_name': info.get('longName', "未知公司"),
                'sector': info.get('sector', "未知行業"),
                'current_price': hist_data['Close'].iloc[-1],
                'pe_ratio': info.get('trailingPE', "N/A"),
                'forward_pe': info.get('forwardPE', "N/A"),
                'dividend_yield': info.get('dividendYield', "N/A"),
                'pb_ratio': info.get('priceToBook', "N/A"),
                'market_cap': info.get('marketCap', "N/A"),
                'revenue_growth': revenue_growth,
                'profit_growth': profit_growth,
                'current_ratio': current_ratio,
                'debt_to_equity': debt_to_equity,
                'return_on_equity': return_on_equity,
                'hist_data': hist_data,
                'ma50': hist_data['MA50'].iloc[-1],
                'ma200': hist_data['MA200'].iloc[-1],
                'rsi': hist_data['RSI'].iloc[-1],
                'industry_pe': industry_pe,
                'historical_pe': historical_pe
            }

        except Exception as e:
            raise ValueError(f"獲取股票資料時出現錯誤: {str(e)}")
            
    def get_industry_average_pe(self, sector):
        # 這裡應該實現獲取行業平均本益比的邏輯
        # 為簡化示例，這裡返回一個虛擬值
        return 20  # 實際應用中，這個值應該是動態獲取的

    def calculate_rsi(self, prices, periods=14):
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))

    def calculate_growth_rate(self, series):

        if len(series) >= 2:
            return ((series.iloc[0] - series.iloc[-1]) / series.iloc[-1] * 100)
        return "N/A"
    
    def get_historical_pe(self, ticker):
        stock = yf.Ticker(ticker)
        hist_data = stock.history(period="5y")
        quarterly_financials = stock.quarterly_financials

        historical_pe = []
        
        for date, price in hist_data['Close'].items():
            if pd.isnull(price):  # 檢查價格是否為 NaN
                continue
            
            # 確保日期是 tz-aware
            if date.tzinfo is None:
                date = date.tz_localize('UTC')

            # 找到最近的季度財報，確保也是 tz-aware
            closest_financial_date = min(
                quarterly_financials.columns,
                key=lambda d: abs(d.tz_localize('UTC') - date)  # 本行進行時區轉換
            )
            
            eps = quarterly_financials.loc['Basic EPS', closest_financial_date]
            if eps > 0:  # 避免除以零
                pe = price / (eps * 4)  # 年化 EPS
                historical_pe.append(pe)
        
        return historical_pe

    def calculate_macd(self, prices, short=12, long=26, signal=9):
        short_ema = prices.ewm(span=short, adjust=False).mean()
        long_ema = prices.ewm(span=long, adjust=False).mean()
        macd = short_ema - long_ema
        signal_line = macd.ewm(span=signal, adjust=False).mean()
        return macd, signal_line

    def calculate_bollinger_bands(self, prices, window=20, num_std=2):

        rolling_mean = prices.rolling(window=window).mean()
        rolling_std = prices.rolling(window=window).std()
        upper_band = rolling_mean + (rolling_std * num_std)
        lower_band = rolling_mean - (rolling_std * num_std)
        return upper_band, rolling_mean, lower_band
class StockAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon("C:\progarming\github\Python\python\stock\icon.ico"))

        self.setWindowTitle("美股價值投資分析")
        self.setGeometry(100, 100, 1400, 900)  # 加大窗口尺寸
        
        # 創建中央小部件和總體布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)  # 增加組件之間的間距
        main_layout.setContentsMargins(20, 20, 20, 20)  # 設置邊距
        
        # 頂部標題
        title_label = QLabel("美股價值投資分析")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # 創建輸入區域框架
        input_frame = QFrame()
        input_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        input_layout = QHBoxLayout(input_frame)
        
        # 股票輸入框
        self.stock_input = QLineEdit()
        self.stock_input.setPlaceholderText("輸入股票代號（例如：AAPL）")
        
        # 分析按鈕
        self.analyze_button = QPushButton("開始分析")
        self.analyze_button.clicked.connect(self.start_analysis)
        
        input_layout.addWidget(self.stock_input, 7)  # 分配更多空間給輸入框
        input_layout.addWidget(self.analyze_button, 3)
        main_layout.addWidget(input_frame)
        
        # 進度條
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)  # 隱藏百分比文字
        main_layout.addWidget(self.progress_bar)
        
        # 創建標籤頁
        self.tab_widget = QTabWidget()
        self.tab_widget.setFont(QFont("Arial", 12))
        
        # 創建各個標籤頁
        self.create_overview_tab()
        self.create_technical_tab()
        self.create_financial_tab()
        
        main_layout.addWidget(self.tab_widget)
        
        self.style_ui()

    def create_overview_tab(self):
        overview_tab = QWidget()
        overview_layout = QVBoxLayout(overview_tab)
        
        # 創建可滾動區域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        # 概覽內容區域
        self.overview_text = QTextEdit()
        self.overview_text.setReadOnly(True)
        scroll_layout.addWidget(self.overview_text)
        
        scroll.setWidget(scroll_content)
        overview_layout.addWidget(scroll)
        
        self.tab_widget.addTab(overview_tab, "市場概覽")

    def create_technical_tab(self):
        technical_tab = QWidget()
        technical_layout = QVBoxLayout(technical_tab)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        self.technical_text = QTextEdit()
        self.technical_text.setReadOnly(True)
        scroll_layout.addWidget(self.technical_text)
        
        scroll.setWidget(scroll_content)
        technical_layout.addWidget(scroll)
        
        self.tab_widget.addTab(technical_tab, "技術分析")

    def create_financial_tab(self):

        financial_tab = QWidget()
        financial_layout = QVBoxLayout(financial_tab)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        self.financial_text = QTextEdit()
        self.financial_text.setReadOnly(True)
        scroll_layout.addWidget(self.financial_text)
        
        scroll.setWidget(scroll_content)
        financial_layout.addWidget(scroll)
        
        self.tab_widget.addTab(financial_tab, "財務分析")

    def style_ui(self):
        # 設置整體樣式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f7fa;
            }
            QLineEdit {
                padding: 12px;
                font-size: 16px;
                border: 2px solid #e1e4e8;
                border-radius: 8px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #0366d6;
            }
            QPushButton {
                padding: 12px 20px;
                font-size: 16px;
                font-weight: bold;
                background-color: #0366d6;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #0256b9;
            }
            QPushButton:pressed {
                background-color: #014795;
            }
            QTextEdit {
                font-family: Arial;
                font-size: 16px;
                line-height: 1.6;
                border: 1px solid #e1e4e8;
                border-radius: 8px;
                padding: 15px;
                background-color: white;
            }
            QTabWidget::pane {
                border: 1px solid #e1e4e8;
                border-radius: 8px;
                background-color: white;
            }
            QTabBar::tab {
                font-size: 14px;
                padding: 12px 20px;
                margin-right: 4px;
                background-color: #f1f3f5;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }
            QTabBar::tab:selected {
                background-color: white;
                border-bottom: none;
                font-weight: bold;
            }
            QProgressBar {
                border: none;
                border-radius: 5px;
                background-color: #e1e4e8;
                height: 6px;
            }
            QProgressBar::chunk {
                background-color: #0366d6;
                border-radius: 5px;
            }
        """)

    def start_analysis(self):
        ticker = self.stock_input.text().strip().upper()
        if not ticker:
            QMessageBox.warning(self, "錯誤", "請輸入股票代號")
            return
        
        self.progress_bar.setValue(0)
        self.analyze_button.setEnabled(False)
        
        self.thread = DataFetchThread(ticker)
        self.thread.finished.connect(self.handle_analysis_result)
        self.thread.error.connect(self.handle_analysis_error)
        self.thread.progress.connect(self.progress_bar.setValue)
        self.thread.start()

    def handle_analysis_result(self, data):
        self.display_overview(data)
        self.display_technical_analysis(data)
        self.display_financial_analysis(data)
        
        self.progress_bar.setValue(100)
        self.analyze_button.setEnabled(True)

    def handle_analysis_error(self, error_message):
        QMessageBox.warning(self, "分析錯誤", error_message)
        self.progress_bar.setValue(0)
        self.analyze_button.setEnabled(True)
    
    def display_overview(self, data):
        # 檢查股息收益率的類型並轉換為數字
        dividend_yield = data['dividend_yield']
        if isinstance(dividend_yield, str):
            dividend_yield = 0.0  # 如果是字符串，設置為 0
        else:
            dividend_yield = float(dividend_yield)  # 確保是浮點數

        overview = f"""
        <h2 style='color: #24292e;'>公司概覽</h2>
        <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px; margin-bottom: 20px;'>
            <p><b>公司名稱：</b> {data['company_name']}</p>
            <p><b>股票代號：</b> {data['ticker']}</p>
            <p><b>所屬行業：</b> {data['sector']}</p>
        </div>

        <h2 style='color: #24292e;'>基本指標</h2>
        <div style='display: grid; grid-template-columns: 1fr 1fr; grid-gap: 15px;'>
            <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px;'>
                <p><b>當前股價：</b> ${data['current_price']:.2f}</p>
                <p><b>市值：</b> ${data['market_cap']/1000000000:.2f}B</p>
                <p><b>本益比(TTM)：</b> {data['pe_ratio']}</p>
            </div>
            <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px;'>
                <p><b>預期本益比：</b> {data['forward_pe']}</p>
                <p><b>股息收益率：</b> {dividend_yield:.2%}</p>  <!-- 這裡修改為使用處理過的 dividend_yield -->
                <p><b>股價淨值比：</b> {data['pb_ratio']}</p>
            </div>
        </div>

        <h2 style='color: #24292e; margin-top: 20px;'>投資建議</h2>
        <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px;'>
            {self.generate_investment_advice(data)}
        </div>
        """
        self.overview_text.setHtml(overview)

    def display_technical_analysis(self, data):
        technical = f"""
        <h2 style='color: #24292e;'>技術指標</h2>
        <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px; margin-bottom: 20px;'>
            <p><b>50日均線：</b> ${data['ma50']:.2f}</p>
            <p><b>200日均線：</b> ${data['ma200']:.2f}</p>
            <p><b>RSI(14)：</b> {data['rsi']:.2f}</p>
        </div>

        <h2 style='color: #24292e;'>技術分析</h2>
        <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px;'>
            {self.analyze_technical_indicators(data)}
        </div>
        """
        self.technical_text.setHtml(technical)

    def display_financial_analysis(self, data):
        financial = f"""
        <h2 style='color: #24292e;'>財務指標</h2>
        <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px; margin-bottom: 20px;'>
            <p><b>營收增長率：</b> {data['revenue_growth']:.2f}%</p>
            <p><b>利潤增長率：</b> {data['profit_growth']:.2f}%</p>
            <p><b>流動比率：</b> {data['current_ratio']}</p>
            <p><b>負債權益比：</b> {data['debt_to_equity']}</p>
            <p><b>股東權益報酬率：</b> {data['return_on_equity']:.2%}</p>
        </div>

        <h2 style='color: #24292e;'>財務分析</h2>
        <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px;'>
            {self.analyze_financial_indicators(data)}
        </div>
        """
        self.financial_text.setHtml(financial)

    def generate_investment_advice(self, data):
        advice = []
        
        #需要修改
        if data['pe_ratio'] != "N/A" and isinstance(data['pe_ratio'], (int, float)):
            current_pe = data['pe_ratio']
            industry_pe = data['industry_pe']
            historical_pe = data['historical_pe']
            
            # 與行業平均比較
            if current_pe < industry_pe * 0.7:
                advice.append(f"基於行業平均本益比（{industry_pe:.2f}），該股票可能被低估")
            elif current_pe > industry_pe * 1.3:
                advice.append(f"基於行業平均本益比（{industry_pe:.2f}），該股票可能被高估")
            
            # 與自身歷史數據比較
            if historical_pe:
                avg_historical_pe = statistics.mean(historical_pe)
                if current_pe < avg_historical_pe * 0.7:
                    advice.append(f"基於歷史平均本益比（{avg_historical_pe:.2f}），該股票當前價值可能被低估")
                elif current_pe > avg_historical_pe * 1.3:
                    advice.append(f"基於歷史平均本益比（{avg_historical_pe:.2f}），該股票當前價值可能被高估")
        # 基於技術指標的建議
        if data['current_price'] > data['ma50'] > data['ma200']:
            advice.append("技術形態呈現上升趨勢")
        elif data['current_price'] < data['ma50'] < data['ma200']:
            advice.append("技術形態呈現下降趨勢")
        
        # 基於RSI的建議
        if data['rsi'] > 70:
            advice.append("RSI顯示股票可能處於超買狀態")
        elif data['rsi'] < 30:
            advice.append("RSI顯示股票可能處於超賣狀態")
        
        return "\n".join(advice) if advice else "目前沒有明確的投資建議"

    def analyze_technical_indicators(self, data):
        analysis = []
        
        # 移動平均線分析
        if data['current_price'] > data['ma50']:
            analysis.append("股價位於50日均線之上，短期走勢偏強")
        else:
            analysis.append("股價位於50日均線之下，短期走勢偏弱")
        
        # RSI分析
        if data['rsi'] > 70:
            analysis.append("RSI顯示股票可能超買")
        elif data['rsi'] < 30:
            analysis.append("RSI顯示股票可能超賣")
        else:
            analysis.append("RSI顯示股票處於中性區間")
        
        return "\n".join(analysis)

    def analyze_financial_indicators(self, data):
        analysis = []
        
        # 增長分析
        if data['revenue_growth'] > 10:
            analysis.append("營收增長強勁")
        elif data['revenue_growth'] < 0:
            analysis.append("營收出現下滑，需要關注")
        
        if data['profit_growth'] > 10:
            analysis.append("利潤增長良好")
        elif data['profit_growth'] < 0:
            analysis.append("利潤下滑，建議深入了解原因")
        
        # 財務健康度分析
        if data['current_ratio'] > 2:
            analysis.append("流動比率健康，短期償債能力強")
        elif data['current_ratio'] < 1:
            analysis.append("流動比率偏低，可能存在短期償債風險")
        
        return "\n".join(analysis)

    def analyze_cash_flow(self, ticker):
        stock = yf.Ticker(ticker)
        cash_flow = stock.cashflow
        
        operating_cash_flow = cash_flow.loc['Operating Cash Flow']
        free_cash_flow = cash_flow.loc['Free Cash Flow']
        
        return {
            'operating_cash_flow_growth': self.calculate_growth_rate(operating_cash_flow),
            'free_cash_flow_growth': self.calculate_growth_rate(free_cash_flow),
            'ocf_to_revenue_ratio': operating_cash_flow / stock.financials.loc['Total Revenue']
        }

    def export_to_pdf(self, data):
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
        
        doc = SimpleDocTemplate("stock_analysis_report.pdf", pagesize=letter)
        elements = []
        
        # 添加表格數據
        table_data = [
            ["指標", "數值"],
            ["股票代碼", data['ticker']],
            ["公司名稱", data['company_name']],
            ["當前價格", f"${data['current_price']:.2f}"],
            ["本益比", f"{data['pe_ratio']}"],
            ["股息收益率", f"{data['dividend_yield']:.2%}"]
        ]
        
        t = Table(table_data)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(t)
        
        doc.build(elements)

    def create_stock_chart(self, data):

        fig = make_subplots(rows=2, cols=1)
        
        # 添加股價和均線
        fig.add_trace(go.Candlestick(
            x=data['hist_data'].index,
            open=data['hist_data']['Open'],
            high=data['hist_data']['High'],
            low=data['hist_data']['Low'],
            close=data['hist_data']['Close'],
            name="股價"
        ), row=1, col=1)
        
        # 添加成交量
        fig.add_trace(go.Bar(
            x=data['hist_data'].index,
            y=data['hist_data']['Volume'],
            name="成交量"
        ), row=2, col=1)
        
        return fig
class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("分析設置")
        
        layout = QVBoxLayout(self)
        
        # RSI 設置
        rsi_group = QGroupBox("RSI 設置")
        rsi_layout = QVBoxLayout()
        self.rsi_period = QSpinBox()
        self.rsi_period.setValue(14)
        rsi_layout.addWidget(QLabel("RSI 週期:"))
        rsi_layout.addWidget(self.rsi_period)
        rsi_group.setLayout(rsi_layout)
        
        # 均線設置
        ma_group = QGroupBox("均線設置")
        ma_layout = QVBoxLayout()
        self.ma_short = QSpinBox()
        self.ma_long = QSpinBox()
        self.ma_short.setValue(50)
        self.ma_long.setValue(200)
        ma_layout.addWidget(QLabel("短期均線:"))
        ma_layout.addWidget(self.ma_short)
        ma_layout.addWidget(QLabel("長期均線:"))
        ma_layout.addWidget(self.ma_long)
        ma_group.setLayout(ma_layout)
        
        layout.addWidget(rsi_group)
        layout.addWidget(ma_group)
        
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
class DataCache:
    def __init__(self, cache_file='stock_cache'):
        self.cache_file = cache_file
    
    def get(self, key):
        with shelve.open(self.cache_file) as db:
            return db.get(key)
    
    def set(self, key, value, expiry=3600):  # 預設緩存1小時
        with shelve.open(self.cache_file) as db:
            db[key] = {
                'data': value,
                'expiry': datetime.now().timestamp() + expiry
            }
    
    def is_valid(self, key):
        cached = self.get(key)
        if cached:
            return datetime.now().timestamp() < cached['expiry']
        return False
class ParallelDataFetcher:
    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    
    def fetch_multiple_stocks(self, tickers):
        futures = []
        for ticker in tickers:
            future = self.executor.submit(self.fetch_single_stock, ticker)
            futures.append(future)
        
        results = {}
        for future, ticker in zip(futures, tickers):
            try:
                results[ticker] = future.result()
            except Exception as e:
                results[ticker] = None  # 或者其他方式處理錯誤
                print(f"Error fetching {ticker}: {e}")
        
        return results
    
    def fetch_single_stock(self, ticker):
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y")
        return hist
class TestStockAnalyzer(unittest.TestCase):

    def setUp(self):
        self.app = QApplication([])
        self.analyzer = StockAnalyzerApp()
    
    def test_rsi_calculation(self):
        # 測試數據
        test_prices = pd.Series([10, 12, 11, 13, 15, 14, 16])
        rsi = self.analyzer.calculate_rsi(test_prices)
        self.assertTrue(0 <= rsi.iloc[-1] <= 100)
    
    def test_invalid_ticker(self):
        with self.assertRaises(ValueError):
            self.analyzer.get_stock_data('INVALID_TICKER')
    
    def tearDown(self):
        self.app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = StockAnalyzerApp()
    window.show()
    sys.exit(app.exec_())

# 單元測試部分應獨立進行
if __name__ == "__main__":
    unittest.main()
