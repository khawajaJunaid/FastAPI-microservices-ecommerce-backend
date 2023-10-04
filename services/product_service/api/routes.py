from fastapi import APIRouter, Depends, HTTPException, status
from api.schemas import ProductCreate, Product, Category, CategoryCreate
from starlette.responses import RedirectResponse
from api.controller import create_product, create_category, get_category_by_name
import traceback
from common.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
def main():
    return RedirectResponse(url="/docs/")


# API Endpoints
@router.post("/create/", response_model=Product, status_code=201)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        created_product = create_product(product, db)
        return created_product
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/create_category", response_model=Category, status_code=201)
def create_product_category(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        category = create_category(category, db)
        return category
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Server Error")
