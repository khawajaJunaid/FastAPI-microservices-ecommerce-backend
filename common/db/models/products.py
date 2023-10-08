# common_db/models/products.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from common.db.base import Base
from sqlalchemy import Enum
import datetime
from common.Enums.product_enums import ProductStatus
from common.Enums.product_enums import ProductCategory


class Product(Base):
    """
    A class representing a product in the ecommerce system.

    Attributes:
    -----------
    id : int
        The unique identifier of the product.
    category_name : str
        The name of the category that the product belongs to.
    name : str
        The name of the product.
    description : str
        The description of the product.
    price : float
        The price of the product.
    image : str
        The URL of the image of the product.
    created_at : datetime
        The date and time when the product was created.
    updated_at : datetime
        The date and time when the product was last updated.
    status : ProductStatus
        The status of the product (ACTIVE, INACTIVE).
    current_inventory : int
        The current inventory of the product.
    category : Category
        The category that the product belongs to.
    inventory_transactions : List[Inventory]
        The list of inventory transactions associated with the product.
    sales : List[Sales]
        The list of sales associated with the product.
    """

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(Enum(ProductCategory), ForeignKey("categories.name"))
    name = Column(String(60), index=True)
    description = Column(String(255))
    price = Column(Float)
    image = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(
        Enum(
            ProductStatus,
            name="product_status",
            create_type=True,
        ),
        default=ProductStatus.ACTIVE.value,
    )
    current_inventory = Column(Integer, default=0)
    category = relationship("Category", back_populates="products")
    inventory_transactions = relationship("Inventory", back_populates="product")
    sales = relationship("Sales", back_populates="products")
