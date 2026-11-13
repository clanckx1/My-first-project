import streamlit as st
import requests
import time

st.set_page_config(page_title="CLANCKX LIVE")
st.title("CLANCKX LIVE - 10 COINS")
st.write("Nigeria, Ukraine, USA, UK - Everywhere")

coins = [
    ("SOL", "SOLUSDT"),
    ("BTC", "BTCUSDT"),
    ("DOGE", "DOGEUSDT"),
    ("ETH", "ETHUSDT"),
    ("XRP", "XRPUSDT"),
    ("BNB", "BNBUSDT"),
    ("ADA", "ADAUSDT"),
    ("PEPE", "PEPEUSDT"),
    ("SHIB", "SHIBUSDT"),
    ("TRX", "TRXUSDT"),
]

def get_price(symbol):
    try:
        r = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}", timeout=5)
        return float(r.json()["price"])
    except:
        return None

old = {name: 0 for name, sym in coins}
placeholder = st.empty()

while True:
    with placeholder.container():
        for name, symbol in coins:
            new_price = get_price(symbol)
            if new_price is None:
                st.write(f"{name}: Loading...")
                continue
            old_price = old[name]
            if new_price > old_price:
                st.write(f"🟢 {name}: {new_price} UP | Old: {old_price}")
            elif new_price < old_price:
                st.write(f"🔴 {name}: {new_price} DOWN | Old: {old_price}")
            else:
                st.write(f"⚪ {name}: {new_price} SAME | Old: {old_price}")
            old[name] = new_price
        st.write("Checking every 5 seconds...")
    time.sleep(5)
    st.rerun()
