import requests
import os
from http import HTTPStatus as HttpStatus
from common.db.models.sales import Sales
from sqlalchemy.orm import Session
from common.custom_exceptions import (
    ProductNotFoundException,
    ProductOutofStockException,
    ProductInventoryUpdateException,
    NoSalesDataFoundException,
    InsufficientInventoryException,
)
from datetime import datetime
from sqlalchemy import func
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import SQLAlchemyError


def create_product_sale_transaction(sale: Sales, db: Session):
    """
    Create product sale transaction:
    - validation for payload using pydantic models
    - check on category if it exists in db
    - create product sale transaction in db

    """
    try:
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
            set_quantity_after_decrement = (
                current_inventory_quantity - db_sale.units_sold
            )
            product_update_response = decrement_product_inventory(
                set_quantity_after_decrement, db_sale.product_id
            )
            if product_update_response.status_code != HttpStatus.OK:
                raise ProductInventoryUpdateException(
                    "Error updating product inventory"
                )
            else:
                print("Product inventory updated")
                # Calculate total_price and revenue based on price and units_sold
                db_sale.total_price = (
                    product_service_response["price"] * db_sale.units_sold
                )
                db_sale.revenue = db_sale.total_price
                db.add(db_sale)
                db.commit()
                db.refresh(db_sale)
                return db_sale
        elif current_inventory_quantity > 0:
            reduce_by = db_sale.units_sold - current_inventory_quantity
            print("Product available for ordering but in reduced quantity")
            raise InsufficientInventoryException(
                f"Insufficient inventory for full order. You can order a reduced quantity, please reduce the quantity by {reduce_by}"
            )
        else:
            print("Product has gone out of stock!")
            raise ProductOutofStockException("Product has gone out of stock!")

    except SQLAlchemyError as e:
        # Rollback the transaction if an exception occurs
        db.rollback()
        raise e  # Re-raise the exception to handle it at a higher level

    finally:
        # Close the session when done
        db.close()


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


def fetch_sales(
    db: Session,
    product_id=None,
    category=None,
    start_date=None,
    end_date=None,
    group_by=None,
):
    """
    Fetches sales data from the database based on the specified criteria.

    Args:
        db (Session): The database session object.
        product_id (int, optional): The ID of the product to filter by. Defaults to None.
        category (str, optional): The name of the category to filter by. Defaults to None.
        start_date (datetime, optional): The start date to filter by. Defaults to None.
        end_date (datetime, optional): The end date to filter by. Defaults to None.
        group_by (str, optional): The time period to group the sales data by (day, month, year, category-year, category-month, category-date, product_id-year, product_id-month, product_id-date, etc.). Defaults to None.

    Returns:
        List: A list of sales data matching the specified criteria, including product ID and category.

    Raises:
        NoSalesDataFoundException: If no sales data is found for the specified criteria.
        ProductNotFoundException: If the specified product ID is not found in the database.
    """
    try:
        # Build the query with selected columns
        sales_query = db.query(
            Sales.product_id,
            Sales.category_name,
            func.max(Sales.sold_at).label("last_sold_at"),
            func.sum(Sales.units_sold).label("total_units_sold"),
            func.sum(Sales.total_price).label("total_revenue"),
        )

        # Check if product exists
        if product_id is not None:
            product_details = get_product_details_by_id(product_id)

            # Check if the specified product exists
            if product_details.status_code != HttpStatus.OK:
                raise ProductNotFoundException("Product not found")

            sales_query = sales_query.filter(Sales.product_id == product_id)

        if category is not None:
            sales_query = sales_query.filter(Sales.category_name == category)

        if start_date is None:
            start_date = datetime.min
        if end_date is None:
            end_date = datetime.now()

        sales_query = sales_query.filter(
            Sales.sold_at >= start_date, Sales.sold_at <= end_date
        )

        # Apply grouping if specified
        if group_by:
            if group_by == "day":
                # Group by day
                sales_query = sales_query.group_by(
                    Sales.product_id,
                    Sales.category_name,
                    func.DATE(Sales.sold_at),
                )
            elif group_by == "month":
                # Group by month
                sales_query = sales_query.group_by(
                    Sales.product_id,
                    Sales.category_name,
                    func.YEAR(Sales.sold_at),
                    func.MONTH(Sales.sold_at),
                )
            elif group_by == "year":
                # Group by year
                sales_query = sales_query.group_by(
                    Sales.product_id,
                    Sales.category_name,
                    func.YEAR(Sales.sold_at),
                )
            elif group_by == "category-year":
                # Group by category and year
                sales_query = sales_query.group_by(
                    Sales.category_name,
                    func.extract("year", Sales.sold_at).label("year"),
                )
                # Exclude product_id from the select
                sales_query = sales_query.with_entities(
                    Sales.category_name,
                    func.extract("year", Sales.sold_at).label("year"),
                    func.max(Sales.sold_at).label("last_sold_at"),
                    func.sum(Sales.units_sold).label("total_units_sold"),
                    func.sum(Sales.total_price).label("total_revenue"),
                )
            elif group_by == "category-month":
                # Group by category and month
                sales_query = sales_query.group_by(
                    Sales.category_name,
                    func.extract("year", Sales.sold_at).label("year"),
                    func.extract("month", Sales.sold_at).label("month"),
                )
                # Exclude product_id from the select
                sales_query = sales_query.with_entities(
                    Sales.category_name,
                    func.extract("year", Sales.sold_at).label("year"),
                    func.extract("month", Sales.sold_at).label("month"),
                    func.max(Sales.sold_at).label("last_sold_at"),
                    func.sum(Sales.units_sold).label("total_units_sold"),
                    func.sum(Sales.total_price).label("total_revenue"),
                )
            elif group_by == "category-date":
                # Group by category and date
                sales_query = sales_query.group_by(
                    Sales.category_name,
                    func.DATE(Sales.sold_at),
                )
                # Exclude product_id from the select
                sales_query = sales_query.with_entities(
                    Sales.category_name,
                    func.DATE(Sales.sold_at).label("date"),
                    func.max(Sales.sold_at).label("last_sold_at"),
                    func.sum(Sales.units_sold).label("total_units_sold"),
                    func.sum(Sales.total_price).label("total_revenue"),
                )
            elif group_by == "product_id-year":
                # Group by product_id and year
                sales_query = sales_query.group_by(
                    Sales.product_id,
                    func.extract("year", Sales.sold_at).label("year"),
                )
                # Exclude category_name from the select
                sales_query = sales_query.with_entities(
                    Sales.product_id,
                    func.extract("year", Sales.sold_at).label("year"),
                    func.max(Sales.sold_at).label("last_sold_at"),
                    func.sum(Sales.units_sold).label("total_units_sold"),
                    func.sum(Sales.total_price).label("total_revenue"),
                )
            elif group_by == "product_id-month":
                # Group by product_id and month
                sales_query = sales_query.group_by(
                    Sales.product_id,
                    func.extract("year", Sales.sold_at).label("year"),
                    func.extract("month", Sales.sold_at).label("month"),
                )
                # Exclude category_name from the select
                sales_query = sales_query.with_entities(
                    Sales.product_id,
                    func.extract("year", Sales.sold_at).label("year"),
                    func.extract("month", Sales.sold_at).label("month"),
                    func.max(Sales.sold_at).label("last_sold_at"),
                    func.sum(Sales.units_sold).label("total_units_sold"),
                    func.sum(Sales.total_price).label("total_revenue"),
                )
            elif group_by == "product_id-date":
                # Group by product_id and date
                sales_query = sales_query.group_by(
                    Sales.product_id,
                    func.DATE(Sales.sold_at),
                )
                # Exclude category_name from the select
                sales_query = sales_query.with_entities(
                    Sales.product_id,
                    func.DATE(Sales.sold_at).label("date"),
                    func.max(Sales.sold_at).label("last_sold_at"),
                    func.sum(Sales.units_sold).label("total_units_sold"),
                    func.sum(Sales.total_price).label("total_revenue"),
                )
            elif group_by == "category":
                # Group only by category
                sales_query = sales_query.group_by(
                    Sales.category_name,
                )
                sales_query = sales_query.with_entities(
                    Sales.category_name,
                    func.max(Sales.sold_at).label("last_sold_at"),
                    func.sum(Sales.units_sold).label("total_units_sold"),
                    func.sum(Sales.total_price).label("total_revenue"),
                )
        else:
            # Group by product_id and category
            sales_query = sales_query.group_by(
                Sales.product_id,
                Sales.category_name,
                Sales.sold_at
            )
        print("sales query statement \n\n\n", sales_query.statement, "\n\n\n\n")
        result = sales_query.all()

        if not result:
            raise NoSalesDataFoundException(
                "No sales data found for the specified criteria"
            )

        return result

    except NoResultFound as exc:
        raise ProductNotFoundException("Product not found") from exc

    except Exception as e:
        raise e
