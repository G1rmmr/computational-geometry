import math

class ConvexHull:
    def __init__(self, points: tuple[int, int]) -> None:
        self.points = points
        self.hull = []

    def polar(self, p0: tuple[int, int], p1: tuple[int, int]) -> float:
        y_span = p1[1] - p0[1]
        x_span = p1[0] - p0[0]
        return math.atan2(y_span, x_span)
    
    def distance(self, p0: tuple[int, int], p1: tuple[int, int]) -> float:
        return math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)

    def graham_scan(self) -> None:
        self.hull.clear()

        start = min(self.points, key=lambda p: (p[1], p[0]))
        self.points.pop(self.points.index(start))

        points = sorted(self.points, 
            key=lambda p: (self.polar(start, p), self.distance(start, p)))
        
        self.hull = [start, points[0]]

        for point in points[1:]:
            while len(self.hull) > 1:
                p0 = self.hull[-2]
                p1 = self.hull[-1]
                p2 = point

                crs = (p1[0] - p0[0]) * (p2[1] - p0[1]) 
                crs -= (p1[1] - p0[1]) * (p2[0] - p0[0])

                if crs > 0:
                    break
                else:
                    self.hull.pop()

            self.hull.append(point)
        self.hull.append(start)

    def javis_march(self) -> None:
        self.hull.clear()

        start = min(self.points)
        p0 = start

        while True:
            self.hull.append(p0)
            p1 = self.points[0]

            for p2 in self.points[1:]:
                if p0 == p1:
                    p1 = p2
                    continue

                crs = (p1[0] - p0[0]) * (p2[1] - p0[1]) 
                crs -= (p1[1] - p0[1]) * (p2[0] - p0[0])

                if crs < 0:
                    p1 = p2

            p0 = p1
            if p0 == start:
                break

        self.hull.append(start)



import sys
import random

from Simulation import Simulation

if __name__ == "__main__":
    points = []

    for _ in range(10):
        x = random.randint(100, 700)
        y = random.randint(100, 500)
        points.append((x, y))

    convex_hull = ConvexHull(points)
    convex_hull.javis_march()

    simul = Simulation("Spline", convex_hull.hull)

    try:
        simul.run()
        
    except Exception as e:
        print(f"Error: {e}")

    finally:
        sys.exit()