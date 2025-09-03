# NVIDIA Market Sentiment Backtesting Tool

A web-based tool for analyzing NVIDIA (NVDA) stock price movements and market sentiment correlation. This single-page application uses historical price data and news sentiment to help understand market trends.

## Features

- Interactive date range selection (DD/MM/YYYY format)
- Real-time data fetching from Finnhub API
- Dual-axis chart showing stock price and sentiment correlation
- 30-day rolling sentiment calculation
- Performance metrics including price change and sentiment correlation
- Responsive design for both desktop and mobile
- Modern UI with Tailwind CSS

## Technologies Used

- HTML5
- Tailwind CSS
- Chart.js
- Finnhub API for market data
- JavaScript (ES6+)

## Setup

1. Clone this repository
2. Replace the Finnhub API key in the code with your own (get one at https://finnhub.io/)
3. Open index.html in a modern web browser

## Usage

1. Select your desired date range using the DD/MM/YYYY format
2. Click "Run Backtest" to fetch and analyze the data
3. View the results in the interactive chart
4. Check the metrics below the chart for price change, average sentiment, and correlation

## Dependencies

All dependencies are loaded via CDN:
- Tailwind CSS
- Chart.js
- Chart.js Date Adapter

## Features

- Real-time stock price updates
- Recent news headlines with sentiment analysis
- Visual sentiment indicator
- Auto-refresh every 5 minutes

## Setup

1. Clone this repository
```bash
git clone https://github.com/HazzaBea/nvidia-market-sentiment.git
cd nvidia-market-sentiment
```

2. Create a `config.js` file in the root directory:
```javascript
const config = {
    FINNHUB_API_KEY: 'YOUR_FINNHUB_API_KEY'
};
```

3. Sign up for a free API key at [Finnhub](https://finnhub.io/) and add it to your `config.js` file.

4. Open `index.html` in your web browser.

## Author

- **HazzaBea** - [GitHub Profile](https://github.com/HazzaBea)
- Contact: hwmbeckwith@gmail.com

## License

This project is open source and available under the MIT License.
