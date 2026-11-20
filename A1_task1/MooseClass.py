from IAnimalClass import IAnimal

class moose(IAnimal):
    """Concrete Product B"""

    @property
    def objType(self) -> str:
        return "moose sound like "
    
    @property
    def say(self) -> str:
        return "bellow(what sound does a moose make?)"