#!/usr/bin/env python3
'''Module for defining a class for representing a Amenity'''

from .base_model import BaseModel


class Amenity(BaseModel):
    '''Class for representing a Amenity'''

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
