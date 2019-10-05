class Wes:
    latinrep = ""
    indx = -1
    def __init__(self, latinrep, indx):
        self.latinrep = latinrep
        self.indx = indx
    def __str__(self):
        return f"Wes({self.latinrep}, {self.indx})"
    def __repr__(self):
        return self.__str__()
    def __lt__(self, other):
        return self.indx < other.indx
    def __le__(self, other):
        return self.indx <= other.indx
    def __eq__(self, other):
        return self.indx == other.indx
    def __ne__(self, other):
        return self.indx != other.indx
    def __ge__(self, other):
        return self.indx >= other.indx
    def __gt__(self, other):
        return self.indx > other.indx
