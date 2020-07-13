import numpy as np
import matplotlib.pyplot as plt
from route import calc
from distance import createcity, distance
from plot import plot_route
import time
from dfs import dfs_best
from sa import calc_cost, swap, sa_2opt


if __name__ == '__main__':
    wh = input('dfs or sa ? : ')
    epoch = int(input('how many do u want to run it ? : '))
    point = createcity(10)
    dis = distance(point)
    test_order = list(np.random.permutation(10))
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
        best_route, _count = dfs_best(test_order, dis, tf, route, len(test_order))
        t = 100000
        a = 0.999
        truth = 0
        for i in range(epoch):
            start = time.time()
            best_route_, _count = sa_2opt(test_order, dis, t, a)
            end = time.time()
            T[i] = end - start
            print(T[i])
            count[i] = _count
            if best_route_ == best_route:
                truth += 1
        print("precision: {:.4f}".format(truth / epoch))
        print("mean time: {:.5f}".format(T.mean()))
        print("mean kaisuu: {}".format(count.mean()))

    plot_route(test_order, best_route, point)
