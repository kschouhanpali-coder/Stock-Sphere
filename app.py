import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import yfinance as yf
from datetime import datetime, timedelta

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="StockSphere | Market Intelligence",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- BACKEND FUNCTIONS (Self-Contained) ---
@st.cache_data(ttl=300)
def get_market_indices():
    indices = {"^GSPC": "S&P 500", "^DJI": "Dow Jones", "^IXIC": "NASDAQ", "BTC-USD": "Bitcoin", "GC=F": "Gold", "^FTSE": "FTSE 100"}
    data = {}
    for symbol, name in indices.items():
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="2d")
            if not hist.empty:
                price = hist['Close'].iloc[-1]
                change_pct = ((price - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100
                data[name] = {"price": price, "change": change_pct}
        except: continue
    return data

@st.cache_data(ttl=300)
def get_stock_quote(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        if data.empty: return {"error": "No data received from Yahoo Finance (Cloud IP Blocked/Rate Limited)."}
        info = ticker.info
        latest = data.iloc[-1]
        prev_close = info.get('previousClose', latest['Open'])
        return {"Global Quote": {"05. price": latest['Close'], "09. change": latest['Close'] - prev_close, "10. change percent": f"{((latest['Close'] - prev_close)/prev_close)*100:.2f}%", "06. volume": latest['Volume'], "03. high": latest['High'], "04. low": latest['Low']}}
    except Exception as e: return {"error": str(e)}

@st.cache_data(ttl=86400)
def get_official_logo(url):
    """Scrape the official website for its high-res logo or favicon."""
    if not url or url == '#': return None
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    try:
        if not url.startswith('http'): url = 'https://' + url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Priority 1: High-res Apple touch icons or OG images
        for rel in ['apple-touch-icon', 'apple-touch-icon-precomposed', 'icon', 'shortcut icon']:
            link = soup.find('link', rel=rel)
            if link and link.get('href'):
                return urljoin(url, link.get('href'))
                
        # Priority 2: Open Graph Image
        og = soup.find('meta', property='og:image')
        if og and og.get('content'):
            return urljoin(url, og.get('content'))
            
        # Priority 3: Fallback to domain root favicon
        return urljoin(url, '/favicon.ico')
    except:
        return None

@st.cache_data(ttl=3600)
def get_company_overview(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        website = info.get('website', '#')
        logo = get_official_logo(website)
        
        return {
            "MarketCapitalization": f"${info.get('marketCap', 0):,}",
            "Description": info.get('longBusinessSummary', "No description available."),
            "Name": info.get('longName', symbol),
            "Sector": info.get('sector', 'N/A'),
            "Industry": info.get('industry', 'N/A'),
            "Employees": info.get('fullTimeEmployees', 'N/A'),
            "PE_Trailing": info.get('trailingPE', 'N/A'),
            "DividendYield": f"{info.get('dividendYield', 0)*100:.2f}%" if info.get('dividendYield') else "0.00%",
            "Beta": info.get('beta', 'N/A'),
            "Revenue": f"${info.get('totalRevenue', 0):,}",
            "ProfitMargin": f"{info.get('profitMargins', 0)*100:.2f}%" if info.get('profitMargins') else "N/A",
            "Website": website,
            "Logo_URL": logo
        }
    except: return {}

@st.cache_data(ttl=300)
def get_daily_series(symbol, period="1mo"):
    try:
        df = yf.Ticker(symbol).history(period=period)
        if df.empty: return {"error": "No data"}
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
        df['RSI'] = 100 - (100 / (1 + (gain/loss)))
        df['MACD'] = df['Close'].ewm(span=12).mean() - df['Close'].ewm(span=26).mean()
        df['Signal'] = df['MACD'].ewm(span=9).mean()
        return {"Time Series (Daily)": df}
    except Exception as e: return {"error": str(e)}

@st.cache_data(ttl=300)
def get_comparison_data(symbols, period="1mo"):
    combined = pd.DataFrame()
    for s in symbols:
        try:
            h = yf.Ticker(s).history(period=period)['Close']
            if not h.empty: combined[s] = h
        except: continue
    return (combined / combined.iloc[0]) * 100 if not combined.empty else None

@st.cache_data(ttl=86400)
def get_wikipedia_summary(name):
    import requests
    try:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{name.replace(' ', '_')}"
        res = requests.get(url, timeout=5)
        if res.status_code == 200: return res.json().get('extract')
    except: pass
    return None

@st.cache_data(ttl=600)
def get_news_sentiment(symbol):
    import requests
    import xml.etree.ElementTree as ET
    try:
        url = f"https://news.google.com/rss/search?q={symbol}+stock&hl=en-US&gl=US&ceid=US:en"
        res = requests.get(url, timeout=5)
        if res.status_code != 200: return {"feed": []}
        
        root = ET.fromstring(res.content)
        articles = []
        for item in root.findall('.//item')[:10]:
            articles.append({
                "title": item.find('title').text,
                "link": item.find('link').text,
                "publisher": item.find('source').text if item.find('source') is not None else "Google News",
                "date": item.find('pubDate').text
            })
        return {"feed": articles}
    except:
        return {"feed": []}

# --- UI POLISH & CUSTOM CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&family=Plus+Jakarta+Sans:wght@400;700&display=swap');
    :root { --bg-color: #05070a; --card-bg: rgba(22, 27, 34, 0.7); --accent: #58a6ff; --accent-glow: rgba(88, 166, 255, 0.3); --text-primary: #f0f6fc; --text-secondary: #8b949e; --border: rgba(48, 54, 61, 0.6); }
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; background-color: var(--bg-color); color: var(--text-primary); }
    .stApp { background-image: radial-gradient(circle at 50% -20%, #161b22 0%, #05070a 100%); }
    div[data-testid="stMetric"] { background: var(--card-bg) !important; border: 1px solid var(--border) !important; border-radius: 20px !important; padding: 25px !important; }
    .profile-card { background: linear-gradient(135deg, rgba(22, 27, 34, 0.8), rgba(13, 17, 23, 0.9)); border: 1px solid var(--border); border-radius: 24px; padding: 30px; margin-bottom: 30px; display: flex; align-items: center; gap: 30px; backdrop-filter: blur(20px); }
    .stock-logo { width: 80px; height: 80px; border-radius: 15px; background: #fff; display: flex; align-items: center; justify-content:center; padding: 8px; }
    .badge { background: rgba(88, 166, 255, 0.1); color: var(--accent); padding: 4px 12px; border-radius: 8px; font-size: 0.8rem; font-weight: 600; border: 1px solid rgba(88, 166, 255, 0.2); }
    .section-title { color: var(--accent); font-family: 'Outfit', sans-serif; text-transform: uppercase; letter-spacing: 3px; font-size: 0.9rem; font-weight: 700; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if 'watchlist' not in st.session_state: st.session_state.watchlist = ["AAPL", "TSLA", "NVDA"]

# --- TICKER TAPE ---
indices_data = get_market_indices()
tape_content = " • ".join([f"{name}: <span style='color:{'#00ff9d' if d['change']>=0 else '#ff3e3e'}'>{d['price']:,.2f} ({d['change']:+.2f}%)</span>" for name, d in indices_data.items()])
st.markdown(f'<div style="background:rgba(13,17,23,0.9); border-bottom:1px solid var(--border); padding:10px 0; overflow:hidden; white-space:nowrap; position:fixed; top:0; left:0; right:0; z-index:1000; backdrop-filter:blur(10px);"><div style="display:inline-block; animation:marquee 30s linear infinite;"><span style="font-family:Outfit; font-size:0.85rem; font-weight:600; color:#8b949e; margin-right:50px;">MARKET PULSE: &nbsp;&nbsp; {tape_content} &nbsp;&nbsp; | &nbsp;&nbsp; {tape_content}</span></div></div><style>@keyframes marquee {{0%{{transform:translateX(0);}} 100%{{transform:translateX(-50%);}}}} .stApp {{margin-top:50px;}}</style>', unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("""
        <div style='display:flex; align-items:center; margin-bottom:10px;'>
            <div style='background:linear-gradient(135deg, #58a6ff, #00ff9d); width:35px; height:35px; border-radius:50%; display:flex; align-items:center; justify-content:center; margin-right:12px; box-shadow: 0 0 15px rgba(88,166,255,0.4);'>
                <span style='color:white; font-size:1rem; font-weight:bold;'>🌐</span>
            </div>
            <h2 style='color:#f0f6fc; margin:0; font-family:Outfit; font-size:1.5rem;'>StockSphere</h2>
        </div>
    """, unsafe_allow_html=True)
    ticker_input = st.text_input("🔍 Search Symbol", value="NVDA").upper()
    if st.button("🚀 Add to Watchlist", use_container_width=True):
        if ticker_input not in st.session_state.watchlist: st.session_state.watchlist.append(ticker_input); st.rerun()
    st.markdown("### Watchlist")
    for symbol in st.session_state.watchlist:
        cols = st.columns([4, 1])
        if cols[0].button(f"📊 {symbol}", key=f"btn_{symbol}", use_container_width=True): ticker_input = symbol; st.rerun()
        if cols[1].button("✕", key=f"del_{symbol}"): st.session_state.watchlist.remove(symbol); st.rerun()
    time_period = st.selectbox("Timeline", ["1 Month", "3 Months", "6 Months", "1 Year", "Max"], index=0)
    period_map = {"1 Month": "1mo", "3 Months": "3mo", "6 Months": "6mo", "1 Year": "1y", "Max": "max"}

# --- MAIN CONTENT ---
ticker = ticker_input
with st.spinner(f"Loading {ticker}..."):
    quote = get_stock_quote(ticker)
    ov = get_company_overview(ticker)
    series = get_daily_series(ticker, period_map[time_period])

    if "error" in quote: 
        st.error(f"Asset not found or blocked by provider. Details: {quote['error']}")
    else:
        q = quote["Global Quote"]
        # Robust Domain Extraction
        raw_website = ov.get("Website", "")
        clean_domain = raw_website.lower().replace("http://", "").replace("https://", "").replace("www.", "").strip("/").split("/")[0]
        initial = ov.get("Name", ticker)[0].upper() if ov.get("Name") else ticker[0].upper()
        
        brand_colors = {
            "NVDA": "linear-gradient(135deg, #76b900, #406300)", # Nvidia Green
            "TSLA": "linear-gradient(135deg, #e23d40, #8a1315)", # Tesla Red
            "AAPL": "linear-gradient(135deg, #555555, #111111)", # Apple Gray/Black
            "MSFT": "linear-gradient(135deg, #00a4ef, #005a84)", # Microsoft Blue
            "META": "linear-gradient(135deg, #0668E1, #033675)", # Meta Blue
            "AMZN": "linear-gradient(135deg, #ff9900, #8a5300)", # Amazon Orange
            "BTC-USD": "linear-gradient(135deg, #f7931a, #8c510b)", # Bitcoin Orange
        }
        # Fallback gradient using a hash of the ticker
        default_color = brand_colors.get(ticker, f"linear-gradient(135deg, hsl({sum(ord(c) for c in ticker)*50 % 360}, 70%, 50%), hsl({sum(ord(c) for c in ticker)*50 % 360}, 80%, 20%))")

        # Custom Logo Overrides for specific companies to use full-text/official variants
        custom_logos = {
            "NVDA": "https://upload.wikimedia.org/wikipedia/commons/2/21/Nvidia_logo.svg",
            "TSLA": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Tesla_logo.png",
            "AAPL": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"
        }
        
        final_logo_url = custom_logos.get(ticker, ov.get("Logo_URL") or f'https://logo.clearbit.com/{clean_domain}?size=120')
        
        # Override background for NVDA to match the white background of the uploaded logo
        if ticker in custom_logos:
            default_color = "#ffffff"

        st.markdown(f'''
            <div class="profile-card">
                <div class="stock-logo" style="position:relative; overflow:hidden; background:{default_color}; padding:0; border-radius:15px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                    <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:white; font-size:2rem; font-weight:800; font-family:Outfit; position:absolute; top:0; left:0; z-index:1;">
                        {initial}
                    </div>
                    <img src="{final_logo_url}" 
                         onerror="this.onerror=null; this.src='https://www.google.com/s2/favicons?domain={clean_domain}&sz=128';" 
                         style="width: 100%; height: 100%; object-fit: contain; position:absolute; top:0; left:0; z-index:2; padding: 10px;">
                </div>
                <div class="stock-info">
                    <div style="display:flex; align-items:center; gap:15px;">
                        <h1>{ov.get("Name", ticker)}</h1>
                        <span class="badge">{ticker}</span>
                    </div>
                    <p style="color:#8b949e; margin:0;">
                        {ov.get("Sector", "N/A")} • {ov.get("Industry", "N/A")} • <a href="{raw_website}" target="_blank" style="color:#58a6ff; text-decoration:none;">Website ↗</a>
                    </p>
                </div>
            </div>
        ''', unsafe_allow_html=True)
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 OVERVIEW", "📉 ANALYSIS", "⚖️ COMPARE", "💰 FINANCIALS", "📰 NEWS"])

        with tab1:
            st.markdown('<p class="section-title">QUOTES</p>', unsafe_allow_html=True)
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Price", f"${q['05. price']:,.2f}", f"{q['09. change']:+.2f}")
            c2.metric("High", f"${q['03. high']:,.2f}")
            c3.metric("Low", f"${q['04. low']:,.2f}")
            c4.metric("Volume", f"{int(q['06. volume']):,}")
            if "Time Series (Daily)" in series:
                df = series["Time Series (Daily)"]
                fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], increasing_line_color='#00ff9d', decreasing_line_color='#ff3e3e')])
                fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False, height=500, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.markdown('<p class="section-title">INDICATORS</p>', unsafe_allow_html=True)
            if "Time Series (Daily)" in series:
                df = series["Time Series (Daily)"]
                inds = st.multiselect("Active Indicators", ["RSI", "MACD"], default=["RSI"])
                from plotly.subplots import make_subplots
                rows = 1 + len(inds)
                fig_a = make_subplots(rows=rows, cols=1, shared_xaxes=True, vertical_spacing=0.05)
                fig_a.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Price", line=dict(color='white')), row=1, col=1)
                curr_row = 2
                if "RSI" in inds:
                    fig_a.add_trace(go.Scatter(x=df.index, y=df['RSI'], name="RSI", line=dict(color='#00ff9d')), row=curr_row, col=1)
                    fig_a.add_hline(y=70, line_color="red", row=curr_row, col=1); fig_a.add_hline(y=30, line_color="green", row=curr_row, col=1)
                    curr_row += 1
                if "MACD" in inds:
                    fig_a.add_trace(go.Scatter(x=df.index, y=df['MACD'], name="MACD", line=dict(color='#58a6ff')), row=curr_row, col=1)
                    fig_a.add_trace(go.Scatter(x=df.index, y=df['Signal'], name="Signal", line=dict(color='#ff7f0e')), row=curr_row, col=1)
                fig_a.update_layout(template="plotly_dark", height=400 + (200*len(inds)), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_a, use_container_width=True)

        with tab3:
            st.markdown('<p class="section-title">PERFORMANCE</p>', unsafe_allow_html=True)
            comp = get_comparison_data(list(set([ticker] + st.session_state.watchlist)), period_map[time_period])
            if comp is not None:
                fig_c = px.line(comp, title="Relative Performance %")
                fig_c.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig_c, use_container_width=True)

        with tab4:
            st.markdown('<p class="section-title">FINANCIALS</p>', unsafe_allow_html=True)
            f1, f2, f3 = st.columns(3)
            f1.metric("Revenue", ov.get('Revenue', 'N/A'))
            f2.metric("Profit Margin", ov.get('ProfitMargin', 'N/A'))
            f3.metric("Beta", ov.get('Beta', 'N/A'))
            st.markdown("---")
            wiki = get_wikipedia_summary(ov.get('Name', ticker))
            if wiki:
                st.markdown("### Wikipedia Insight")
                st.write(wiki)
                st.markdown("---")
            st.markdown("### Company Summary")
            st.write(ov.get('Description', 'No info.'))

        with tab5:
            st.markdown('<p class="section-title">LATEST NEWS</p>', unsafe_allow_html=True)
            news_feed = get_news_sentiment(ticker).get('feed', [])
            if news_feed:
                for n in news_feed[:10]:
                    title = n.get("title") or n.get("headline") or "News Update"
                    publisher = n.get("publisher") or n.get("source") or "Financial Source"
                    link = n.get("link") or n.get("url") or "#"
                    st.markdown(f'<div style="background:var(--card-bg); padding:20px; border-radius:15px; border:1px solid var(--border); margin-bottom:12px; border-left: 4px solid var(--accent);"><a href="{link}" target="_blank" style="color:#58a6ff; text-decoration:none; font-weight:bold; font-size:1.1rem; display:block; margin-bottom:5px;">{title}</a><small style="color:#8b949e;">{publisher}</small></div>', unsafe_allow_html=True)
            else:
                st.info("No news found for this asset.")