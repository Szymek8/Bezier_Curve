import matplotlib.pyplot as plt
import numpy as np


def bezier_curve(points, t):
    if len(points) == 1:
        return points[0]
    else:
        return (1 - t) * np.array(bezier_curve(points[:-1], t)) + t * np.array(bezier_curve(points[1:], t))


points = [
    # Litera S
    [(4, 0.5), (4, 0.5), (6.2, 0), (6, 2)],
    [(6, 2), (5.8, 3.84), (4.2, 2.9), (4.4, 4)],
    [(4.4, 4), (4.3, 5.9), (5.6, 4.7), (6, 5.4)],
    [(6, 5.4), (6, 6.5), (4, 6.3), (4, 4.5)],
    [(4, 4.5), (3.8, 2.2), (5, 2.5), (5.6, 2)],
    [(5.6, 2), (5.6, 1), (3.5, 2), (4, 0.5)],

    # Litera Ł
    [(7, 0.5), (7, 2), (7, 5), (7, 6.2)],
    [(7, 6.2), (7.5, 6.2)],
    [(7.5, 6.2), (7.5, 3), (7.5, 1.5)],
    [(7.5, 1.5), (8.7, 1.5)],
    [(8.7, 1.5), (8.7, 0.5)],
    [(8.7, 0.5), (7, 0.5)],
    [(8, 5), (6.5, 3)],
    [(6.5, 3), (6.8, 2.5)],
    [(6.8, 2.5), (8.3, 4.5)],
    [(8.3, 4.5), (8, 5)]

]

t_values = np.linspace(0, 1)

plt.figure(figsize=(6, 4))

for point_set in points:
    curve_points = [bezier_curve(point_set, t) for t in t_values]
    plt.plot(*zip(*curve_points), color='blue')
    plt.scatter(*zip(*point_set), color='red')

plt.title("Inicjały z Krzywych Bezier")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
