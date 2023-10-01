from api.schemas import ProductCreate
from common.db.models.products import Product
from sqlalchemy.orm import Session


def create_product(product: ProductCreate, db: Session):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
