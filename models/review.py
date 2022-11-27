#!/usr/bin/env python3
'''Module for defining a class for representing a Review'''

from .base_model import BaseModel


class Review(BaseModel):
    '''Class for representing a review'''

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
