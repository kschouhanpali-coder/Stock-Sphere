<div align="center">

# 📈 StockSphere

**Market Intelligence Dashboard**

A sleek, dark-themed stock market intelligence web app — live quotes, candlestick charts, technical analysis, and news, built entirely with **free data sources** (no paid API required).

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Launch_App-00d4ff?style=for-the-badge)](https://stock-sphere-ipdbyuaaiwt9wabxeqepc9.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [Screenshots](#️-screenshots)
- [Tech Stack](#️-tech-stack)
- [Installation](#-installation)
- [Configuration](#️-configuration)
- [Project Structure](#-project-structure)
- [Deployment](#️-deployment)
- [Contributing](#-contributing)

---

## 🎯 Overview

**StockSphere** brings together everything you need to track the market in one clean interface — live index tickers, candlestick price action, technical indicators, watchlist comparisons, company financials, and curated news. Built entirely on free data sources, it's a fully functional market dashboard with zero API costs.

---

## 🌐 Live Demo

<div align="center">

### 👉 [**Launch StockSphere**](https://stock-sphere-ipdbyuaaiwt9wabxeqepc9.streamlit.app/)

*Runs live in your browser — no installation required.*

</div>

---

## 🚀 Features

<table>
<tr>
<td valign="top" width="50%">

### 📊 Market Data
- **Live Ticker Banner** — scrolling pulse for S&P 500, Dow Jones, NASDAQ, Gold, and FTSE 100
- **Stock Search** — look up any ticker and instantly load detailed data
- **Watchlist** — add/remove multiple stocks (AAPL, TSLA, NVDA...) with persistent session state

### 📈 Charts & Analysis
- **Candlestick Chart** — interactive OHLCV chart with green/red candles
- **Technical Analysis** — RSI indicator with overbought/oversold threshold lines

</td>
<td valign="top" width="50%">

### 🔍 Insights
- **Compare Tab** — normalized relative performance across your watchlist, indexed to 100
- **Financials Tab** — revenue, profit margin, and beta metric cards plus a full company summary
- **News Feed** — latest headlines with source attribution (Barron's, CNBC, Yahoo Finance, and more)

### 🎨 Design
- Sleek, professional dark theme throughout

</td>
</tr>
</table>

---

## 🖥️ Screenshots

| Overview | Analysis | Compare |
|:---:|:---:|:---:|
| Candlestick chart + quote cards | RSI indicator chart | Relative performance % |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core language |
| **Streamlit** | Web UI framework |
| **Plotly** | Interactive charts (candlestick, line, indicators) |
| **Pandas** | Data manipulation |
| **yfinance** | Free stock market data source |

---

## 📦 Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/stocksphere.git
cd stocksphere
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` 🎉

### Requirements
```
streamlit
pandas
plotly
yfinance
requests
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

## 📁 Project Structure

```bash
stocksphere/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .streamlit/
│   └── config.toml         # Dark theme configuration
└── README.md
```

---

## ☁️ Deployment

**Deploy on Streamlit Community Cloud (Free):**

1. Push your code to a public GitHub repository
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in with GitHub
3. Click **New app** → select your repo and `app.py`
4. Click **Deploy** — your app will be live in minutes! 🚀

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

---

<div align="center">

**Built with ❤️ — StockSphere**

</div>
