from pydantic import BaseModel
from common.Enums.product_enums import ProductCategory
from pydantic import BaseModel, validator


# product schemas
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image: str
    category_name: ProductCategory

    @validator("category_name")
    def validate_category(cls, value):
        print("category values:", ProductCategory.__members__)
        valid_values = [item for item in ProductCategory]
        print(valid_values)
        if value not in valid_values:
            raise ValueError("Invalid category")
        return value


class ProductCreate(ProductBase):
    pass


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
