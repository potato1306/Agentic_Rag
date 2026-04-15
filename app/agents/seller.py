from app.utils.logger import log

class SellerAgent:
    def should_sell(self, price, position):
        if price >= position.target_price:
            log("Target reached ✅")
            return True

        if price <= position.stop_loss_price:
            log("Stop loss triggered ❌")
            return True

        return False