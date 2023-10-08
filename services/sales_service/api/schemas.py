from pydantic import BaseModel
from common.Enums.product_enums import ProductCategory
from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional


class SalesBase(BaseModel):
    product_id: int
    category_name: ProductCategory
    units_sold: int = 0

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


class SalesRequestParams(BaseModel):
    """
    Represents the request parameters for retrieving sales data.

    Attributes:
    -----------
    product_id : Optional[int]
        The ID of the product to retrieve sales data for.
    category : Optional[str]
        The category of products to retrieve sales data for.
    start_date : Optional[str]
        The start date of the sales data to retrieve.
    end_date : Optional[str]
        The end date of the sales data to retrieve.
    group_by : Optional[str]
        The field to group the sales data by.
    """

    product_id: Optional[int] = None
    category: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    group_by: Optional[str] = None
