from IAnimalClass import IAnimal

class lions(IAnimal):
    """Concrete Product A"""

    @property
    def objType(self) -> str:
        return "lions sound like "
    
    @property
    def say(self) -> str:
        return "Roaring"