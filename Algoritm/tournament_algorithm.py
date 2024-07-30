# Tournament two - to find two largest element of an array -- Limitation it only works when number of elements in array multiple of 2
def tournament_two(A):
    N = len(A)
    winner = [None]*(N-1)
    looser = [None]*(N-1)
    prior =[-1]*(N-1)
    idx = 0
    for i in range(0 , N, 2):
        if A[i] < A[i+1]:
            winner[idx] = A[i+1]
            looser[idx] = A[i]
        else:
            winner[idx] = A[i]
            looser[idx] = A[i+1]
        idx += 1
    m = 0
    while idx < N-1:
        if winner[m] < winner[m+1]:
            winner[idx] = winner[m+1]
            looser[idx] = winner[m]
            prior[idx] = m+1
        else:
            winner[idx] = winner[m]
            looser[idx] = winner[m+1]
            prior[idx] = m
        idx += 1
        m += 2
    largest = winner[m]
    second = looser[m]
    while m >= 0:
        if second < looser[m]:
            second = looser[m]
        m = prior[m]
    return (largest, second)

print(tournament_two([12,23,11,42,32,65,12,45,67,78,21,34,25,62,43,61]))