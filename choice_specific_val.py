import numpy
from period_utility import util
from conditional_density import f
from emax import w

def vj(beta, N, delta, r, threshold, epsilon_draw):

    v = numpy.empty(2 * (N + 1))
    v.shape = (N + 1, 2)

    for j in range(2): # calculate choice specific value for each action
        for x in range(N + 1): # calculate for each state
            emax_w = w(beta, N, delta, r, threshold, epsilon_draw) # emax function
            cont_val = beta * sum(emax_w[x_prime] * f(x_prime, x, j, N) for x_prime in range(N + 1))
            v[x,j] = util(x, j, delta, N, r) + cont_val

    return v