from ..generics.generic_scraper import GenericScraper


class PlodineScraper(GenericScraper):
    """

    """
    def __init__(self) -> None:
        super().__init__()


    def __str__(self) -> str:
        return 'plodine scraper' 


    def scrape_products(self, page_link: str):
        pass


    def scrape_store_info(self):
        pass


    def scrape_product_categories(self):
        pass


    def scrape_pages(self, category_link: str):
        pass