from ..generics.generic_scraper import GenericScraper
from ..parameters import Param
import requests
from bs4 import BeautifulSoup, PageElement

class KonzumScraper(GenericScraper):
    """

    """
    HOMEPAGE = 'https://www.konzum.hr/'
    SITE_NAVIGATION_TITLE = 'site-nav__title'
    CATEGORY_CLASS = 'nav-child-wrap-level-2'
    PAGINATION_CLASS = 'pagination'
    PRODUCT_LIST_CLASS = 'product-list--grid'
    PRODUCT_ARTICLE_CLASS = 'product-item product-default'
    PRODUCT_LINK_CLASS = 'link-to-product'


    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return 'konzum scraper'
     

    def scrape_products(self, page_link: str):
        soup = self.cook_soup(page_link)

        product_grid = soup.find('div', class_= KonzumScraper.PRODUCT_LIST_CLASS)
        product_articles = product_grid.find_all('article', class_=KonzumScraper.PRODUCT_ARTICLE_CLASS)
        products_data = list()
        for article in product_articles:
            print(article)
            print('*'*200)
            article_data = self.__get_product_article_data(article)
            products_data.append(article_data)

        return products_data
    

    def scrape_store_info(self):
        pass


    def scrape_product_categories(self):
        soup = self.cook_soup(KonzumScraper.HOMEPAGE)

        category_ul_elements = soup.find_all('ul', class_=KonzumScraper.CATEGORY_CLASS)
        category_li_elements = list()

        for ul in category_ul_elements:
            li_elements = ul.find_all('li')
            category_li_elements.extend(li_elements)

        categories_data = list()

        for li in category_li_elements:
            anchor = li.find('a')

            if not anchor:
                continue

            text = anchor.get_text(strip=True)
            link = anchor.get('href')

            category_data = {
                Param.CATEGORY_NAME.value: text, 
                Param.CATEGORY_LINK.value: link
                }
            
            categories_data.append(category_data)

        return categories_data


    def scrape_pages(self, category_link: str):
        soup = self.cook_soup(category_link)

        pagination_ul = soup.find('ul', class_=KonzumScraper.PAGINATION_CLASS)
        pagination_data = list()
        li_elements = pagination_ul.find_all('li')

        # Iterate through li elements
        for li in li_elements:
            page_link = li.find('a')
            if not page_link:
                continue

            page_number = page_link.get_text(strip=True)
            page_href = page_link.get('href')

            page_data = {
                Param.PAGE_NUMBER.value: page_number, 
                Param.PAGE_LINK.value: page_href}
            
            pagination_data.append(page_data)

        return pagination_data
    
    #private_methods
    
    def __get_product_article_data(self, article: PageElement):

        product_data_div: PageElement = article.find('div')

        # Product name
        product_name = product_data_div.get('data-ga-name')

        product_price_element = product_data_div.get('data-ga-price')
        product_price = self.__parse_price(product_price_element)

        product_brand = product_data_div.get('data-ga-brand')

        product_currency_element = product_data_div.get('data-ga-currency')
        product_currency = self.__parse_currency(product_currency_element)

        product_data[Param.PRODUCT_NAME.value] = product_data_div.get('data-ga-name')

        # Product URL
        product_anchor = article.find('a', class_=KonzumScraper.PRODUCT_LINK_CLASS)
        product_url = product_anchor.get('href')
        product_data[Param.PRODUCT_URL.value] = product_url

        # Product image URL
        product_image= product_anchor.find('img')
        product_image_url = product_image['src']
        product_data[Param.PRODUCT_IMAGE_URL.value] = product_image_url

        product_data = {
            Param.PRODUCT_NAME.value: self.__empty_str_if_none(product_name),
            Param.PRODUCT_PRICE.value: self.__empty_str_if_none(product_price),
            Param.PRODUCT_PRICE_DATE_START: "",
            Param.PRODUCT_PRICE_DATE_END: "",
            Param.PRODUCT_URL: "",
            Param.PRODUCT_IMAGE_URL: ","
        }



        # Product price

        # Product unit

        # Product price per unit 02398939
        return product_data



