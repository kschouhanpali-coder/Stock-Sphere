# Stock-Sphere

**StockSphere** is a Streamlit-based stock market dashboard featuring a live ticker banner, candlestick charts, RSI analysis, multi-stock watchlist comparison, financials, and a news feed — built entirely without any paid API, using free data sources with a sleek dark-themed professional UI.

# 📈 StockSphere — Market Intelligence Dashboard

> A sleek, dark-themed stock market intelligence web application built with Streamlit — no paid API required.

---

## 🌐 Live Demo

**👉 [Launch StockSphere](https://stock-sphere-ipdbyuaaiwt9wabxeqepc9.streamlit.app/)**

> Runs live in your browser — no installation required.

---

## 🚀 Features

- **Live Ticker Banner** — Scrolling market pulse showing S&P 500, Dow Jones, NASDAQ, Gold, and FTSE 100
- **Stock Search** — Search any ticker symbol and instantly load detailed data
- **Watchlist** — Add/remove multiple stocks (e.g. AAPL, TSLA, NVDA) with persistent session state
- **Candlestick Chart** — Interactive OHLCV candlestick chart with green/red candles
- **Technical Analysis** — RSI indicator overlaid with price chart, overbought/oversold threshold lines
- **Compare Tab** — Normalized relative performance chart for all watchlist stocks indexed to 100
- **Financials Tab** — Revenue, Profit Margin, Beta metric cards + full Company Summary
- **News Feed** — Latest headlines with source attribution (Barron's, CNBC, Yahoo Finance, etc.)

---

## 🖥️ Screenshots

| Overview | Analysis | Compare |
|----------|----------|---------|
| Candlestick chart + quote cards | RSI indicator chart | Relative performance % |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Web UI framework |
| Plotly | Interactive charts (candlestick, line, indicators) |
| Pandas | Data manipulation |
| yfinance / free data source | Stock data (no paid API) |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/stocksphere.git
cd stocksphere
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 📁 Project Structure

```
stocksphere/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml         # Dark theme configuration
└── README.md
```

---

## ⚙️ Configuration

The dark theme is pre-configured in `.streamlit/config.toml`:

```toml
[theme]
base = "dark"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#161b22"
primaryColor = "#00d4ff"
```

---

## 📋 Requirements

```
streamlit
pandas
plotly
yfinance
requests
```

---

## 🌐 Deployment

### Deploy on Streamlit Community Cloud (Free)

1. Push your code to a public GitHub repository
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in with GitHub
3. Click **New app** → select your repo and `app.py`
4. Click **Deploy** — your app will be live in minutes!

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

[MIT](LICENSE)

---

## 👨‍💻 Author

Built with ❤️ using AI-assisted development tools.
