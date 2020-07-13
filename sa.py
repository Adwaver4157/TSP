import numpy as np
import matplotlib.pyplot as plt
from route import calc
from distance import createcity, distance
from plot import plot_route
import time
import math


def calc_cost(route, i, j, dist):
    l = len(route)
    a, b = route[i], route[(i + 1) % l]
    c, d = route[j], route[(j + 1) % l]

    before = dist[a, b] + dist[c, d]
    after = dist[a, c] + dist[b, d]

    return after - before


def swap(route, i, j):
    tmp = route[i + 1: j + 1]
    tmp.reverse()
    route[i + 1: j + 1] = tmp
    return route


def sa_2opt(route, dist, t=10000, a=0.99):
    global count
    count = 0
    _route = route.copy()
    l = len(_route)
    while t > 0.0001:
        for i in range(0, l - 2):
            for j in range(i + 2, l):
                if i == 0 and j == l - 1:
                    continue

                cost_diff = calc_cost(_route, i, j, dist)
                count += 1

                if cost_diff < 0:
                    _route = swap(_route, i, j)
                else:
                    prob = pow(math.e, -cost_diff / t)
                    np.random.seed()
                    if np.random.rand() < prob:
                        _route = swap(_route, i, j)
                    t = t * a

    return _route, count


if __name__ == '__main__':
    point = createcity(12)
    dist = distance(point)
    test_order = list(np.random.permutation(12))
    t = 100000
    a = 0.999
    start = time.time()
    best_route, count = sa_2opt(test_order, dist, t, a)
    end = time.time()
    print(end - start, "秒")
    print(count, "計算回数")
    plot_route(test_order, best_route, point)
