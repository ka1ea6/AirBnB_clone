#!/usr/bin/env python3
'''Module for defining a class for representing a City'''

from .base_model import BaseModel


class City(BaseModel):
    '''Class for representing a city'''

    name = ''
    state_id = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
