from app.agents.buyer import BuyerAgent
from app.core.monitor import Monitor
from app.config import SYMBOL

def run():
    buyer = BuyerAgent()
    monitor = Monitor()

    amount = float(input("Enter USDC amount to trade: "))

    position = buyer.execute(SYMBOL, amount)

    monitor.run(position)