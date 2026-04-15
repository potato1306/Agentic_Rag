import ccxt
from app.config import API_KEY, API_SECRET

class ExchangeClient:
    def __init__(self, testnet=True):
        if testnet:
            self.exchange = ccxt.binance({
                "apiKey": API_KEY,
                "secret": API_SECRET,
                "enableRateLimit": True,
            })
            self.exchange.set_sandbox_mode(True)
        else:
            self.exchange = ccxt.binance({
                "apiKey": API_KEY,
                "secret": API_SECRET,
                "enableRateLimit": True,
            })