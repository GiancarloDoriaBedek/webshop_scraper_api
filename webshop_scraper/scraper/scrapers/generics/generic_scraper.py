from abc import ABC, abstractmethod
from enum import Enum
from bs4 import BeautifulSoup
import requests


class Unit(Enum):
    GRAM = 'g'
    KILOGRAM = 'kg'
    LITRE = 'l'
    MILLILITRE = 'ml'
    UNIT = 'unit'


class GenericScraper(ABC):
    """

    """
    HTML_PARSER = 'lxml'


    def __init__(self) -> None:
        super().__init__()

        self.soup = None # beautifulsoup

    
    def __str__(self) -> str:
        return 'generic scraper'    


    @abstractmethod
    def scrape_products(self):
        pass


    @abstractmethod
    def scrape_store_info(self, page_link: str):
        pass


    @abstractmethod
    def scrape_product_categories(self):
        pass


    @abstractmethod
    def scrape_pages(self, category_link: str):
        pass


    def cook_soup(self, website_link: str):
        html_file = requests.get(website_link)
        if html_file.status_code != 200:
            # throw an error in the future
            return

        return BeautifulSoup(html_file.content, GenericScraper.HTML_PARSER)
    

    def _empty_str_if_none(self, value):
        return value if value is not None else ""
    

    def _parse_price(self, value: str):
        if '.' not in value and ',' not in value:
            return float(value)

        elif value[-3] in ',.':
            dec_char = value[-3]
            sep_char = {'.': ',', ',':'.'}[dec_char]
            value = value.replace(sep_char, '')
            value = value.replace(',', '.')
            return float(value)

        else:
            value = value.replace(',','').replace('.', '')
            return float(value)
        

    def _parse_currency(self, value: str):
        return value
    

    def _parse_unit_of_measurement(self, unit_of_measurement: str)-> Unit:
        unit = unit_of_measurement.split('/')[-1].lower()
        
        match unit:
            case 'kom' | 'unit' | 'komad' | 'jed' | 'jedinica':
                return Unit.UNIT
            
            case 'g' | 'gram':
                return Unit.GRAM
            
            case 'kg' | 'kilo' | 'kilogram':
                return Unit.KILOGRAM
            
            case 'ml' | 'millilitre':
                return Unit.MILLILITRE
            
            case 'l' | 'litre':
                return Unit.LITRE
            
            case _:
                return Unit.UNIT


    def _get_package_unit_of_measurement(self, product_package_quantity: float, unit_of_measurement: Unit)-> Unit:
        if product_package_quantity >= 1:
            return unit_of_measurement
        
        match unit_of_measurement:
            case Unit.LITRE:
                return Unit.MILLILITRE
            
            case Unit.KILOGRAM:
                return Unit.GRAM
            
            case _:
                return unit_of_measurement
            

    def _adjust_quantity_to_new_unit(self, value: float, upcast:bool=False):
        if upcast:
            return value / 1000
        
        return round(value * 1000)
    

    def _generate_link(self, domain: str, path: str, lstrip_path: bool=True):
        if lstrip_path is True:
            path = path.lstrip('/')
            
        return domain + path
