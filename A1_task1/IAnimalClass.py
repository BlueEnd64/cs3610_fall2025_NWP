from abc import ABC, abstractmethod

class IAnimal(ABC):
    """Abstract Product Interface"""

    @property
    @abstractmethod
    def objType(self) -> str:
        pass
    
    @property
    def say(self) -> str:
        pass
    