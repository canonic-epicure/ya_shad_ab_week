import random
import numpy as np


k = 100000


A_prob = 1 / 6
B_prob = 1 / 6 + 1 / 3

def model():
    step = 0
    str = ''

    while str[-3:] != 'abt':
        x = random.random()

        if x < A_prob:
            str += 'a'
        elif x < B_prob:
            str += 'b'
        else:
            str += 't'

        step += 1

    return step

tests = [ model() for i in range(k) ]

uniques, counts = np.unique(tests, return_counts=True)

probs = counts / k

print((uniques * probs).sum())
