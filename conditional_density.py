def f(x_prime, x, j, N):
    if x < N and j == 1 and x_prime == x + 1:
        prob = 1
    elif x == N and j == 1 and x_prime == 0:
        prob = 1
    elif x <= N and j == 0 and x_prime == x:
        prob = 1
    else:
        prob = 0
    return prob