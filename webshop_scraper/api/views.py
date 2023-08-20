import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from scraper.scrapers.scraper_factory import ScraperFactory
from scraper.scrapers.webshops import Webshop
from .helpers.parameter_parser import ParameterParser
from .helpers.parameter_parser import Param

from .helpers.api_functions.api_function_factory import api_factory, ApiFunction



@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    anus
    """
    body = request.body
    data = dict()
    print(request.GET)

    try:
        data = json.loads(body)
        data['headers'] = request.headers
        data['content_type'] = request.content_type
    except:
        pass

    print(body)
    return Response(data)


@api_view(["GET"])
def get_product_categories(request, *args, **kwargs):
    body = request.body
    try:
        parameters = json.loads(body)

    except:
        return Response('Mising body')
    
    function = api_factory(ApiFunction.GET_CATEGORIES, parameters)
    function.parse_data()
    function.scrape_data()
    
    return Response(function.scraped_data, content_type='application/json')


@api_view(["GET"])
def get_product(request, *args, **kwargs):
    pass


@api_view(["GET"])
def get_products(request, *args, **kwargs):
    body = request.body
    try:
        parameters = json.loads(body)

    except:
        return Response('Mising body')
    
    function = api_factory(ApiFunction.GET_PRODUCTS, parameters)
    function.parse_data()
    function.scrape_data()
    
    return Response(function.scraped_data, content_type='application/json')


@api_view(["GET"])
def get_store_info(request, *args, **kwargs):
    body = request.body
    try:
        parameters = json.loads(body)

    except:
        return Response('Mising body')
    
    function = api_factory(ApiFunction.GET_STORE_INFO, parameters)
    function.parse_data()
    function.scrape_data()
    
    return Response(function.scraped_data, content_type='application/json')




@api_view(["GET"])
def get_pages(request, *args, **kwargs):
    body = request.body
    try:
        parameters = json.loads(body)

    except:
        return Response('Mising body')
    
    function = api_factory(ApiFunction.GET_PAGES, parameters)
    function.parse_data()
    function.scrape_data()
    
    return Response(function.scraped_data, content_type='application/json')