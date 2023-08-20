from ..exceptions.scraper_exceptions import MissingScraperException

from .konzum.konzum_scraper import KonzumScraper
from .plodine.plodine_scraper import PlodineScraper

from .webshops import Webshop

class ScraperFactory(object):

    @classmethod
    def create_scraper(cls, webshop: Webshop):
        match webshop:
            case Webshop.konzum:
                return KonzumScraper()
            
            case Webshop.plodine:
                return PlodineScraper()
            
            case _:
                raise MissingScraperException()
