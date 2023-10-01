from fastapi import APIRouter, Depends, HTTPException, status
from api.schemas import ProductCreate, Product
from starlette.responses import RedirectResponse
from api.controller import create_product
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
        print("Getting details here", product)
        created_product = create_product(product, db)
        return created_product
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Server Error")
