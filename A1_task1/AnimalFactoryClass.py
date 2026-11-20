from IAnimalClass import IAnimal
from LionsClass import lions
from ElephantsClass import elephants
from PenguinsClass import penguins
from WhiteBearsClass import whiteBears
from GrizzlyBearsClass import grizzlyBears
from MooseClass import moose

from typing import Type


myObjs: dict[str, Type[IAnimal]] = {
    'lions': lions,
    'elephants': elephants,
    'penguins': penguins,
    'white bears': whiteBears,
    'grizzly bears': grizzlyBears,
    'moose': moose
}

class AnimalFactory:
    '''The Factory Method Class'''

    @staticmethod
    def create_Animal(objType: str) ->IAnimal: #A static method to get a concrete product
        try:
            # print(objType)
            if objType in myObjs.keys():
                
                return myObjs[objType]()
            else:
                raise Exception("I can't make this object")
        except Exception as _e:
            print(_e)
        return None