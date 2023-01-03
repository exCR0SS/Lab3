class Main:

    x = int(input())
    i = 1
    res = [1, 1]

    while i != x - 1:
        res.append(res[i-1] + res[i])
        i += 1
    print(*res)