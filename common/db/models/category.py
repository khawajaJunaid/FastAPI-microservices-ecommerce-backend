# common_db/models/categories.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from common.db.base import Base

# from common.enums.product_enums import Category
from common.Enums.product_enums import ProductCategory
from sqlalchemy import Enum


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True)
    name = Column(
        Enum(
            ProductCategory,
            name="category_name",
            create_type=True,
        ),
        index=True,
    )
    description = Column(String(255), nullable=True)

    # Define a relationship with products
    products = relationship("Product", back_populates="category")
