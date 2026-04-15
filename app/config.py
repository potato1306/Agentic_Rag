import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

TARGET_PROFIT = 1.10
STOP_LOSS = 0.95
POLL_INTERVAL = 5  # seconds

SYMBOL = "ETH/USDC"