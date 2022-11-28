#!/usr/bin/env python3
'''Module for the definition of a base model that
defines all common attributes/methods for other classes'''

import uuid
from datetime import datetime
import models


class BaseModel(object):
    '''Class defining base features found in different classes'''

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.__dict__ = {
                **kwargs, "created_at":
                datetime.fromisoformat(kwargs['created_at']),
                "updated_at": datetime.fromisoformat(kwargs['updated_at']),
                "__class__": ""
            }
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __setattr__(self, key, value):
        object.__setattr__(self, 'updated_at', datetime.now())
        object.__setattr__(self, key, value)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        return {
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
