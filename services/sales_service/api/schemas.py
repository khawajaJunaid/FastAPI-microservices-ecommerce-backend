from pydantic import BaseModel
from common.Enums.product_enums import ProductCategory
from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional


class SalesBase(BaseModel):
    product_id: int
    category_name: ProductCategory
    units_sold: int = 0
    revenue: float
    total_price: float

    @validator("category_name")
    def validate_category(cls, value):
        if value is not None:
            valid_values = [item for item in ProductCategory]
            if value not in valid_values:
                raise ValueError("Invalid category")
        return value


class SalesCreate(SalesBase):
    pass


class Sales(SalesBase):
    class Config:
        orm_mode = True
