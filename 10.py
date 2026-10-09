def card_value(card):
    card = card.strip()
    if card in ['J', 'Q', 'K']:
        return 0.5
    if card == 'A':
        return 1.0
    return float(card)

cards_x = [input() for _ in range(3)]
cards_y = [input() for _ in range(3)]

score_x = sum(card_value(c) for c in cards_x)
score_y = sum(card_value(c) for c in cards_y)

if score_x > 10.5:
    score_x = 0
if score_y > 10.5:
    score_y = 0

def format_score(s):
    return int(s) if s == int(s) else s

print(format_score(score_x))
print(format_score(score_y))

if score_x > score_y:
    print("X Win")
elif score_y > score_x:
    print("Y Win")
else:
    print("Tie")