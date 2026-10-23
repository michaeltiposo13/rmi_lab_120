from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def getPrice(self):
        pass