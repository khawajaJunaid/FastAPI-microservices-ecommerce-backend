from api.schemas import ProductCreate, CategoryCreate
from common.db.models.products import Product
from common.db.models.category import Category
from sqlalchemy.orm import Session


def create_product(product: ProductCreate, db: Session):
    """
    Create product:
    - validation for payload using pydantic models
    - check on category if it exists in db
    - create product in db

    """
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def create_category(category: CategoryCreate, db: Session):
    """
    Create category:
    - validation for payload using pydantic models
    - create category in db

    """
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category_by_name(category_name: str, db: Session):
    """
    Get category by name
    """
    return db.query(Category).filter(Category.name == category_name).first()
