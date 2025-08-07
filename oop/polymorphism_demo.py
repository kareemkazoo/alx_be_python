import math
class shap:
    def area(self):
        raise NotImplementedError("Subclasses must override area()")
        
class Rectangle(shap):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Circle(shap):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
        