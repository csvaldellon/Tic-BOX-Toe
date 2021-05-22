import numpy as np
import time
import random
from numba import njit,cuda

@njit
def monte_carlo_pi_jit(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc +=1
    return 4.0*acc / nsamples


# start_time = time.time()
# monte_carlo_pi(10**9)
# print(time.time()-start_time)

# monte_carlo_pi_jit = njit()(monte_carlo_pi)
start_time_2 = time.time()
monte_carlo_pi_jit(10**9)
print(time.time()-start_time_2)
