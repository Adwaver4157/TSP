import numpy as np
import matplotlib.pyplot as plt
from route import calc
from distance import createcity, distance
from plot import plot_route
import time
from dfs import dfs_best
from sa import calc_cost, swap, sa_2opt


def tru(route, best_route):
    flag = False
    if route == best_route:
        flag = True
    else:
        tmp = route[1:]
        tmp.reverse()
        route[1:] = tmp
        if route == best_route:
            flag = True
    return flag


if __name__ == '__main__':
    wh = input('dfs or sa ? : ')
    epoch = int(input('how many do u want to run it ? : '))
    point = createcity(500)
    dis = distance(point)
    test_order = list(np.random.permutation(500))
    if wh == 'dfs':
        T = np.arange(epoch, dtype=np.float64)
        count = np.arange(epoch)
        for i in range(epoch):
            tf = [True] * len(test_order)
            route = []
            start = time.time()
            best_route, _count = dfs_best(test_order, dis, tf, route, len(test_order))
            end = time.time()
            T[i] = end - start
            print(T[i])
            count[i] = _count
        print("mean time: {:.5f}".format(T.mean()))
        print("mean kaisuu: {}".format(count.mean()))
    elif wh == 'sa':
        T = np.arange(epoch, dtype=np.float64)
        count = np.arange(epoch)
        tf = [True] * len(test_order)
        route = []
        if len(test_order) == 10:
            best_route, _count = dfs_best(test_order, dis, tf, route, len(test_order))
        t = 1000
        a = 0.999
        truth = 0
        for i in range(epoch):
            start = time.time()
            best_route_, _count = sa_2opt(test_order, dis, t, a)
            end = time.time()
            T[i] = end - start
            print(T[i])
            count[i] = _count
            if len(test_order) == 10:
                if tru(best_route_, best_route):
                    truth += 1
        if len(test_order) == 10:
            print("precision: {:.4f}".format(truth / epoch))
        print("mean time: {:.5f}".format(T.mean()))
        print("mean kaisuu: {}".format(count.mean()))

    plot_route(test_order, best_route_, point)
