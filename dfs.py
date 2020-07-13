import numpy as np
import matplotlib.pyplot as plt
from route import calc
from distance import createcity, distance
from plot import plot_route
import time

best_route = [] * 5
best_s = 10000000


def dfs_best(init_order, dis, tf, route, num):
    global best_route
    global best_s
    global count
    if num == len(init_order):
        count = 0
        init = init_order[0]
        route.append(init)
        count += 1
        tf[0] = False
        l = len(init_order)
        num -= 1
        _ = dfs_best(init_order, dis, tf, route, num)

        return list(best_route[0, :l]), count
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
                count += 1
                tf[i] = False
                num -= 1
                _ = dfs_best(init_order, dis, tf, route, num)
                route.pop()
                num += 1
                tf[i] = True


if __name__ == '__main__':
    point = createcity(8)
    dis = distance(point)
    test_order = list(np.random.permutation(8))
    tf = [True] * len(test_order)
    route = []
    start = time.time()
    best_route, count = dfs_best(test_order, dis, tf, route, len(test_order))
    end = time.time()
    print(end - start, "秒")
    print(count, "計算回数")
    plot_route(test_order, best_route, point)
