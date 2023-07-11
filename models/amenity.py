#!/usr/bin/python3

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

