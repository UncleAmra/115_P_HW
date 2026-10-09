rolls = []

r1 = int(input())
rolls.append(r1)
if r1 < 10:
    r2 = int(input())
    rolls.append(r2)

r1 = int(input())
rolls.append(r1)
if r1 < 10:
    r2 = int(input())
    rolls.append(r2)

r1 = int(input())
rolls.append(r1)
if r1 == 10:
    ex1 = int(input())
    ex2 = int(input())
    rolls.append(ex1)
    rolls.append(ex2)
else:
    r2 = int(input())
    rolls.append(r2)
    if r1 + r2 == 10:
        ex1 = int(input())
        rolls.append(ex1)

total_score = 0
i = 0
for _ in range(3):
    if rolls[i] == 10:
        total_score += 10 + rolls[i + 1] + rolls[i + 2]
        i += 1
    elif rolls[i] + rolls[i + 1] == 10:
        total_score += 10 + rolls[i + 2]
        i += 2
    else:
        total_score += rolls[i] + rolls[i + 1]
        i += 2

print(total_score)