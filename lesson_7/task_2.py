from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):

    @property
    def calculation(self):
        return round((self.size / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculation(self):
        return round((2 * self.size) + 0.3)


coat = Coat(60)
suit = Suit(180)
print(coat.calculation)
print(suit.calculation)
