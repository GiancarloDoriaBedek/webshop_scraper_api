from enum import Enum


class Param(Enum):
    WEBSITE = 'website'
    PAGE_NUMBER = 'page number'
    PAGE_LINK = 'page_link'
    CATEGORY_NAME = 'category_name'
    CATEGORY_LINK = 'category_link'
    PRODUCT = 'product'
    PRODUCT_NAME = 'product_name'
    PRODUCT_URL = 'product_url'
    PRODUCT_IMAGE_URL = 'product_image_url'
    PRODUCT_PRICE = 'product_price'
    PRODUCT_PRICE_DATE_START = 'product_price_date_start'
    PRODUCT_PRICE_DATE_END = 'product_price_date_end'
    PRODUCT_QUANTITY = 'product_quantity'
    PRODUCT_UNIT_OF_MEASUREMENT = 'product_unit_of_measurement'
    PRODUCT_PRICE_PER_UNIT_OF_MEASUREMENT = 'product_price_per_unit_of_measurement'