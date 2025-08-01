import logging

# Setup logging
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)


class StockChecker:
    def __init__(self, stock_file="data/stock.txt"):
        
        self.stock_file = stock_file
        self.stock_data = self.check_stock()  # Load stock data on initialization

    def check_stock(self):
        """Load stock data while ensuring valid formatting."""
        stock_data = {}
        with open(self.stock_file, "r") as file:
            lines = [
                line.strip() for line in file.readlines() if line.strip()
            ]  # Remove empty lines
            for line in lines:
                product, quantity = line.split(",")
                product, quantity = product.strip().lower(), quantity.strip()
                stock_data[product] = int(quantity)
        return stock_data

    def refresh_stock(self):
        """Reload stock data from file to reflect real-time updates."""
        logging.info("Refreshing stock data...")
        self.stock_data = self.check_stock()

    def validate_product(self, product_name):
        """Check if the given product exists in stock data."""
        if product_name not in self.stock_data:
            logging.warning(
                f"🚨 Invalid product name entered: {product_name}. Choose one product from the list above."
            )
            return False  # Product does not exist
        return True  # Product exists
