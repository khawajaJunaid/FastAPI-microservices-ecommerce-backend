# common_db/models/sales.py
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from common.db.base import Base
from sqlalchemy import Enum
import datetime
from common.Enums.product_enums import ProductCategory


class Sales(Base):
    """
    A class used to represent sales data.

    Attributes
    ----------
    id : int
        The unique identifier for the sale.
    product_id : int
        The unique identifier for the product being sold.
    category_name : str
        The name of the category the product belongs to.
    units_sold : int
        The number of units sold.
    sold_at : datetime
        The date and time the sale was made.
    total_price : float
        The total price of the sale.
    revenue : float
        The revenue generated from the sale.

    Relationships
    -------------
    products : relationship
        The relationship between the sale and the product being sold.
    category : relationship
        The relationship between the sale and the category the product belongs to.
    """

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    category_name = Column(Enum(ProductCategory), ForeignKey("categories.name"))
    units_sold = Column(Integer, default=0, nullable=False)
    sold_at = Column(DateTime, default=datetime.datetime.utcnow)
    total_price = Column(Float, nullable=False)
    revenue = Column(Float, nullable=True)

    # Define relationships
    products = relationship("Product", back_populates="sales")
    category = relationship("Category", back_populates="sales")
