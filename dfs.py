import numpy as np
import matplotlib.pyplot as plt
from route import calc
from distance import createcity, distance
from plot import plot_route

best_route = [] * 5
best_s = 10000000


def dfs_best(init_order, dis, tf, route, num):
    global best_route
    global best_s
    if num == len(init_order):
        init = init_order[0]
        route.append(init)
        tf[0] = False
        l = len(init_order)
        num -= 1
        _ = dfs_best(init_order, dis, tf, route, num)

        return list(best_route[0, :l])
    else:

        if num == 0:
            _route, s = calc(route, dis)
            if best_s > s:
                best_s = s
                best_route = _route
        for i in range(len(init_order)):
            if tf[i] == True:
                init = init_order[i]
                route.append(init)
                tf[i] = False
                num -= 1
                _ = dfs_best(init_order, dis, tf, route, num)
                tf[i] = True


if __name__ == '__main__':
    point = createcity(5)
    dis = distance(point)
    test_order = list(np.random.permutation(5))
    tf = [True] * len(test_order)
    route = []
    best_route = [] * len(test_order)
    best_s = 10000000
    best_route = dfs_best(test_order, dis, tf, route, len(test_order))
    plot_route(test_order, best_route, point)
