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


class NoSalesDataFoundException(Exception):
    def __init__(self, message="No sales data found for the conditions specified"):
        self.message = message
        super().__init__(self.message)


class InsufficientInventoryException(Exception):
    """Custom exception for indicating insufficient inventory but still available for ordering."""
    def __init__(self, message="Product has insufficnient inventory, please reduce the amount of your order."):
        self.message = message
        super().__init__(self.message)