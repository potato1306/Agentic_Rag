import time
from app.exchange.client import ExchangeClient
from app.agents.seller import SellerAgent
from app.config import POLL_INTERVAL
from app.utils.logger import log

class Monitor:
    def __init__(self):
        self.client = ExchangeClient()
        self.seller = SellerAgent()

    def run(self, position):
        log("Starting monitor...")

        while position.is_open:
            price = self.client.get_price(position.symbol)

            log(f"Price: {price} | Target: {position.target_price}")

            if self.seller.should_sell(price, position):
                self.client.market_sell(position.symbol, position.amount)
                position.is_open = False
                log("Position closed 💰")
                break

            time.sleep(POLL_INTERVAL)