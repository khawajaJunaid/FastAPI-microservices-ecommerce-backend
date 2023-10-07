import requests
import os
from http import HTTPStatus as HttpStatus
from common.db.models.sales import Sales
from sqlalchemy.orm import Session
from common.custom_exceptions import (
    ProductNotFoundException,
    ProductOutofStockException,
    ProductInventoryUpdateException,
)


def create_product_sale_transaction(sale: Sales, db: Session):
    """
    Create product sale transaction:
    - validation for payload using pydantic models
    - check on category if it exists in db
    - create product sale transaction in db

    """
    db_sale = Sales(**sale.dict())

    print("payload received for sale: ", vars(db_sale))
    product_service_response = get_product_details_by_id(db_sale.product_id)

    if product_service_response.status_code != HttpStatus.OK:
        raise ProductNotFoundException("Product not found")
    product_service_response = product_service_response.json()
    print("product_service_response: ", product_service_response)
    current_inventory_quantity = product_service_response.get("current_inventory")
    if current_inventory_quantity >= db_sale.units_sold:
        print("Product stock exists for sale")
        set_quantity_after_decrement = current_inventory_quantity - db_sale.units_sold
        product_update_response = decrement_product_inventory(
            set_quantity_after_decrement, db_sale.product_id
        )
        if product_update_response.status_code != HttpStatus.OK:
            raise ProductInventoryUpdateException("Error updating product inventory")
        else:
            print("Product inventory updated")
            db.add(db_sale)
            db.commit()
            db.refresh(db_sale)
            return db_sale
    else:
        print("Product has gone out of stock!")
        raise ProductOutofStockException("Product has gone out of stock!")


def get_product_details_by_id(product_id: int):
    """
    Get product details by id
    - creates an http request to the product microservice for details
    """
    base_path = os.getenv(
        "PRODUCT_SERVICE_URL", "http://ecommerce-product_service-1:8000"
    )
    url = f"{base_path}/products/get_product/?product_id={product_id}"
    print("Reqpyuesting product details from product service at: ", url)
    result = requests.get(url=url)
    return result


def decrement_product_inventory(new_quantity: int, product_id: int):
    """
    Get product details by id
    - creates an http request to the product microservice for details
    """
    base_path = os.getenv(
        "PRODUCT_SERVICE_URL", "http://ecommerce-product_service-1:8000"
    )
    url = f"{base_path}/products/update/?product_id={product_id}"

    update_inventory_body = {"current_inventory": new_quantity}
    result = requests.put(url=url, json=update_inventory_body)

    return result
