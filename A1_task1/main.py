from abc import ABC, abstractmethod
from typing import Type #Type is used for type hints when a variable represents a class itself, rather than an instance of that class.
from ClientClass import client

p1=client()

zoo=p1.selectZoo('toronto')
print(zoo.get_itinerary())
zoo.show_animals()

p2=client()
zoo=p2.selectZoo('calgary')
print(zoo.get_itinerary())
zoo.show_animals()
