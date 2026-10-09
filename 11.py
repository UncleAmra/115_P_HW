lines = []
for _ in range(3):
    x1 = int(input())
    x2 = int(input())
    lines.append((min(x1, x2), max(x1, x2)))

lines.sort()

merged = []
for start, end in lines:
    if not merged or merged[-1][1] < start:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

print(sum(end - start for start, end in merged))