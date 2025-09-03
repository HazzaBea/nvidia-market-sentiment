# NVIDIA Market Sentiment Tool

A web-based tool that displays real-time market sentiment analysis for NVIDIA (NVDA) stock, including current price and news sentiment analysis.

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
