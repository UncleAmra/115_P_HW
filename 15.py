def number_part(k):
    up = "".join(str(x) for x in range(1, k + 1))
    down = "".join(str(x) for x in range(k - 1, 0, -1))
    return up + down

m = int(input())
n = int(input())

if n < 3 or n > 50:
    print("Row Error")
else:
    for i in range(1, n + 1):
        if m == 1:
            print(number_part(i))
        elif m == 2:
            pad = "_" * (n - i)
            print(pad + number_part(i) + pad)
        elif m == 3:
            pad = "_" * (i - 1)
            print(pad + number_part(n - i + 1) + pad)