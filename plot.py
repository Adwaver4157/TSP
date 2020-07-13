import numpy as np
import matplotlib.pyplot as plt
from distance import createcity, distance
from route import calc


def plot_route(test_order, order, point):
    dis = distance(point)
    test_order, _ = calc(test_order, dis)
    orders, dist = calc(order, dis)
    x0 = point[test_order[0], 0]
    y0 = point[test_order[0], 1]
    x = point[orders[0], 0]
    y = point[orders[0], 1]

    print('original order: {}'.format(test_order[0]))
    print('sorted order: {}'.format(orders[0]))
    print('distance: {}'.format(dist))

    fig = plt.figure(figsize=(10, 5))
    origin = fig.add_subplot(121)
    ordered = fig.add_subplot(122)
    origin.plot(x0, y0, marker='o', ls='-')
    ordered.plot(x, y, color='b', marker='o', ls='-')
    plt.show()


if __name__ == '__main__':

    point = createcity(20)
    order = list(np.random.permutation(20))  # change here
    plot_route(order, point)
