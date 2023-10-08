# common_db/models/categories.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from common.db.base import Base

# from common.enums.product_enums import Category
from common.Enums.product_enums import ProductCategory
from sqlalchemy import Enum


class Category(Base):
    """
    A class representing a category of products in the ecommerce system.

    Attributes:
    -----------
    category_id : int
        The unique identifier for the category.
    name : ProductCategory
        The name of the category.
    description : str
        A brief description of the category.
    products : List[Product]
        A list of products in the category.
    inventory_transactions : List[Inventory]
        A list of inventory transactions for the category.
    sales : List[Sales]
        A list of sales for the category.

    relationships:
    --------------
    products : relationship
        The relationship between the category and the products in the category.
    inventory_transactions : relationship
        The relationship between the category and the inventory transactions for the category.
    sales : relationship
        The relationship between the category and the sales for the category.
    """

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
    inventory_transactions = relationship("Inventory", back_populates="category")
    sales = relationship("Sales", back_populates="category")
