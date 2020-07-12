import numpy as np
import matplotlib.pyplot as plt

# make locations(route)


def createcity(num=10):
    POINT = num
    np.random.seed(seed=80)
    point = np.random.rand(POINT, 2) * 100

    return point


# make a matrix of all distances between locations

def distance(point):
    r, _ = point.shape
    d1 = np.zeros((r + 1, r + 1))
    d2 = d1.copy()
    d1[1:, 0] = point[:, 0]
    d1[0, 1:] = point[:, 0].T
    d2[1:, 0] = point[:, 1]
    d2[0, 1:] = point[:, 1].T
    for i in range(r):
        i += 1
        for j in range(r):
            j += 1
            d1[i, j] = (d1[i, 0] - d1[0, j]) ** 2
            d2[i, j] = (d2[i, 0] - d2[0, j]) ** 2
    dis = np.sqrt(d1[1:, 1:] + d2[1:, 1:])
    return dis


if __name__ == '__main__':

    point = createcity(10)
    dis = distance(point)
    print(point[:, 0])
    print(dis[0, :])
