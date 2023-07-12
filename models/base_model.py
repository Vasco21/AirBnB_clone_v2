#!/usr/bin/python3

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        now = datetime.utcnow()
        if 'created_at' not in kwargs:
            self.created_at = now
        if 'updated_at' not in kwargs:
            self.updated_at = now

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def to_dict(self):
        data = self.__dict__.copy()
        data.pop('_sa_instance_state', None)
        data['created_at'] = data['created_at'].isoformat()
        data['updated_at'] = data['updated_at'].isoformat()
        data['__class__'] = self.__class__.__name__
        return data
