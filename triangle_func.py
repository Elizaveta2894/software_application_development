class IncorrectTriangleSides(Exception):
    pass

def get_triangle_type(side1, side2, side3):
    if not all(isinstance(s, (int, float)) for s in (side1, side2, side3)):
        raise IncorrectTriangleSides("Все стороны должны быть числами")
    
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise IncorrectTriangleSides("Длины сторон должны быть положительными числами")
    if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
        raise IncorrectTriangleSides("Стороны не удовлетворяют неравенству треугольника")

    if side1 == side2 == side3:
        return "equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"
    else:
        return "nonequilateral"