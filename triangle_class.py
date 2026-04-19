from triangle_func import IncorrectTriangleSides
class Triangle:
    
    def __init__(self, side1, side2, side3):

        if not all(isinstance(s, (int, float)) for s in (side1, side2, side3)):
            raise IncorrectTriangleSides("Все стороны должны быть числами")

        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise IncorrectTriangleSides("Длины сторон должны быть положительными числами")

        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            raise IncorrectTriangleSides("Стороны не удовлетворяют неравенству треугольника")
        
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def triangle_type(self):

        if self.side1 == self.side2 == self.side3:
            return "equilateral"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "isosceles"
        else:
            return "nonequilateral"
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3