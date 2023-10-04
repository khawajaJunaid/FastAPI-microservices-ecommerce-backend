from enum import EnumMeta, Enum

class ProductStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class ProductCategory(str, Enum):
    ELECTRONICS = "electronics"
    FASHION = "fashion"
    PERSONAL_CARE = "personal_care"
    TOYS = "toys"
    HOME = "home"
    