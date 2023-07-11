#!/usr/bin/python3


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
from models import storage

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

    def save(self):
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def delete(self):
        storage.delete(self)

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        if '_sa_instance_state' in dict_copy:
            del dict_copy['_sa_instance_state']
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = type(self).__name__
        return dict_copy
