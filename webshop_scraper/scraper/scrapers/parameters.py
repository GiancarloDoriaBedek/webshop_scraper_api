from enum import Enum

# TODO: Change to dataclass
class Param(Enum):
    WEBSITE = 'StoreName'
    PAGE_NUMBER = 'PageNumber'
    PAGE_LINK = 'PageURL'
    CATEGORY_NAME = 'CategoryName'
    CATEGORY_LINK = 'CategoryURL'
    PRODUCT = 'Product'
    PRODUCT_NAME = 'ProductName'
    PRODUCT_NATIVE_ID = 'ProductNativeID'
    PRODUCT_BRAND = 'ProductBrand'
    PRODUCT_PRICE = 'ProductPrice'
    PRODUCT_CURRENCY = 'ProductCurrency'
    PRODUCT_PRICE_DATE = 'PriceDate'
    PRODUCT_PRICE_DATE_START = 'ProductPriceStartDate'
    PRODUCT_PRICE_DATE_END = 'ProductPriceEndDate'
    PRODUCT_URL = 'ProductURL'
    PRODUCT_IMAGE_URL = 'ProductImageURL'
    PRODUCT_UNIT_OF_MEASUREMENT = 'ProductUnitOfMeasurement'
    PRODUCT_PACKAGE_UNIT_OF_MEASUREMENT = 'ProductPackageUnitOfMeasurement'
    PRODUCT_PRICE_PER_UNIT_OF_MEASUREMENT = 'ProductPricePerUnitOfMeasurement'
    PRODUCT_PACKAGE_QUANTITY = 'ProductPackageQuantity'
