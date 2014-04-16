import numpy
from period_utility import util
from conditional_density import f

def w(beta, N, delta, r, threshold, epsilon_draw):

    w_next = numpy.empty(N + 1)
    w_now = numpy.ones(N + 1) # initial value
    distance = 1

    while distance > threshold: # loop until convergence

        for x in range(N + 1): # calculate for each state
    
            val = numpy.empty(epsilon_draw) # values for different epsilon draws
            epsilon = numpy.random.gumbel(0, 1, epsilon_draw) # Random Type 1 Extreme Values
        
            for i in range(epsilon_draw): # Monte Carlo simulation
            
                choice_specific_val = numpy.empty(2)
                for j in [0,1]: # calculate choice specific value for each action
                    cont_val = beta * sum(w_now[x_prime] * f(x_prime, x, j, N) for x_prime in range(N + 1))
                    choice_specific_val[j] = util(x, j, delta, N, r) + epsilon[i] + cont_val
                    val[i] = choice_specific_val.max()
            
            w_next[x] = val.mean() # Take average of values for each epsilon
        
        distance = numpy.linalg.norm(w_next - w_now) # calculate distance between w(n+1) and w(n)
        w_now = w_next # move on to the next step
        
    return w_now