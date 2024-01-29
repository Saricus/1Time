# inicjalizer
# - specjalana metoda ktora pozwala zainicjalizowac obiekt nowej instacji
# - jest uruchamiana automatycznie w momencie tworzenia nowej instacji
# - uzywamy jej w celu ustawienia poczontkowego stanu instacji (poczatkowej wartosci atrybutow)

# self
# referencja do instancji
# mozna np. odwolac sie do atrybutu danej instancji

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Point(3, 5)
print(p1.x, p1.y)