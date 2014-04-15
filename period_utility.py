def util(x, j, delta, N, r):
    if j == 0:
        utility = 0
    else:
        utility = delta + r * (x == N)
    return utility