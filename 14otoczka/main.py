import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def orientation(p, q, r):
    return (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x)


def low_left_point(points):
    idx = 0
    for i in range(len(points)):
        if points[i].x < points[idx].x:
            idx = i
        elif points[i].x == points[idx].x:
            if points[i].y < points[idx].y:
                idx = i
    return idx


def jarvis(points):
    start_idx = low_left_point(points)
    p = start_idx
    otoczka = []
    while True:
        otoczka.append(points[p])
        if p == len(points) - 1:
            q = 0
        else:
            q = p + 1
        for r in range(len(points)):
            if orientation(points[p], points[q], points[r]) > 0:
                q = r
        p = q
        if p == start_idx:
            break
    return otoczka


def distance(point1, point2):
    return np.sqrt((point2.x - point1.x)**2 + (point2.y - point1.y)**2)


def jarvis_improved(points):
    start_idx = low_left_point(points)
    p = start_idx
    otoczka = []
    while True:
        otoczka.append(points[p])
        if p == len(points) - 1:
            q = 0
        else:
            q = p + 1
        for r in range(len(points)):
            if orientation(points[p], points[q], points[r]) > 0:
                q = r
            elif orientation(points[p], points[r], points[q]) == 0:
                pq_distance = distance(points[p], points[q])
                pr_distance = distance(points[p], points[r])
                qr_distance = distance(points[q], points[r])
                if pr_distance >= pq_distance and pr_distance >= qr_distance:
                    q = r
        p = q
        if p == start_idx:
            break
    return otoczka


if __name__ == '__main__':
    punkty1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    punkty2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    points1 = [Point(point[0], point[1]) for point in punkty1]
    points2 = [Point(point[0], point[1]) for point in punkty2]
    print(jarvis(points1))
    print(jarvis(points2))
    print()

    print(jarvis_improved(points1))
    print(jarvis_improved(points2))
    print()

    punkty = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    points = [Point(point[0], point[1]) for point in punkty]
    print(jarvis(points))
    print(jarvis_improved(points))
