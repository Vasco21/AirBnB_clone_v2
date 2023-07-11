#!/usr/bin/python3

class FileStorage:
def delete(self, obj=None):
    """Deletes obj from __objects"""

    if obj is None:
        return

    key = obj.__class__.__name__ + '.' + obj.id
    if key in self.__objects:
        del self.__objects[key]
        self.save()

def all(self, cls=None):
    """Returns a dictionary of objects of a specific class"""
    if cls is None:
        return self.__objects

    filtered_objects = {}
    for key, obj in self.__objects.items():
        if type(obj) is cls:
            filtered_objects[key] = obj
    return filtered_objects
