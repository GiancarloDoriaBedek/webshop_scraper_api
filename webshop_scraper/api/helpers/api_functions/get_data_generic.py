from abc import ABC, abstractmethod
from ..parameter_parser import ParameterParser

from scraper.scrapers.parameters import Param
from scraper.scrapers.scraper_factory import ScraperFactory
from scraper.scrapers.generics.generic_scraper import GenericScraper 

class GetData(ABC):
    def __init__(self, parameters) -> None:
        self.scraper: GenericScraper = None
        self.parameter_parser = ParameterParser()
        self.parameters = parameters
        self.scraped_data = dict()

    @abstractmethod
    def parse_data(self):
        self.scraper = self.create_scraper()


    @abstractmethod
    def scrape_data(self):
        pass

    
    def create_scraper(self):
        webshop_name = self.webshop_name()
        webshop_enum = self.parameter_parser.map_website_name_to_enum(webshop_name)

        return ScraperFactory.create_scraper(webshop_enum)
    

    def webshop_name(self):
        webshop_name = self.parameter_parser.safe_parameter_parse(self.parameters, Param.WEBSITE)

        return webshop_name
    

    
