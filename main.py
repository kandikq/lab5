from enum import Enum
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    # Додайте інші кольори, якщо потрібно


class Polynom:
    def __init__(self, points, color):
        self.points = points
        self.color = color

    def __repr__(self):
        return f"Polynom({self.points}, {self.color})"

    def __str__(self):
        return f"Polynom Color: {self.color.name}, Points: {', '.join(map(str, self.points))}"

    def calculate_distance(self, point1, point2):
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

    def calculate_perimeter(self):
        perimeter = 0
        for i in range(len(self.points) - 1):
            perimeter += self.calculate_distance(self.points[i], self.points[i + 1])
        perimeter += self.calculate_distance(self.points[-1], self.points[0])  # Додатково замкнутий полігон
        return perimeter

    def calculate_longest_diagonal(self):
        max_diagonal = 0
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                diagonal = self.calculate_distance(self.points[i], self.points[j])
                if diagonal > max_diagonal:
                    max_diagonal = diagonal
        return max_diagonal

    def sort_by_x(self):
        self.points.sort(key=lambda point: point.x)

    def sort_by_y(self):
        self.points.sort(key=lambda point: point.y)


def main():
    point1 = Point(1, 2)
    point2 = Point(3, 4)
    point3 = Point(5, 6)

    polynom_points = [point1, point2, point3]
    polynom_color = Color.RED

    polynom = Polynom(polynom_points, polynom_color)

    print("Початковий полігон:")
    print(f"__str__(): {str(polynom)}")
    print(f"__repr__(): {repr(polynom)}")

    print("\nВідсортовано за X:")
    polynom.sort_by_x()
    print(f"__str__(): {str(polynom)}")
    print(f"__repr__(): {repr(polynom)}")

    print("\nВідсортовано за Y:")
    polynom.sort_by_y()
    print(f"__str__(): {str(polynom)}")
    print(f"__repr__(): {repr(polynom)}")

    print(f"\nПериметр: {polynom.calculate_perimeter()}")
    print(f"Найдовша діагональ: {polynom.calculate_longest_diagonal()}")

    print("\nНовий полігон:")
    new_polynom_points = [Point(2, 3), Point(4, 5), Point(6, 7)]
    new_polynom_color = Color.GREEN

    new_polynom = Polynom(new_polynom_points, new_polynom_color)

    print("\nВідсортовано за X:")
    new_polynom.sort_by_x()
    print(f"__str__(): {str(new_polynom)}")
    print(f"__repr__(): {repr(new_polynom)}")

    print("\nВідсортовано за Y:")
    new_polynom.sort_by_y()
    print(f"__str__(): {str(new_polynom)}")
    print(f"__repr__(): {repr(new_polynom)}")

    print(f"\nПериметр нового полігону: {new_polynom.calculate_perimeter()}")
    print(f"Найдовша діагональ нового полігону: {new_polynom.calculate_longest_diagonal()}")


if __name__ == "__main__":
    main()