
def optimal_sequence(n):
    if n == 1:
        return [1]
    sequence = [[]] * (n+1)
    sequence[1] = [1]
    for m in range(2,n+1):
        if m%3 == 0:
            minNum = min(len(sequence[m//3]) + 1, len(sequence[m//2]) +1)
            if minNum == len(sequence[m//3]) + 1:
                sequence[m] = sequence[m//3] + [m]
            else:
                sequence[m] = sequence[m-1] + [m]
        elif m%2 == 0:
            minNum = min(len(sequence[m - 1]) + 1, len(sequence[m//2]) +1)
            if minNum == len(sequence[m//2]) + 1:
                sequence[m] = sequence[m//2] + [m]
            else:
                sequence[m] = sequence[m-1] + [m]
        else:
            sequence[m] = sequence[m-1] + [m]

    return sequence[m],len(sequence[m])
print(len(optimal_sequence2(1000000)))