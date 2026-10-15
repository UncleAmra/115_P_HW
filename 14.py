def score(p):
    special = "~!@#$%^&*<>_+="
    total = 0.0
    digit_count = 0
    for c in p:
        if c.islower():
            total += 1
        elif c.isupper():
            total += 3
        elif c.isdigit():
            total += 2
            digit_count += 1
        elif c in special:
            total += 4.5
    if digit_count >= 5:
        separated = True
        for i in range(len(p) - 1):
            if p[i].isdigit() and p[i + 1].isdigit():
                separated = False
                break
        if separated:
            total += 10
    if len(p) > 8:
        total += len(p) - 8
    if "1234" in p:
        total -= 10
    return total

n = int(input())
best = None
worst = None
for _ in range(n):
    p = input().strip()
    s = score(p)
    if best is None or s > best[1]:
        best = (p, s)
    if worst is None or s < worst[1]:
        worst = (p, s)
print(f"{best[0]} {best[1]:.1f}")
print(f"{worst[0]} {worst[1]:.1f}")