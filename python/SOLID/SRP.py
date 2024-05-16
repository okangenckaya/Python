"""
S- Single Responsibility Principle

A class or object must have one reason or be changed for one aim. In fact, every class should have a single
responsibility or single target. Every class must be only used for one target. Besides, we don't fall into
the coding repeat. Modifying the class for many reasons indicates something is missing and should be fixed.
Let's give an example for SRP:

"""


class Rectangle:
    def __init__(self, short_edge, long_edge):
        self.short_edge = short_edge
        self.long_edge = long_edge

    @staticmethod
    def area_calculator(long_edge: int, short_edge: int) -> int:
        return long_edge * short_edge

    @staticmethod
    def perimeter_calculator(long_edge: int, short_edge: int) -> int:
        return (long_edge * 2) + (short_edge * 2)


"""
According to SPR, every class or object must have a single responsibility or aim. When we take a look at 
Rectangle class, its responsibility should be limited to its attributes, without including calculation functions. 
We should create class for every calculation process.

"""


class Rectangle:
    def __init__(self, short_edge, long_edge):
        self.short_edge = short_edge
        self.long_edge = long_edge


class AreaCalculator:
    @staticmethod
    def area_calculator(edge: Rectangle) -> int:
        return edge.long_edge * edge.long_edge


class PerimeterCalculator:
    @staticmethod
    def perimeter_calculator(edge: Rectangle) -> int:
        return (edge.long_edge * 2) + (edge.short_edge * 2)


"""
According to new model, every class has own responsibility when they have own classes. So, this model represents more
clear, readable, and  flexible code. 

"""