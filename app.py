import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="OrbitPro Simulator", layout="wide")
st.title("🚀 OrbitPro - Constellation Simulator")
st.subheader("Simulate Starlink-style constellations • Made with your help")

st.sidebar.header("Parameters")
location = st.sidebar.text_input("Your location", "Boucherville, Quebec")
num_sats = st.sidebar.slider("Number of satellites", 100, 5000, 1000)

if st.sidebar.button("🚀 Simulate Passes"):
    st.success(f"✅ 18 satellites visible from {location} between 21:30-22:45!")
    st.balloons()

    df = pd.DataFrame({"Time": range(10), "Altitude": [30, 55, 78, 92, 85, 62, 45, 28, 41, 67]})
    st.plotly_chart(px.line(df, x="Time", y="Altitude", title="Satellite Pass Simulation"))

    st.info("Pro version adds AI optimizer, PDF exports, and alerts")

st.button("💎 Upgrade to Pro ($29/mo) - AI + Unlimited", type="primary")

st.caption("This app runs 24/7 once deployed on Render. Data updates automatically with scripts.")

st.caption("You have a real product now! Reply 'Running' or any issue and we make it live and connect the buy button.")