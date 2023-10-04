# common_db/models/products.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from common.db.base import Base
from sqlalchemy import Enum
import datetime
from common.Enums.product_enums import ProductStatus
from common.Enums.product_enums import ProductCategory


class Product(Base):
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
    category = relationship("Category", back_populates="products")

    # @classmethod
    # def get_by_id(cls, product_id: int):
    #     db = SessionLocal()
    #     product = db.query(cls).filter(cls.product_id == product_id).first()
    #     db.close()
    #     return product
