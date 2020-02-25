class Kruh:

    def __radd__(self, other):
        return Kruh(self.polomer + other)

    def __mul__(self, other):
        return Kruh(self.polomer * other.polomer)

    def __add__(self, other):
        if isinstance(other,Kruh):
            return Kruh(self.polomer+other.polomer)
        else:
            return Kruh(self.polomer + other)

    def __sub__(self, other):
        return Kruh(self.polomer-other.polomer)

    def __truediv__(self, other):
        return Kruh(self.polomer/other.polomer)

    def __eq__(self, other):
        return self.polomer==other.polomer

    def __lt__(self, other):
        return self.polomer<other.polomer

    def __init__(self, _polomer):
        self.polomer = _polomer
        self.farba= None

    def __str__(self):
        return "Kruh ma polomer {}".format(self.polomer)

    def obsah(self):
        return 3.14 * self.polomer * self.polomer

    @property
    def polomer(self):
        return self.__polomer

    @polomer.setter
    def polomer(self,polomer):
        assert polomer>0,"Polomer je zly"
        self.__polomer=polomer


Prvy = Kruh(-10)
Druhy = Kruh(10)
# Treti = Prvy + Druhy
# print(Prvy.obsah())
# print(Prvy)
# if Prvy==Druhy:
#     print("Rovnaju sa")
# else:
#     print("Newrovnaju sa")
#
# if Prvy<Druhy:
#     print("Je mensi")
# else:
#     print("Je vacsi")
#
# print(Treti)
# print(Prvy-Druhy)
# print(Prvy/Druhy)
# print(Prvy*Druhy)
# print(Prvy+2)
# print(3+Prvy)
