#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table(
        'place_amenity', Base.metadata,
        Column(
            'place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
        Column(
            'amenity_id', String(60), ForeignKey('amenities.id'),
            primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """
    Place Class
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenities = relationship(
            'Amenity', secondary=place_amenity, viewonly=False)
    reviews = relationship(
            "Review", backref="place", cascade="all, delete-orphan")

    @property
    def reviews(self):
        """
        Getter attribute for reviews in FileStorage
        Returns a list of Review instances with
        place_id equal to the current Place.id
        """
        from models import storage
        review_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
