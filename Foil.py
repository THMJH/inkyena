class Foil:
    latinrep = ""
    weslis = []
    def __init__(self, latinrep, weslis):
        self.latinrep = latinrep
        self.weslis = weslis
    def __init__(self, latinrep):
        self.latinrep = latinrep
        self.weslis = parseFoil(latinrep)
    def __str__(self):
        return f"Foil({self.latinrep}, {self.weslis})"
    def __repr__(self):
        return self.__str__()
    def __lt__(self, other):
        return self.weslis < other.weslis
    def __le__(self, other):
        return self.weslis <= other.weslis
    def __eq__(self, other):
        return self.weslis == other.weslis
    def __ne__(self, other):
        return self.weslis != other.weslis
    def __ge__(self, other):
        return self.weslis >= other.weslis
    def __gt__(self, other):
        return self.weslis > other.weslis
