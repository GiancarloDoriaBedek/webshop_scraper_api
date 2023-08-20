from .get_data_generic import GetData


class GetProductCategories(GetData):
    def __init__(self, parameters) -> None:
        super().__init__(parameters)


    def parse_data(self):
        super().parse_data()
        pass


    def scrape_data(self):
        self.scraped_data = self.scraper.scrape_product_categories()
