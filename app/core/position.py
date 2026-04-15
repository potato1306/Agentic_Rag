from app.config import TARGET_PROFIT, STOP_LOSS

class Position:
    def __init__(self, symbol, entry_price, amount):
        self.symbol = symbol
        self.entry_price = entry_price
        self.amount = amount
        self.target_price = entry_price * TARGET_PROFIT
        self.stop_loss_price = entry_price * STOP_LOSS
        self.is_open = True

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        pos = Position(
            data["symbol"],
            data["entry_price"],
            data["amount"]
        )
        pos.__dict__.update(data)
        return pos