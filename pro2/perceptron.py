# -*- coding: utf-8 -*-
import time
import numpy as np
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self, nodes=3, lr=0.3, init_weights=0):
        self.nodes = nodes
        self.lr = lr
        self.weights = init_weights

    def forward(self, x):
        out = np.dot(self.weighs, x)
        return out

    def train(self, x, y):
        out = self.forward(x)
        flag = False
        if out < 0 and y > 0:
            self.weigths += self.lr * x
            flag = True
        if out > 0 and y < 0:
            self.weigths -= self.lr * x
            flag = True
        return flag

    def pred(self, x, y):
        start = time.time()
        out = self.forward(x)
        end = time.time()
        if (out > 0 and y > 0) or (out < 0 and y < 0):
            result = True
        else:
            result = False
        print('prediction time: {}(sec)'.format(end - start))
        print('the predicted value is {}, it is {}'.format(out, result))


if __name__ == '__main__':
    neuron = Perceptron()
    data = np.array([[2, 3, 1], [4, 3, 0], [2, 6, 1], [4, 1, 0]])
    length = len(data)
    epoch = input('enter epoch num: ')
    loop = 0
    count = 0
    while True:
        epoch -= 1
        loop += 1
        p = data.pop()
        x = p[:len(p) - 1]
        y = p[-1]
        flag = neuron.train(x, y)
        if not flag:
            count += 1
        if loop == length and count == length:
            print('training is successful! training is ending...')
            break
        if epoch == 0:
            break

    plt.plot(data)
    print('finally perceptron\'s weights are as follows:')
    print(neuron.weights)
