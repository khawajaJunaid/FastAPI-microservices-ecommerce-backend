# common_db/models/sales.py
from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from common.db.base import Base
from sqlalchemy import Enum
import datetime
from common.Enums.product_enums import ProductCategory


class Sales(Base):
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
