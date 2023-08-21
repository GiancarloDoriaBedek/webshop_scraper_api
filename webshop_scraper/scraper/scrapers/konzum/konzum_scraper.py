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
            page_href = self._generate_link(KonzumScraper.HOMEPAGE, page_link.get('href'))

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

        # Product native ID
        product_native_ID = product_data_div.get('data-ga-id')

        # Product brand
        product_brand = product_data_div.get('data-ga-brand')

        # Product price
        product_price_element = product_data_div.get('data-ga-price')
        print(product_price_element)
        product_price_element = str(product_price_element).split(' ')[0]
        print(product_price_element)
        product_price = self._parse_price(product_price_element)

        # Product currency
        product_currency_element = product_data_div.get('data-ga-currency')
        product_currency = self._parse_currency(product_currency_element)

        # Product price start date
        # Product price end date

        # Product URL
        product_image_div = article.find('div', class_='product-default__image')
        product_anchor = product_image_div.find('a', class_=KonzumScraper.PRODUCT_LINK_CLASS)
        product_url = self._generate_link(KonzumScraper.HOMEPAGE, product_anchor.get('href'))

        # Product image URL
        product_image= product_anchor.find('img')
        product_image_url = product_image['src']

        # Product price per unit / Product unit of measurement
        product_meta_details_div = article.find('div', class_='product-default__meta-details')
        price_element = product_meta_details_div.find('strong').text
        price_value, per_unit = price_element.split(' ')
        price_per_unit = self._parse_price(price_value)
        unit_of_measurement = self._parse_unit_of_measurement(per_unit)

        # Product package quantity
        product_package_quantity = product_price / price_per_unit

        # Product package unit of measurement
        product_package_unit = self._get_package_unit_of_measurement(product_package_quantity, unit_of_measurement)

        if unit_of_measurement != product_package_unit:
            product_package_quantity = self._adjust_quantity_to_new_unit(product_package_quantity)

        product_data = {
            Param.PRODUCT_NAME.value: self._empty_str_if_none(product_name),
            Param.PRODUCT_NATIVE_ID.value:  self._empty_str_if_none(product_native_ID),
            Param.PRODUCT_BRAND.value: self._empty_str_if_none(product_brand),
            Param.PRODUCT_PRICE.value: self._empty_str_if_none(product_price),
            Param.PRODUCT_CURRENCY.value: self._empty_str_if_none(product_currency),
            Param.PRODUCT_PRICE_DATE_START.value: "",
            Param.PRODUCT_PRICE_DATE_END.value: "",
            Param.PRODUCT_URL.value: self._empty_str_if_none(product_url),
            Param.PRODUCT_IMAGE_URL.value: self._empty_str_if_none(product_image_url),
            Param.PRODUCT_UNIT_OF_MEASUREMENT.value: unit_of_measurement.value,
            Param.PRODUCT_PRICE_PER_UNIT_OF_MEASUREMENT.value: self._empty_str_if_none(price_per_unit),
            Param.PRODUCT_PACKAGE_QUANTITY.value: product_package_quantity,
            Param.PRODUCT_PACKAGE_UNIT_OF_MEASUREMENT.value: product_package_unit.value
        }

        return product_data
