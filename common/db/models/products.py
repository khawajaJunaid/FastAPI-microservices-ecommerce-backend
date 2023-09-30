# common_db/models/products.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from common.db.base import Base
from common.db.session import SessionLocal



class Product(Base):
    _tablename_ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    product_name = Column(String, index=True)
    product_description = Column(String)
    product_price = Column(Float)
    product_image = Column(String)

    category = relationship("Category", back_populates="products")

    @classmethod
    def get_by_id(cls, product_id: int):
        db = SessionLocal()
        product = db.query(cls).filter(cls.product_id == product_id).first()
        db.close()
        return product

    @classmethod
    def create(cls, **kwargs):
        db = SessionLocal()
        product = cls(**kwargs)
        db.add(product)
        db.commit()
        db.refresh(product)
        db.close()
        return product