# common_db/models/products.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from common.db.base import Base
from sqlalchemy import Enum
import datetime
from common.Enums.product_enums import ProductCategory


class Inventory(Base):
    """
    A class used to represent the inventory of a product.

    Attributes
    ----------
    id : int
        The unique identifier of the inventory transaction.
    product_id : int
        The unique identifier of the product associated with the inventory transaction.
    category_name : str
        The name of the category associated with the inventory transaction.
    inventory_quantity : int
        The quantity of the product in the inventory.
    inserted_at : datetime
        The date and time when the inventory transaction was inserted.
    low_stock_alert_threshold : int
        The minimum quantity of the product that triggers a low stock alert.

    Relationships
    -------------
    product : Product
        The product associated with the inventory transaction.
    category : Category
        The category associated with the inventory transaction.
    """

    __tablename__ = "inventory_transactions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    category_name = Column(Enum(ProductCategory), ForeignKey("categories.name"))
    inventory_quantity = Column(Integer, default=0, nullable=True)
    inserted_at = Column(DateTime, default=datetime.datetime.utcnow)
    low_stock_alert_threshold = Column(Integer, default=10)

    # Define relationships
    product = relationship("Product", back_populates="inventory_transactions")
    category = relationship("Category", back_populates="inventory_transactions")
