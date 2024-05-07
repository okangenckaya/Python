# How to create calculator of a Circle's area and perimeter by OOP ?

class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def calculating_area(self, r: float):
        return self.pi * r ** 2

    def calculating_perimeter(self, r: float):
        return self.pi * 2 * r


r = float(input('Radius: '))
result = Circle(r)

print(f"""
Area: {result.calculating_area(r)}
Perimeter {result.calculating_perimeter(r)}
""")
