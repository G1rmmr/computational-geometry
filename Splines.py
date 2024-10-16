import math

# 0: bernstein polynomial / 1: de_casteljau algorithm
TYPE = 1

class Bezier:
    def __init__(self, points: tuple[int, int]) -> None:
        self.points = points
        self.curve_points = []
        self.degree = 3

    def generate(self) -> None:
        self.curve_points.clear()

        for i in range(0, 100):
            t = 0.01 * i
            point = self.bernstein(t) if TYPE == 0 else self.de_casteljau(t)
            self.curve_points.append(point)

    def bernstein(self, t: float) -> tuple[float, float]:
        x, y = 0, 0

        for i, (px, py) in enumerate(self.points):
            bin = math.comb(self.degree, i)
            bernstein_coeff = bin * ((1 - t) ** (self.degree - i)) * t ** i
            x += bernstein_coeff * px
            y += bernstein_coeff * py

        return (x, y)

    def de_casteljau(self, t: float) -> tuple[float, float]:
        temp_points = self.points.copy()

        for i in range(1, self.degree):
            for j in range(self.degree - i):
                x = (1 - t) * temp_points[j][0] + t * temp_points[j + 1][0]
                y = (1 - t) * temp_points[j][1] + t * temp_points[j + 1][1]
                temp_points[j] = (x, y)

        return temp_points[0]
    
import sys

from Simulation import Simulation

if __name__ == "__main__":
    points = [
        (100, 150),
        (200, 100),
        (300, 300),
        (400, 200)
    ]

    bezier = Bezier(points)
    bezier.generate()

    simul: Simulation = Simulation("Spline", bezier.curve_points)

    try:
        simul.run()
        
    except Exception as e:
        print(f"Error: {e}")

    finally:
        sys.exit()