def progression(a):
    min_quantity = len(a)
    min_dif = 0
    min_a1 = 0
    for i in range(len(a) - 1):
        quantity = 0
        dif = a[i + 1] - a[i]
        for j in range(len(a)):
            if a[j] != a[i] + dif * (j - i):
                quantity += 1
        if quantity < min_quantity:
            min_quantity = quantity
            min_dif = dif
            min_a1 = a[i] - dif * i
    return list(range(min_a1, min_a1 + min_dif * len(a), min_dif))


if __name__ == '__main__':
    example = [1, 16, 4, 10, 7, 11, 1, -2]
    print('Result:  ', progression(example))