# common_db/models/products.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from common.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    # category_id = Column(Integer, ForeignKey("categories.category_id"))
    name = Column(String(60), index=True)
    description = Column(String(255))
    price = Column(Float)
    image = Column(String(255))

    # category = relationship("Category", back_populates="products")

    # @classmethod
    # def get_by_id(cls, product_id: int):
    #     db = SessionLocal()
    #     product = db.query(cls).filter(cls.product_id == product_id).first()
    #     db.close()
    #     return product
