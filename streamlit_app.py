import streamlit as st
import requests
from datetime import datetime
import time

# Config and setup
st.set_page_config(
    page_title="NVIDIA Market Sentiment Tool",
    layout="wide"
)

# API Configuration
FINNHUB_API_KEY = 'd2s0nrpr01qv11lgk070d2s0nrpr01qv11lgk07g'

def get_stock_price():
    """Fetch current stock price from Finnhub"""
    try:
        response = requests.get(f'https://finnhub.io/api/v1/quote?symbol=NVDA&token={FINNHUB_API_KEY}')
        data = response.json()
        if 'c' in data:
            return f"${data['c']:.2f}"
        else:
            return "Unable to fetch price"
    except Exception as e:
        return f"Error: {str(e)}"

def get_news_and_sentiment():
    """Fetch news and calculate sentiment"""
    try:
        today = datetime.now().strftime('%Y-%m-%d')
        response = requests.get(
            f'https://finnhub.io/api/v1/company-news?symbol=NVDA&from={today}&to={today}&token={FINNHUB_API_KEY}'
        )
        news = response.json()
        
        if isinstance(news, list) and len(news) > 0:
            return news[:5]  # Return only the 5 most recent news items
        return []
    except Exception as e:
        st.error(f"Failed to fetch news: {str(e)}")
        return []

def get_sentiment_color(score):
    """Return appropriate color based on sentiment score"""
    if score > 0.3:
        return "green"
    elif score < -0.3:
        return "red"
    return "yellow"

def get_sentiment_label(score):
    """Return sentiment label based on score"""
    if score > 0.3:
        return "Bullish"
    elif score < -0.3:
        return "Bearish"
    return "Neutral"

# Main app layout
st.title("NVIDIA (NVDA) Market Sentiment")

# Create two columns for stock price and sentiment
col1, col2 = st.columns(2)

# Stock Price Section
with col1:
    st.subheader("Current Price")
    price = get_stock_price()
    st.markdown(f"<h1 style='text-align: center; color: green;'>{price}</h1>", unsafe_allow_html=True)

# Overall Sentiment Section
with col2:
    st.subheader("Market Sentiment")
    # Simulate sentiment score (replace with actual sentiment analysis)
    import random
    overall_sentiment = random.uniform(-1, 1)
    sentiment_label = get_sentiment_label(overall_sentiment)
    sentiment_color = get_sentiment_color(overall_sentiment)
    
    st.markdown(f"<h1 style='text-align: center; color: {sentiment_color};'>{sentiment_label}</h1>", 
                unsafe_allow_html=True)
    
    # Create a progress bar to visualize sentiment
    normalized_sentiment = (overall_sentiment + 1) / 2  # Convert from [-1,1] to [0,1]
    st.progress(normalized_sentiment)

# News Headlines Section
st.subheader("Recent News Headlines")
news_items = get_news_and_sentiment()

for article in news_items:
    with st.expander(article['headline']):
        st.write(f"Date: {datetime.fromtimestamp(article['datetime']).strftime('%Y-%m-%d')}")
        if 'summary' in article:
            st.write(article['summary'])
        
        # Simulate sentiment for each article (replace with actual sentiment analysis)
        article_sentiment = random.uniform(-1, 1)
        sentiment_label = get_sentiment_label(article_sentiment)
        sentiment_color = get_sentiment_color(article_sentiment)
        st.markdown(f"<p style='color: {sentiment_color};'>Sentiment: {sentiment_label}</p>", 
                   unsafe_allow_html=True)

# Last updated timestamp
st.sidebar.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Auto-refresh button
if st.sidebar.button("Refresh Data"):
    st.experimental_rerun()

# Add auto-refresh using streamlit's rerun
time.sleep(300)  # 5 minutes
st.experimental_rerun()
