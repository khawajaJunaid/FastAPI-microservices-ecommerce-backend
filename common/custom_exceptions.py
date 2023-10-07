class ProductNotFoundException(Exception):
    def __init__(self, message="Product not found"):
        self.message = message
        super().__init__(self.message)


class ProductInventoryUpdateException(Exception):
    def __init__(self, message="Inventory not updated"):
        self.message = message
        super().__init__(self.message)


class ProductOutofStockException(Exception):
    def __init__(self, message="Product is out of stock, please stay tuned!"):
        self.message = message
        super().__init__(self.message)
