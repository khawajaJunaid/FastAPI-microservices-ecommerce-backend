from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    class Config:
        orm_mode = True
