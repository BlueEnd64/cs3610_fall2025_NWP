from abc import ABC, abstractmethod

class IProduct():
    
    @staticmethod
    @abstractmethod
    def get_Price() -> int:
        pass
    
    @staticmethod
    @abstractmethod
    def get_Description() -> str:
        pass