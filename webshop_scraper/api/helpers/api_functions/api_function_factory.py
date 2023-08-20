from enum import Enum

from .get_pages import GetCategoryPages
from .get_product_categories import GetProductCategories
from .get_products import GetProducts
from .get_store_info import GetStoreInfo

class ApiFunction(Enum):
    """
    All available api functionalities
    """
    GET_PRODUCTS = 1
    GET_CATEGORIES = 2
    GET_PAGES = 3
    GET_STORE_INFO = 4


def api_factory(api_function: ApiFunction, parameters):
    """
    Creates a class with functionality defined by provided ApiFunction enum
    """
    match api_function:
        case ApiFunction.GET_PRODUCTS:
            return GetProducts(parameters)

        case ApiFunction.GET_CATEGORIES:
            return GetProductCategories(parameters)

        case ApiFunction.GET_PAGES:
            return GetCategoryPages(parameters)

        case ApiFunction.GET_STORE_INFO:
            return GetStoreInfo(parameters)

        case _:
            raise ValueError("Missing functionality")