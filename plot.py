import numpy as np
import matplotlib.pyplot as plt
from distance import createcity, distance
from route import calc


def plot_route(order, point):
    dis = distance(point)
    orders, dist = calc(order, dis)
    x = point[orders[0], 0]
    y = point[orders[1], 1]

    print('original order: {}'.format(point))
    print('sorted order: {}'.format(orders[0]))
    print('distance: {}'.format(dist))

    fig = plt.figure(figsize=(10, 5))
    origin = fig.add_subplot(121)
    ordered = fig.add_subplot(122)
    origin.plot(point[:, 0], point[:, 1], marker='o', ls='-')
    ordered.plot(x, y, color='b', marker='o', ls='-')
    plt.show()


if __name__ == '__main__':

    point = createcity(20)
    order = list(np.random.permutation(20))  # change here
    plot_route(order, point)
