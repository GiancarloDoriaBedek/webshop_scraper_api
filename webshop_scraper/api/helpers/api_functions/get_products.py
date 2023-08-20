from .get_data_generic import GetData
from scraper.scrapers.parameters import Param


class GetProducts(GetData):
    def __init__(self, parameters) -> None:
        super().__init__(parameters)
        self.page_link = None


    def parse_data(self):
        super().parse_data()
        
        self.page_link = self.parameter_parser.safe_parameter_parse(
            self.parameters, 
            Param.PAGE_LINK)


    def scrape_data(self):
        self.scraped_data = self.scraper.scrape_products(self.page_link)