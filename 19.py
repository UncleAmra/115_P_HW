n = int(input())
bases = [0, 0, 0]
score = 0
outs = 0

for _ in range(n):
    k = int(input())
    if k == 0:
        outs += 1
        if outs == 3:
            outs = 0
            bases = [0, 0, 0]
    else:
        new_bases = [0, 0, 0]
        for i in range(3):
            if bases[i]:
                pos = i + 1 + k
                if pos >= 4:
                    score += 1
                else:
                    new_bases[pos - 1] = 1
        if k >= 4:
            score += 1
        else:
            new_bases[k - 1] = 1
        bases = new_bases

print(score)
print(*bases)