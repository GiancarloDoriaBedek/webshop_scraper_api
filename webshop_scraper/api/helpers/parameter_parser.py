from scraper.scrapers.webshops import Webshop
from .enum_parser import EnumParser

from rest_framework.exceptions import APIException, ParseError
from enum import Enum

from scraper.scrapers.parameters import Param

class ParameterParser(object):
    def __init__(self) -> None:
        pass


    def map_website_name_to_enum(self, website_name: str):
        try:
            enum_value = EnumParser.parse_from_string(Webshop, website_name)
        except ValueError:
            raise ParseError(f'Website with name: {website_name} could not be found')
        
        return enum_value
    

    def map_website_id_to_enum(self, website_id: int):
        try:
            enum_value = EnumParser.parse_from_int(Webshop, website_id)
        
        except ValueError:
            raise ParseError(f'Website with id: {website_id} could not be found')
            
        return enum_value
    

    def safe_parameter_parse(self, params, property: Param):
        try:
            if property is None or params is None:
                raise KeyError
            
            property_value = params[property.value]
            
        except ValueError:
            raise ParseError(f'"{property.name}" is not a valid property name')
        except KeyError:
            raise ParseError(f'Property of "{property.name}" does not exist')

        return property_value
