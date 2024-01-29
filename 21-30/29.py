# klasy dziedziczonce
# zachowanie podobne do klasy istniejcej
# dziedziczy z klasy podstawowej ale moze miec swoje dodatkowe
class Widget:
    def __init__(self, label):
        self.label = label

#w = Widget('My widget')
#print(w.label)
class Button(Widget):   # dziedziczy z widget ( ma dostemp do wszystkiego)
    def __init__(self, label, size):
        super().__init__(label) # super pozwala odwołać się do bazowej klasy ( u mnie widget)
        self.size = size # ale musze przypisac nowy atrybut

    def hande_click(self):
        return 'click'
    # klasa bazowa nie ma dostepu do tego co jest w klasach dziedziczoncych 

b = Button('kappa', 'large')

print(b.label, b.size)

print(b.hande_click())

w = Widget('leolo')
# w.hande_click() nie mozna 