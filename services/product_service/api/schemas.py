from pydantic import BaseModel
from common.Enums.product_enums import ProductCategory
from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional


# product schemas
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image: str
    category_name: ProductCategory
    current_inventory: int = 0

    @validator("category_name")
    def validate_category(cls, value):
        valid_values = [item for item in ProductCategory]
        if value not in valid_values:
            raise ValueError("Invalid category")
        return value


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    image: Optional[str]
    category_name: Optional[ProductCategory]
    current_inventory: Optional[int]
    updated_at: datetime = datetime.utcnow()

    @validator("category_name")
    def validate_category(cls, value):
        if value is not None:
            valid_values = [item for item in ProductCategory]
            if value not in valid_values:
                raise ValueError("Invalid category")
        return value


class Product(ProductBase):
    class Config:
        orm_mode = True


# category schemas
class CategoryBase(BaseModel):
    name: str
    description: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    class Config:
        orm_mode = True


class InventoryBase(BaseModel):
    product_id: int
    low_stock_alert_threshold: int = 10
    category_name: ProductCategory
    inventory_quantity: int = 0


class InventoryCreate(InventoryBase):
    pass


class Inventory(InventoryBase):
    class Config:
        orm_mode = True
