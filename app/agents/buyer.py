from app.exchange.client import ExchangeClient
from app.core.position import Position
from app.storage.db import save_position
from app.utils.logger import log

class BuyerAgent:
    def __init__(self):
        self.client = ExchangeClient()

    def execute(self, symbol, usdc_amount):
        log(f"Buying {symbol} for {usdc_amount} USDC")

        price, amount, _ = self.client.market_buy(symbol, usdc_amount)

        position = Position(symbol, price, amount)

        save_position(position)

        log(f"Bought at {price}, amount {amount}")
        return position