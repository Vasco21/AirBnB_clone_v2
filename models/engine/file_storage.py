#!/usr/bin/python3

def delete(self, obj=None):
    """
    Delete an object from the storage.

    Args:
        obj (BaseModel): The object to be deleted.

    Returns:
        None
    """
    if obj is None:
        return

    key = "{}.{}".format(type(obj).__name__, obj.id)
    if key in self.__objects:
        del self.__objects[key]
        self.save()
