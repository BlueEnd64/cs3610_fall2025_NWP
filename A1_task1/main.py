from abc import ABC, abstractmethod
from typing import Type #Type is used for type hints when a variable represents a class itself, rather than an instance of that class.

# 1. Product Interface
class IAnimal(ABC):
    """Abstract Product Interface"""

    @property
    @abstractmethod
    def objType(self) -> str:
        pass
    
    @property
    def say(self) -> str:
        pass


# 2. Concrete Products
class lions(IAnimal):
    """Concrete Product A"""

    @property
    def objType(self) -> str:
        return "I am Class A"
    
    @property
    def say(self) -> str:
        return "Roaring"


class elephants(IAnimal):
    """Concrete Product B"""

    @property
    def objType(self) -> str:
        return "I am Class B"
    
    @property
    def say(self) -> str:
        return "trumpet"



myObjs: dict[str, Type[IAnimal]] = {
    'a': lions,
    'b': elephants
}

class Creator:
    '''The Factory Method Class'''

    @staticmethod
    def create_Animal(objType: str) ->IAnimal: #A static method to get a concrete product
        try:
            if objType in myObjs.keys():
                return myObjs[objType]()
            else:
                raise Exception("I can't make this object")
        except Exception as _e:
            print(_e)
        return None


# The Client
objNames=['a','b','c']

for name in objNames:
    res=Creator.create_Animal(name)
    if res:
        print(res.say) # outputs the entered property

