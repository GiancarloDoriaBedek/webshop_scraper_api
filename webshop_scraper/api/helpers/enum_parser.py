from enum import Enum


class EnumParser(object):
    @classmethod
    def parse_from_int(cls, enum_type: Enum, value: int):
        for webshop in enum_type:
            if webshop.value == value:
                return webshop
        
        raise ValueError(f"No {enum_type.__name__} member with value {value}")
    

    @classmethod
    def parse_from_string(cls, enum_type: Enum, value: str):
        try:
            return enum_type[value]
        except KeyError:
            raise ValueError(f"No {enum_type.__name__} member with name {value}")
        
    
    @classmethod
    def string_from_enum(cls, enum_type: Enum, enum_member: Enum):
        for key, value in enum_type.__members__.items():
            if value == enum_member:
                return key
            
        raise ValueError("Enum member not found")