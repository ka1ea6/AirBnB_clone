#!/usr/bin/env python3
'''Module for defining a class for representing a User'''

from .base_model import BaseModel


class User(BaseModel):
    '''Class for representing a user'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
