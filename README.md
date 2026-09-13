<div align="center" id="top">

# 📈 STOCKSPHERE

<img src="https://img.shields.io/badge/-%F0%9F%93%88%20MARKET%20INTELLIGENCE%20DASHBOARD%20%F0%9F%93%88-0e1117?style=flat-square&labelColor=0e1117&color=00d4ff" alt="Market Intelligence Dashboard"/>

### A sleek, dark-themed stock market intelligence web app — live quotes, candlestick charts, technical analysis, and news

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="Plotly"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/>
</p>

<p>
  <img src="https://img.shields.io/badge/status-active-2ea44f?style=flat-square" alt="status"/>
  <img src="https://img.shields.io/badge/license-MIT-00d4ff?style=flat-square" alt="license"/>
  <img src="https://img.shields.io/badge/data-free%20sources-00d4ff?style=flat-square" alt="free data sources"/>
  <img src="https://img.shields.io/badge/API%20cost-%240-2ea44f?style=flat-square" alt="zero API cost"/>
  <img src="https://img.shields.io/badge/PRs-welcome-00d4ff?style=flat-square" alt="PRs welcome"/>
</p>

</div>

<br/>

## 📖 Table of Contents

| | | |
|---|---|---|
| [🎯 Overview](#-overview) | [🚀 Features](#-features) | [🛠️ Tech Stack](#️-tech-stack) |
| [📦 Installation](#-installation) | [⚙️ Configuration](#️-configuration) | [📁 Project Structure](#-project-structure) |
| [☁️ Deployment](#️-deployment) | [🗺️ Roadmap](#️-roadmap) | [🤝 Contributing](#-contributing) |
| [❓ FAQ](#-faq) | [📄 License](#-license) | [👤 Credits & Contact](#-credits--contact) |

### 🌐 Live Demo

<div align="center">

[![🌐 Launch StockSphere](https://img.shields.io/badge/🌐_LAUNCH_STOCKSPHERE-00d4ff?style=for-the-badge&labelColor=0e1117)](https://stock-sphere-ipdbyuaaiwt9wabxeqepc9.streamlit.app/)

<sub>Runs live in your browser · No installation required</sub>

</div>

<br/>

---

## 🎯 Overview

**StockSphere** brings together everything you need to track the market in one clean interface — live index tickers, candlestick price action, technical indicators, watchlist comparisons, company financials, and curated news. Built entirely on free data sources, it's a fully functional market dashboard with zero API costs.

<div align="center">

| 📡 | 📊 | 🔍 | 📰 |
|:---:|:---:|:---:|:---:|
| **Live Data**<br/>Real-time index & stock quotes | **Candlestick Charts**<br/>Interactive OHLCV visualization | **Watchlist Compare**<br/>Normalized performance tracking | **News Feed**<br/>Curated financial headlines |

</div>

<br/>

---

## 🚀 Features

<table width="100%">
<tr>
<th align="left" width="50%">📊 Market Data & Charts</th>
<th align="left" width="50%">🔍 Insights & Design</th>
</tr>
<tr>
<td valign="top">

**Market Data**
- **Live Ticker Banner** — scrolling pulse for S&P 500, Dow Jones, NASDAQ, Gold, and FTSE 100
- **Stock Search** — look up any ticker and instantly load detailed data
- **Watchlist** — add/remove multiple stocks (AAPL, TSLA, NVDA...) with persistent session state

**Charts & Analysis**
- **Candlestick Chart** — interactive OHLCV chart with green/red candles
- **Technical Analysis** — RSI indicator with overbought/oversold threshold lines

</td>
<td valign="top">

**Insights**
- **Compare Tab** — normalized relative performance across your watchlist, indexed to 100
- **Financials Tab** — revenue, profit margin, and beta metric cards plus a full company summary
- **News Feed** — latest headlines with source attribution (Barron's, CNBC, Yahoo Finance, and more)

**Design**
- Sleek, professional dark theme throughout
- Responsive, distraction-free layout

</td>
</tr>
</table>

<br/>

---

## 🛠️ Tech Stack

<div align="center">

| Tool | Purpose |
|:---:|---|
| 🐍 **Python** | Core language |
| 🎈 **Streamlit** | Web UI framework |
| 📊 **Plotly** | Interactive charts (candlestick, line, indicators) |
| 🐼 **Pandas** | Data manipulation |
| 📡 **yfinance** | Free stock market data source |

</div>

> Built entirely on free data sources — no paid API required.

<br/>

---

## 📦 Installation

<table>
<tr><td>

**1️⃣ Clone the repository**
```bash
git clone https://github.com/yourusername/stocksphere.git
cd stocksphere
```

**2️⃣ Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

**4️⃣ Run the app**
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` 🎉

</td></tr>
</table>

**Requirements**
```
streamlit
pandas
plotly
yfinance
requests
```

<br/>

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

<br/>

---

## 📁 Project Structure

```bash
stocksphere/
├── app.py                  # 🎯 Main Streamlit application
├── requirements.txt        # 📦 Python dependencies
├── .streamlit/
│   └── config.toml         # 🎨 Dark theme configuration
└── README.md                # 📖 Project overview
```

<div align="center">

| File | Responsibility |
|---|---|
| `app.py` | Application logic — data fetching, charts, tabs, UI |
| `requirements.txt` | Declares all Python package dependencies |
| `.streamlit/config.toml` | Controls theme colors and base styling |

</div>

<br/>

---

## ☁️ Deployment

**Deploy on Streamlit Community Cloud (Free):**

1. 🚀 Push your code to a public GitHub repository
2. 🌐 Go to [streamlit.io/cloud](https://streamlit.io/cloud) and sign in with GitHub
3. ➕ Click **New app** → select your repo and `app.py`
4. ✅ Click **Deploy** — your app will be live in minutes!

<br/>

---

## 🗺️ Roadmap

| Status | Feature |
|:---:|---|
| ⏳ | Portfolio tracking with P&L calculations |
| ⏳ | Additional technical indicators (MACD, Bollinger Bands, moving averages) |
| ⏳ | Price alerts and notifications |
| ⏳ | Export charts and reports |
| ⏳ | Multi-currency support |

<br/>

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

<table>
<tr><td>

1. 🍴 Fork the project
2. 🌱 Create your feature branch — `git checkout -b feature/amazing-feature`
3. 💾 Commit your changes — `git commit -m 'Add some amazing feature'`
4. 🚀 Push to the branch — `git push origin feature/amazing-feature`
5. 🔁 Open a pull request

</td></tr>
</table>

<br/>

---

## ❓ FAQ

**Do I need a paid API key to run this?**
No — StockSphere runs entirely on free data sources (via yfinance), with zero API costs.

**Can I track my own custom list of stocks?**
Yes — use the Watchlist feature to add or remove tickers, with your selections persisted in session state.

**Does it support portfolio tracking?**
Not yet — portfolio tracking with P&L calculations is on the [roadmap](#️-roadmap).

**Can I deploy this myself for free?**
Yes — see the [Deployment](#️-deployment) section for deploying on Streamlit Community Cloud at no cost.

<br/>

---

## 📄 License

This project is open source. Feel free to use, modify, and share it with proper attribution.

<br/>

---

## 👤 Credits & Contact

<div align="center">

### 📈 Built with precision — StockSphere

*Markets move fast. Now you can keep up.*

Built with Python, Streamlit, Plotly, and Pandas · Powered by free market data via yfinance

For bugs, feature requests, or questions, open an issue on the GitHub repository.

<br/>

**[⬆ Back to top](#top)**

</div>
