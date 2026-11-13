import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=5 * 1000, key="auto_refresh")
st.set_page_config(page_title="CLANCKX LIVE", layout="wide")
st.title("CLANCKX LIVE - 10 COINS 🔥")
st.write("Nigeria, Ukraine, USA, UK - Everywhere")

coins = {
    "SOL": "solana",
    "BTC": "bitcoin",
    "DOGE": "dogecoin",
    "ETH": "ethereum",
    "XRP": "ripple",
    "BNB": "binancecoin",
    "ADA": "cardano",
    "PEPE": "pepe",
    "SHIB": "shiba-inu",
    "TRX": "tron"
}

if st.button("🔄 Refresh Prices"):
    st.rerun()

try:
    ids = ",".join(coins.values())
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&include_24hr_change=true"
    data = requests.get(url, timeout=10).json()

    for symbol, cid in coins.items():
        price = data.get(cid, {}).get("usd", 0)
        change = data.get(cid, {}).get("usd_24h_change", 0)

        if price < 0.01:
            price_text = f"${price:.8f}"
        else:
            price_text = f"${price:.2f}"

      color =  "green" if change >= 0 else "red"
      arrow = "▲" if change >= 0 else "▼"
      msg = f"{symbol}: {price_text} {arrow} {change:.2f}%"
      st.markdown(f"<span style='color:{color}'><b>{msg}</b></span>", unsafe_allow_html=True)

