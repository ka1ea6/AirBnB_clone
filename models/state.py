#!/usr/bin/env python3
'''Module for defining a class for representing a State'''

from .base_model import BaseModel


class State(BaseModel):
    '''Class for representing a state'''

    name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
