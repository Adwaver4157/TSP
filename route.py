import numpy as np
from distance import createcity, distance


def calc(order, distance):
    l = len(order)
    orders = np.zeros((2, l + 1), dtype=np.uint8)
    orders[0, :l] = order
    orders[0, l] = order[0]
    orders[1, :l - 1] = order[1:]
    orders[1, l - 1:l + 1] = order[0:2]
    sum = 0
    for i in range(l):
        sum += distance[orders[0][i]][orders[1][i]]

    return orders, sum


if __name__ == '__main__':

    point = createcity(10)
    dis = distance(point)
    order = list(np.random.permutation(10))
    orders, dist = calc(order, dis)
    print(orders)
    print(dist)
