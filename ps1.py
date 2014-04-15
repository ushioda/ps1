import numpy
from period_utility import util
from conditional_density import f

beta = 0.98
N = 10
delta = 5 
r = 2
threshold = 0.001
epsilon_draw = 1000

w_next = numpy.empty(N + 1)
w = numpy.ones(N + 1) # initial value
distance = 1


while distance > threshold: # loop until convergence

    for x in range(N + 1): # calculate for each state
    
        val = numpy.empty(epsilon_draw) # values for different epsilon draws
        epsilon = numpy.random.gumbel(0, 1, epsilon_draw) # Random Type 1 Extreme Values
        
        for i in range(epsilon_draw): # Monte Carlo simulation
            
            choice_specific_val = numpy.empty(2)
            for j in [0,1]: # calculate choice specific value for each action
                cont_val = beta * sum(w[x_prime] * f(x_prime, x, j, N) for x_prime in range(N))
                choice_specific_val[j] = util(x, j, delta, N, r) + epsilon[i] + cont_val
            val[i] = choice_specific_val.max()
            
        w_next[x] = val.mean() # Take average of values for each epsilon draw (MonteCarlo)
        
    distance = numpy.linalg.norm(w_next - w) # calculate distance between w(n+1) and w(n)
    w = w_next # move on to the next step
    
print w