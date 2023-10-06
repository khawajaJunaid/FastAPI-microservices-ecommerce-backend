from fastapi import APIRouter, Depends, HTTPException, status
from api.schemas import (
    ProductCreate,
    Product,
    Category,
    CategoryCreate,
    ProductUpdate,
    InventoryCreate,
)
from starlette.responses import RedirectResponse
from api.controller import (
    create_product,
    create_category,
    update_product_attribute,
    get_product_by_id,
    get_product_inventory_history,
)
import traceback
from common.db.session import get_db
from sqlalchemy.orm import Session
from common.custom_exceptions import ProductNotFoundException

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


@router.put("/update", status_code=200)
def update_product(
    updated_attributes: ProductUpdate, product_id, db: Session = Depends(get_db)
):
    try:
        props_to_update = {
            key: value
            for key, value in updated_attributes.dict().items()
            if value is not None or key == "current_inventory"
        }

        db_product = update_product_attribute(product_id, props_to_update, db)
        return db_product

    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/get_product/", response_model=Product, status_code=200)
def get_product_inventory(product_id: int, db: Session = Depends(get_db)):
    try:
        result = get_product_by_id(product_id, db)

        return result

    except ProductNotFoundException as error:
        raise HTTPException(status_code=404, detail=str(error))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/inventory_history", status_code=200)
def get_product_inventory(product_id, db: Session = Depends(get_db)):
    try:
        result = get_product_inventory_history(product_id, db)

        return result
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Server Error")
