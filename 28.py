class Point:
    points_counter = 0 #mozna wykozystac na rzecz instancji lub klasy
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        Point.points_counter += 1
    def move_to_new_coords(self, x=0, y=0): #lepsza zmiana
        self.x = x
        self.y = y

p1 = Point(3, 5)
p2 = Point(3, 5)
#p2.points_counter = 12
#Point.points_counter = 2
# print(p2.points_counter) # dla klasy moze miec inna wartosc
# print(Point.points_counter) # dla instancji moze miec inna wartosc

print(Point.points_counter)
print(p1.points_counter) # dla jednej istancji mozna nadpisac





