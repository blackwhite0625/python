import sys
import yfinance as yf
import pandas as pd
import numpy as np
import statistics
import shelve
import unittest
import plotly.express as px
import plotly.graph_objs as go
import logging
import feedparser
from datetime import datetime, timedelta
from PyQt5.QtCore import QTimer
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, 
                            QPushButton, QTextEdit, QVBoxLayout, QWidget, 
                            QProgressBar, QComboBox, QListWidget, QMessageBox,
                            QTabWidget, QHBoxLayout, QGridLayout, QScrollArea,
                            QFrame, QSizePolicy,QDialog)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


#數據抓取
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
        industry_pe = self.get_industry_average_pe(ticker)
        if industry_pe is None:
            industry_pe = "N/A"
        # 計算PEG比率
        try:
            peg_ratio = info.get('pegRatio', 'N/A')
        except:
            peg_ratio = 'N/A'

        # 計算自由現金流收益率
        try:
            market_cap = info.get('marketCap', 0)
            free_cash_flow = financials.loc['Free Cash Flow'].iloc[0]
            fcf_yield = (free_cash_flow / market_cap) * 100 if market_cap != 0 else 'N/A'
        except:
            fcf_yield = 'N/A'
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
            hist_data['MACD'], hist_data['Signal_Line'] = self.calculate_macd(hist_data['Close'])
            hist_data['Upper_BB'], hist_data['Middle_BB'], hist_data['Lower_BB'] = self.calculate_bollinger_bands(hist_data['Close'])
            
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
                'historical_pe': historical_pe,
                'financials': financials,
                'peg_ratio': peg_ratio,
                'fcf_yield': fcf_yield,
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

    def run_stock_filter(self):
        criteria = {
            'pe_ratio': 15,  # 例如：PE比率小於15
            'dividend_yield': 0.02  # 例如：股息收益率大於2%
        }
        filtered_stocks = self.filter_stocks(criteria)
        self.display_filtered_stocks(filtered_stocks)

    def display_filtered_stocks(self, stocks):
        # 實現這個方法來在UI中顯示篩選後的股票列表
        pass

#主應用程序類，處理 UI 和主要邏輯
class StockAnalyzerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.stock_filter = StockFilter()
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_data)
        self.update_timer.start(300000)  # 每5分鐘更新一次
        self.init_portfolio_manager()
        
    def update_data(self):
        if hasattr(self, 'current_ticker') and self.current_ticker:
            self.start_analysis()
               
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

        self.technical_view = QWebEngineView()  # 使用 QWebEngineView
        scroll_layout.addWidget(self.technical_view)

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

        self.financial_view = QWebEngineView()  # Use QWebEngineView instead of QTextEdit
        scroll_layout.addWidget(self.financial_view)

        scroll.setWidget(scroll_content)
        financial_layout.addWidget(scroll)

        self.tab_widget.addTab(financial_tab, "財務分析")

    def create_financial_charts(self, data):
        # 處理財務數據
        financials = data['financials'].T
        financials.index = financials.index.strftime('%Y-%m-%d')  # 格式化日期
        financials = financials.sort_index()  # 確保日期順序正確

        # 創建子圖
        fig = make_subplots(rows=2, cols=2, subplot_titles=(
            "營收和淨利潤趨勢", "利潤率趨勢", "資產負債結構", "現金流趨勢"
        ))

        # 檢查並添加圖表
        missing_data = []

        # 1. 營收和淨利潤趨勢
        if 'Total Revenue' in financials.columns and 'Net Income' in financials.columns:
            fig.add_trace(go.Bar(x=financials.index, y=financials['Total Revenue'], name="營收"), row=1, col=1)
            fig.add_trace(go.Scatter(x=financials.index, y=financials['Net Income'], name="淨利潤", mode='lines+markers'), row=1, col=1)
        else:
            missing_data.append("營收和淨利潤")

        # 2. 利潤率趨勢
        if 'Gross Profit' in financials.columns and 'Total Revenue' in financials.columns:
            gross_margin = (financials['Gross Profit'] / financials['Total Revenue']) * 100
            net_margin = (financials['Net Income'] / financials['Total Revenue']) * 100
            fig.add_trace(go.Scatter(x=financials.index, y=gross_margin, name="毛利率", mode='lines+markers'), row=1, col=2)
            fig.add_trace(go.Scatter(x=financials.index, y=net_margin, name="淨利率", mode='lines+markers'), row=1, col=2)
        else:
            missing_data.append("利潤率")

        # 3. 資產負債結構
        if 'Total Assets' in financials.columns and 'Total Liabilities Net Minority Interest' in financials.columns:
            fig.add_trace(go.Bar(x=financials.index, y=financials['Total Assets'], name="總資產"), row=2, col=1)
            fig.add_trace(go.Bar(x=financials.index, y=financials['Total Liabilities Net Minority Interest'], name="總負債"), row=2, col=1)
        else:
            missing_data.append("資產負債結構")

        # 4. 現金流趨勢
        if 'Operating Cash Flow' in financials.columns and 'Free Cash Flow' in financials.columns:
            fig.add_trace(go.Scatter(x=financials.index, y=financials['Operating Cash Flow'], name="營運現金流", mode='lines+markers'), row=2, col=2)
            fig.add_trace(go.Scatter(x=financials.index, y=financials['Free Cash Flow'], name="自由現金流", mode='lines+markers'), row=2, col=2)
        else:
            missing_data.append("現金流")

        # 更新佈局
        fig.update_layout(
            height=800, width=1200,
            title_text="財務分析圖表",
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            font=dict(family="Arial", size=10),
            margin=dict(l=50, r=50, t=80, b=50)
        )

        # 更新x軸和y軸
        fig.update_xaxes(tickangle=45, tickmode='auto', nticks=20)
        fig.update_yaxes(title_text="金額 (美元)", row=1, col=1)
        fig.update_yaxes(title_text="百分比 (%)", row=1, col=2)
        fig.update_yaxes(title_text="金額 (美元)", row=2, col=1)
        fig.update_yaxes(title_text="金額 (美元)", row=2, col=2)

        return fig, missing_data

    def create_overview_charts(self, data):
        # 創建子圖
        fig = make_subplots(rows=2, cols=2, subplot_titles=(
            "股價趨勢", "成交量", "本益比趨勢", "股息收益率趨勢"
        ))
        
        # 1. 股價趨勢
        fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['Close'], name="股價"), row=1, col=1)
        
        # 2. 成交量
        fig.add_trace(go.Bar(x=data['hist_data'].index, y=data['hist_data']['Volume'], name="成交量"), row=1, col=2)
        
        # 3. 本益比趨勢（如果有數據的話）
        if 'pe_ratio' in data['hist_data'].columns:
            fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['pe_ratio'], name="本益比"), row=2, col=1)
        
        # 4. 股息收益率趨勢（如果有數據的話）
        if 'dividend_yield' in data['hist_data'].columns:
            fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['dividend_yield'], name="股息收益率"), row=2, col=2)
        
        # 更新佈局
        fig.update_layout(height=800, width=1200, title_text="市場概覽圖表")
        
        return fig
    
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
        logging.basicConfig(filename='stock_analyzer.log', level=logging.ERROR)
        try:
            # 原有的數據獲取代碼
            self.thread = DataFetchThread(ticker)
            self.thread.finished.connect(self.handle_analysis_result)
            self.thread.error.connect(self.handle_analysis_error)
            self.thread.start()
        except Exception as e:
            logging.exception(f"分析過程中發生錯誤: {e}")
            QMessageBox.critical(self, "錯誤", f"分析過程中發生錯誤: {e}")

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
            
        # fcf_yield = data['fcf_yield']
        # fcf_yield_str = f"{fcf_yield:.2f}%" if isinstance(fcf_yield, (float, int)) else fcf_yield
        
        fcf_yield = data.get('fcf_yield', 'N/A')
        if isinstance(fcf_yield, (float, int)):
            fcf_yield_str = f"{fcf_yield:.2f}%"
        else:
            fcf_yield_str = fcf_yield
            
        overview_fig = self.create_overview_charts(data)
        overview_chart_html = overview_fig.to_html(full_html=False, include_plotlyjs='cdn')
        
        overview = f"""
        <h2 style='color: #24292e;'>市場概覽圖表</h2>
        
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
        
        <h2 style='color: #24292e;'>進階指標</h2>
        <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px;'>
            <p><b>PEG比率：</b> {data['peg_ratio']}</p>
            <p><b>自由現金流收益率：</b> {fcf_yield_str}</p>
        </div>
        {overview_chart_html}
        """
        self.overview_text.setHtml(overview)

    def display_technical_analysis(self, data):
        # 創建股票圖表
        fig = self.create_stock_chart(data)  # 調用 create_stock_chart 函數

        # 將圖表轉換為 HTML 格式
        html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        {html}

        # 文字敘述方式
        # 將圖表添加到 technical_text 中
        # technical = f"""
        # <h2 style='color: #24292e;'>技術指標</h2>
        # <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px; margin-bottom: 20px;'>
        #     <p><b>50日均線：</b> ${data['ma50']:.2f}</p>
        #     <p><b>200日均線：</b> ${data['ma200']:.2f}</p>
        #     <p><b>RSI(14)：</b> {data['rsi']:.2f}</p>
        # </div>

        # <h2 style='color: #24292e;'>技術分析</h2>
        # <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px;'>
        #     {self.analyze_technical_indicators(data)}
        # </div>
        #"""
        self.technical_view.setHtml(html)
        
    def display_financial_analysis(self, data):
        financial_fig, missing_data = self.create_financial_charts(data)
    
        # 將圖表轉換為 HTML 格式
        chart_html = financial_fig.to_html(full_html=False, include_plotlyjs='cdn')
        
        missing_data_html = ""
        if missing_data:
            missing_data_html = f"""
            <div style='background-color: #fff3cd; color: #856404; padding: 15px; border-radius: 6px; margin-bottom: 20px;'>
                <p><strong>注意：</strong> 以下財務數據無法顯示：{', '.join(missing_data)}</p>
            </div>
            """
        
        financial_html = f"""
        <h2 style='color: #24292e;'>財務指標</h2>
        <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px; margin-bottom: 20px;'>
            <p><b>營收增長率：</b> {data.get('revenue_growth', 'N/A'):.2f}%</p>
            <p><b>利潤增長率：</b> {data.get('profit_growth', 'N/A'):.2f}%</p>
            <p><b>流動比率：</b> {data.get('current_ratio', 'N/A')}</p>
            <p><b>負債權益比：</b> {data.get('debt_to_equity', 'N/A')}</p>
            <p><b>股東權益報酬率：</b> {data.get('return_on_equity', 'N/A'):.2%}</p>
        </div>

        {missing_data_html}

        <h2 style='color: #24292e;'>財務分析</h2>
        <div style='background-color: #f6f8fa; padding: 15px; border-radius: 6px;'>
            {self.analyze_financial_indicators(data)}
        </div>

        {chart_html}
        """
        self.financial_view.setHtml(financial_html)

    def generate_investment_advice(self, data):
        advice = []

        if data['pe_ratio'] == "N/A":  # 首先判斷是否為 "N/A"
            return "目前沒有明確的投資建議"

        if isinstance(data['pe_ratio'], (int, float)):
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
        fig = make_subplots(rows=4, cols=1, shared_xaxes=True, vertical_spacing=0.02, 
                            row_heights=[0.5, 0.2, 0.15, 0.15])
        
        # 添加K線圖和均線
        fig.add_trace(go.Candlestick(
            x=data['hist_data'].index,
            open=data['hist_data']['Open'],
            high=data['hist_data']['High'],
            low=data['hist_data']['Low'],
            close=data['hist_data']['Close'],
            name="股價"
        ), row=1, col=1)
        
        fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['MA50'], name="MA50"), row=1, col=1)
        fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['MA200'], name="MA200"), row=1, col=1)
        
        # 添加成交量
        fig.add_trace(go.Bar(x=data['hist_data'].index, y=data['hist_data']['Volume'], name="成交量"), row=2, col=1)
        
        # 添加MACD
        fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['MACD'], name="MACD"), row=3, col=1)
        fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['Signal_Line'], name="Signal Line"), row=3, col=1)
        
        # 添加布林通道
        fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['Upper_BB'], name="Upper BB", line=dict(dash='dash')), row=4, col=1)
        fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['Middle_BB'], name="Middle BB"), row=4, col=1)
        fig.add_trace(go.Scatter(x=data['hist_data'].index, y=data['hist_data']['Lower_BB'], name="Lower BB", line=dict(dash='dash')), row=4, col=1)
        
        fig.update_layout(height=800, title_text="股票技術分析圖表")
        fig.update_xaxes(rangeslider_visible=False)
        
        return fig
    
    def filter_stocks(self, criteria):
        filtered_stocks = []
        for ticker in self.all_stocks:  # 假設您有一個包含所有股票的列表
            stock_data = self.get_stock_data(ticker)
            if self.meets_criteria(stock_data, criteria):
                filtered_stocks.append(ticker)
        return filtered_stocks

    def meets_criteria(self, stock_data, criteria):
        for key, value in criteria.items():
            if key not in stock_data or stock_data[key] < value:
                return False
        return True

    def export_to_excel(self, data):
        df = pd.DataFrame(data)
        df.to_excel('stock_analysis.xlsx', index=False)

    def export_to_pdf(self, data):
        doc = SimpleDocTemplate("stock_analysis.pdf", pagesize=letter)
        elements = []
        # 將數據轉換為表格格式
        t = Table(data)
        t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke)]))
        elements.append(t)
        doc.build(elements)


        fig = go.Figure()
        fig.add_trace(go.Scatter(name='Operating Cash Flow', x=data['Date'], y=data['Operating Cash Flow'], mode='lines', line=dict(color='blue')))
        fig.add_trace(go.Scatter(name='Investing Cash Flow', x=data['Date'], y=data['Investing Cash Flow'], mode='lines', line=dict(color='red')))
        fig.add_trace(go.Scatter(name='Financing Cash Flow', x=data['Date'], y=data['Financing Cash Flow'], mode='lines', line=dict(color='green')))

        fig.update_layout(title='Cash Flow Trend Over Time',
                        xaxis_title='Date', yaxis_title='Cash Flow')
        fig.show()

    def init_portfolio_manager(self):
        self.portfolio_manager = PortfolioManager()
        self.news_integrator = NewsIntegrator()

        # 創建投資組合管理標籤頁
        portfolio_tab = QWidget()
        portfolio_layout = QVBoxLayout(portfolio_tab)

        # 添加創建投資組合的控件
        create_portfolio_layout = QHBoxLayout()
        self.portfolio_name_input = QLineEdit()
        create_portfolio_button = QPushButton("創建投資組合")
        create_portfolio_button.clicked.connect(self.create_portfolio)
        create_portfolio_layout.addWidget(self.portfolio_name_input)
        create_portfolio_layout.addWidget(create_portfolio_button)
        portfolio_layout.addLayout(create_portfolio_layout)

        # 添加投資組合列表
        self.portfolio_list = QListWidget()
        self.portfolio_list.itemClicked.connect(self.show_portfolio_details)
        portfolio_layout.addWidget(self.portfolio_list)

        # 添加投資組合詳情區域
        self.portfolio_details = QTextEdit()
        self.portfolio_details.setReadOnly(True)
        portfolio_layout.addWidget(self.portfolio_details)

        self.tab_widget.addTab(portfolio_tab, "投資組合")

        # 創建新聞標籤頁
        news_tab = QWidget()
        news_layout = QVBoxLayout(news_tab)

        # 添加新聞源選擇下拉框
        self.news_source_combo = QComboBox()
        self.news_source_combo.addItems(self.news_integrator.news_feeds.keys())
        news_layout.addWidget(self.news_source_combo)

        # 添加獲取新聞按鈕
        get_news_button = QPushButton("獲取新聞")
        get_news_button.clicked.connect(self.fetch_news)
        news_layout.addWidget(get_news_button)

        # 添加新聞顯示區域
        self.news_display = QTextEdit()
        self.news_display.setReadOnly(True)
        news_layout.addWidget(self.news_display)

        self.tab_widget.addTab(news_tab, "新聞")

    def create_portfolio(self):
        name = self.portfolio_name_input.text()
        try:
            self.portfolio_manager.create_portfolio(name)
            self.portfolio_list.addItem(name)
            self.portfolio_name_input.clear()
        except ValueError as e:
            QMessageBox.warning(self, "錯誤", str(e))

    def show_portfolio_details(self, item):
        portfolio = self.portfolio_manager.get_portfolio(item.text())
        if portfolio:
            details = f"投資組合: {portfolio.name}\n"
            details += f"總價值: ${portfolio.get_value():.2f}\n\n"
            details += "持股:\n"
            for ticker, quantity in portfolio.holdings.items():
                stock = yf.Ticker(ticker)
                current_price = stock.info['regularMarketPrice']
                value = current_price * quantity
                details += f"{ticker}: {quantity} 股, 價值: ${value:.2f}\n"
            self.portfolio_details.setText(details)

    def fetch_news(self):
        source = self.news_source_combo.currentText()
        try:
            news = self.news_integrator.get_news(source)
            news_text = ""
            for entry in news:
                news_text += f"標題: {entry.title}\n"
                news_text += f"發布時間: {entry.published}\n"
                news_text += f"鏈接: {entry.link}\n\n"
            self.news_display.setText(news_text)
        except ValueError as e:
            QMessageBox.warning(self, "錯誤", str(e))

    def generate_investment_advice(self, data):
        advice = []

        # 基本面分析
        if data['pe_ratio'] != "N/A" and isinstance(data['pe_ratio'], (int, float)):
            if data['pe_ratio'] < data['industry_pe'] * 0.7:
                advice.append("基於行業平均本益比,該股票可能被低估")
            elif data['pe_ratio'] > data['industry_pe'] * 1.3:
                advice.append("基於行業平均本益比,該股票可能被高估")
        
        if data['pb_ratio'] != "N/A" and isinstance(data['pb_ratio'], (int, float)):
            if data['pb_ratio'] < 1:
                advice.append("股價淨值比低於1,可能表示股票被低估")
            elif data['pb_ratio'] > 3:
                advice.append("股價淨值比較高,需謹慎評估")

        # 股息分析
        if data['dividend_yield'] != "N/A" and isinstance(data['dividend_yield'], (int, float)):
            if data['dividend_yield'] > 0.04:
                advice.append("股息收益率較高,可能適合收入型投資者")
            elif data['dividend_yield'] < 0.01:
                advice.append("股息收益率較低,可能不適合尋求穩定收入的投資者")

        # 成長性分析
        if data['revenue_growth'] > 20:
            advice.append("營收增長強勁,公司可能處於高速成長期")
        elif data['revenue_growth'] < 0:
            advice.append("營收出現下滑,需要關注公司基本面變化")

        # 財務健康度分析
        if data['debt_to_equity'] != "N/A" and isinstance(data['debt_to_equity'], (int, float)):
            if data['debt_to_equity'] > 2:
                advice.append("負債權益比較高,公司財務風險可能較大")
            elif data['debt_to_equity'] < 0.5:
                advice.append("負債權益比較低,公司財務狀況相對穩健")

        # 技術面分析
        if data['current_price'] > data['ma50'] > data['ma200']:
            advice.append("股價位於50日和200日均線之上,短期技術形態偏強")
        elif data['current_price'] < data['ma50'] < data['ma200']:
            advice.append("股價位於50日和200日均線之下,短期技術形態偏弱")

        if data['rsi'] > 70:
            advice.append("RSI處於超買區間,短期可能面臨回調風險")
        elif data['rsi'] < 30:
            advice.append("RSI處於超賣區間,可能存在反彈機會")

        # 綜合建議
        if len(advice) == 0:
            return "目前沒有明確的投資建議,建議進行更深入的研究"
        elif len(advice) <= 2:
            return "初步分析建議:\n" + "\n".join(advice) + "\n建議結合更多因素進行綜合判斷"
        else:
            return "投資建議:\n" + "\n".join(advice) + "\n請注意,這些建議僅供參考,實際投資決策需要考慮更多因素"

    def get_industry_average_pe(self, ticker):
        try:
            stock = yf.Ticker(ticker)
            industry = stock.info['industry']
            sector = stock.info['sector']
            
            # 獲取同行業的主要公司
            peers = stock.info.get('recommendationKey', [])
            if not peers:
                # 如果無法獲取推薦的同行,可以使用行業ETF作為替代
                industry_etfs = {
                    "Technology": "XLK",
                    "Healthcare": "XLV",
                    "Financials": "XLF",
                    "Consumer Discretionary": "XLY",
                    "Industrials": "XLI",
                    # 添加更多行業ETF...
                }
                etf_ticker = industry_etfs.get(sector, "SPY")  # 如果找不到對應的ETF,使用S&P 500 ETF
                peers = yf.Ticker(etf_ticker).info.get('holdings', [])[:10]  # 獲取ETF前10大持股
            
            pe_ratios = []
            for peer in peers:
                peer_stock = yf.Ticker(peer)
                pe = peer_stock.info.get('trailingPE')
                if pe and isinstance(pe, (int, float)) and pe > 0:
                    pe_ratios.append(pe)
            
            if pe_ratios:
                avg_pe = sum(pe_ratios) / len(pe_ratios)
                return avg_pe
            else:
                return None
        except Exception as e:
            print(f"獲取行業平均本益比時出錯: {e}")
            return None

#設定對話框
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

#數據緩存
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
    
#並行數據獲取
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

#單元測試
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

#股票篩選功能
class StockFilter:
    def __init__(self):
        self.criteria = {}

    def add_criterion(self, name, operator, value):
        self.criteria[name] = (operator, value)

    def filter_stocks(self, stocks):
        return [stock for stock in stocks if self.meets_criteria(stock)]

    def meets_criteria(self, stock):
        for name, (operator, value) in self.criteria.items():
            if operator == '>' and stock[name] <= value:
                   return False
            elif operator == '<' and stock[name] >= value:
                   return False
               # 添加更多操作符...
        return True

#用戶自定義指標
class CustomIndicator:
    def __init__(self, name, formula):
        self.name = name
        self.formula = formula

    def calculate(self, data):
        # 使用 eval 或更安全的方法來執行公式
        return eval(self.formula, {"data": data})

class IndicatorManager:
    def __init__(self):
        self.indicators = {}

    def add_indicator(self, name, formula):
        self.indicators[name] = CustomIndicator(name, formula)

    def calculate_indicator(self, name, data):
        if name in self.indicators:
            return self.indicators[name].calculate(data)
        else:
            raise ValueError(f"指標 {name} 不存在")

class Portfolio:
    def __init__(self, name):
        self.name = name
        self.holdings = {}  # 股票代碼: 持股數量
        self.transactions = []

    def add_stock(self, ticker, quantity):
        if ticker in self.holdings:
            self.holdings[ticker] += quantity
        else:
            self.holdings[ticker] = quantity
        self.transactions.append(("買入", ticker, quantity, datetime.now()))

    def remove_stock(self, ticker, quantity):
        if ticker in self.holdings:
            if self.holdings[ticker] >= quantity:
                self.holdings[ticker] -= quantity
                if self.holdings[ticker] == 0:
                    del self.holdings[ticker]
                self.transactions.append(("賣出", ticker, quantity, datetime.now()))
            else:
                raise ValueError("賣出數量超過持有數量")
        else:
            raise ValueError("投資組合中沒有此股票")

    def get_value(self):
        total_value = 0
        for ticker, quantity in self.holdings.items():
            stock = yf.Ticker(ticker)
            current_price = stock.info['regularMarketPrice']
            total_value += current_price * quantity
        return total_value

class PortfolioManager:
    def __init__(self):
        self.portfolios = {}

    def create_portfolio(self, name):
        if name not in self.portfolios:
            self.portfolios[name] = Portfolio(name)
        else:
            raise ValueError("投資組合名稱已存在")

    def delete_portfolio(self, name):
        if name in self.portfolios:
            del self.portfolios[name]
        else:
            raise ValueError("投資組合不存在")

    def get_portfolio(self, name):
        return self.portfolios.get(name)

class NewsIntegrator:
    def __init__(self):
        self.news_feeds = {
            "財經新聞": "http://finance.yahoo.com/rss/topstories",
            "市場動態": "http://feeds.marketwatch.com/marketwatch/topstories/"
        }

    def get_news(self, feed_name, max_entries=10):
        if feed_name in self.news_feeds:
            feed = feedparser.parse(self.news_feeds[feed_name])
            return feed.entries[:max_entries]
        else:
            raise ValueError("無效的新聞源名稱")

    def get_stock_news(self, ticker, max_entries=10):
        stock_feed = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={ticker}&region=US&lang=en-US"
        feed = feedparser.parse(stock_feed)
        return feed.entries[:max_entries]
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = StockAnalyzerApp()
    window.show()
    sys.exit(app.exec_())

# 單元測試部分應獨立進行
if __name__ == "__main__":
    unittest.main()

