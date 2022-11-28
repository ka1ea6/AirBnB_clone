#!/usr/bin/env python3
'''Module defining the file storage class'''

import json
from datetime import datetime
from ..amenity import Amenity
from ..base_model import BaseModel
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State
from ..user import User


class FileStorage:
    '''Class for serialization and deserialization of instances to JSON'''

    __file_path = 'file.json'
    __objects = {}

    def __init__(self, *args, **kwargs):
        pass

    def all(self):
        '''Public instance method to return a list of all objects in memory'''
        return FileStorage.__objects

    def new(self, obj):
        # new_obj = {**obj}
        class_name = obj.__class__.__name__
        FileStorage.__objects[f'{class_name}.{obj.id}'] = obj

    def update(self, obj_id, attr_key, attr_value):
        try:
            attr_value = self.__clean_quotes(attr_value)
            if attr_key not in ["id", "created_at", "updated_at"]:
                self.__objects[f'{obj_id}'].__dict__[
                    f'{attr_key}'] = attr_value
                self.save()
                return True
            else:
                return False
        except KeyError:
            return False

    def __clean_quotes(self, to_clean):
        clean_attr_value = to_clean.split("\"")
        if len(clean_attr_value) > 1:
            return clean_attr_value[1]
        else:
            return clean_attr_value[0]

    def remove(self, obj_id):
        '''Public instance method to delete a
         certain element from the dictionary'''
        try:
            del self.__objects[f'{obj_id}']
            self.save()
            return True
        except KeyError:
            return False

    def save(self):
        currObjs = FileStorage.__objects
        objDict = {obj: currObjs[obj].to_dict() for obj in currObjs.keys()}
        fileName = FileStorage.__file_path
        with open(f'{fileName}', 'w', encoding='utf8') as file_db:
            json.dump(objDict, file_db)

    def reload(self):
        try:
            with open(f'{FileStorage.__file_path}', 'r') as file_db:
                reload_objs = json.load(file_db)
                for obj in reload_objs.values():
                    cls_name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
