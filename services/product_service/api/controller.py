from api.schemas import ProductCreate, CategoryCreate, InventoryCreate
from common.db.models.products import Product
from common.db.models.category import Category
from common.db.models.inventory import Inventory
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from common.Enums.product_enums import ProductCategory
from common.custom_exceptions import ProductNotFoundException


def create_product(product: ProductCreate, db: Session):
    """
    Create product:
    - validation for payload using pydantic models
    - check on category if it exists in db
    - create product in db

    """

    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    inventory_data = InventoryCreate(
        category_name=db_product.category_name,
        product_id=db_product.id,
        inventory_quantity=db_product.current_inventory,
    )

    try:
        create_inventory(inventory_data, db)
    except Exception as error:
        print("Error creating inventory: ", error)

    return db_product


def update_product_attribute(product_id: int, updated_attributes: dict, db: Session):
    """
    Update product attributes based on a dictionary of updated values:
    - Update specified attributes of the product in db
    - Create or update inventory if 'current_inventory' is in updated_attributes

    Args:
        product_id (int): The ID of the product to update.
        updated_attributes (dict): A dictionary of updated product attributes.
        db (Session): SQLAlchemy database session.

    Returns:
        dict: A dictionary containing the result of the update operation.
    """
    try:
        # Retrieve the existing product from the database
        db_product = db.query(Product).filter_by(id=product_id).first()

        if db_product:
            # Update only the specified attributes present in updated_attributes
            for key, value in updated_attributes.items():
                if hasattr(db_product, key):
                    setattr(db_product, key, value)
            db.commit()
            # Refresh the db_product to get the updated values
            db.refresh(db_product)
            if "current_inventory" in updated_attributes:
                # The "current_inventory" key exists in the dictionary
                inventory_data = InventoryCreate(
                    product_id=product_id,
                    category_name=db_product.category_name,
                    inventory_quantity=updated_attributes["current_inventory"],
                )
                create_inventory(inventory_data, db)
            db.refresh(db_product)
            print("db: ", vars(db_product))
            return {
                "success": True,
                "message": "Product attributes updated successfully",
                "product": db_product,
            }
        else:
            return {
                "success": False,
                "message": f"Product with ID {product_id} not found",
            }

    except SQLAlchemyError as e:
        # Handle the database error and return an error response
        db.rollback()
        error_message = str(e)
        return {"success": False, "message": f"Database error: {error_message}"}
    except Exception as e:
        # Handle other exceptions and return an error response
        return {"success": False, "message": f"An error occurred: {str(e)}"}


def get_product_by_id(product_id: int, db: Session):
    result = db.query(Product).filter(Product.id == product_id).first()
    if result is None:
        raise ProductNotFoundException("Product not found")
    return result


def create_category(category: CategoryCreate, db: Session):
    """
    Create category:
    - validation for payload using pydantic models
    - create category in db

    """
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category_by_name(category_name: str, db: Session):
    """
    Get category by name
    """
    return db.query(Category).filter(Category.name == category_name).first()


def create_inventory(inventory: InventoryCreate, db: Session):
    db_inventory = Inventory(**inventory.dict())
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory


def get_product_inventory_history(product_id: int, db: Session):
    result = db.query(Inventory).filter(Inventory.product_id == product_id).all()

    if result is None:
        raise ProductNotFoundException("Product not found")
    return result
