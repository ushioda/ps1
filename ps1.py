import numpy
from pylab import plot, show, legend

beta = 0.98 # discount factor 
N = 10 # max number of reward points
delta = 5 # consumption utility from each purchase
r = 2 # value of reward
threshold = 0.001 # threshold for convergence
epsilon_draw = 100 # number of epsilon draws for MC simulation




###############################
#          Problem 2          #
###############################

from choice_specific_val import vj

v = vj(beta, N, delta, r, threshold, epsilon_draw)
print v




###############################
#          Problem 4          #
###############################

######## baseline case, beta = 0.98 ########


## baseline case, delta = 5

c = numpy.empty(N + 1)

for x in range(N + 1):
    c[x] = (v[x,1] - v[x,0]) - (v[0,1] - v[0,0])
    
    
## low type case, delta = 1

delta_low = 1
v_low = vj(beta, N, delta_low, r, threshold, epsilon_draw)

c_low = numpy.empty(N + 1)

for x in range(N + 1):
    c_low[x] = (v_low[x,1] - v_low[x,0]) - (v_low[0,1] - v_low[0,0])


## high type case, delta = 20

delta_high = 20
v_high = vj(beta, N, delta_high, r, threshold, epsilon_draw)

c_high = numpy.empty(N + 1)

for x in range(N + 1):
    c_high[x] = (v_high[x,1] - v_high[x,0]) - (v_high[0,1] - v_high[0,0])
    

## plot different types of c

plot(c, label = 'delta = 5')
plot(c_low, label = 'delta = 1')
plot(c_high, label = 'delta = 20')
legend(loc='upper left')
show()



######## low discount factor case, beta = 0.6 ########

beta = 0.6

## baseline case, delta = 5

c = numpy.empty(N + 1)

for x in range(N + 1):
    c[x] = (v[x,1] - v[x,0]) - (v[0,1] - v[0,0])
    
    
## low type case, delta = 1

delta_low = 1
v_low = vj(beta, N, delta_low, r, threshold, epsilon_draw)

c_low = numpy.empty(N + 1)

for x in range(N + 1):
    c_low[x] = (v_low[x,1] - v_low[x,0]) - (v_low[0,1] - v_low[0,0])


## high type case, delta = 20

delta_high = 20
v_high = vj(beta, N, delta_high, r, threshold, epsilon_draw)

c_high = numpy.empty(N + 1)

for x in range(N + 1):
    c_high[x] = (v_high[x,1] - v_high[x,0]) - (v_high[0,1] - v_high[0,0])
    

## plot different types of c

plot(c, label = 'delta = 5')
plot(c_low, label = 'delta = 1')
plot(c_high, label = 'delta = 20')
legend(loc='upper left')
show()




###############################
#          Problem 5          #
###############################

