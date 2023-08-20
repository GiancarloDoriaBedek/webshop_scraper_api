from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests

class GenericScraper(ABC):
    """

    """
    HTML_PARSER = 'lxml'
    UNITS = ['kg', 'l', 'kom']

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
    

    def __empty_str_if_none(self, value: str):
        return value if value is not None else ""