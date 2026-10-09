from datetime import date

def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def is_valid(y, m, d):
    if m < 1 or m > 12:
        return False
    days_in_month = [0, 31, 29 if is_leap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if d < 1 or d > days_in_month[m]:
        return False
    return True

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

if not is_valid(y1, m1, d1) or not is_valid(y2, m2, d2):
    print("Invalid Date")
elif (y2, m2, d2) < (y1, m1, d1):
    print("Invalid Range")
else:
    dt1 = date(y1, m1, d1)
    dt2 = date(y2, m2, d2)
    print((dt2 - dt1).days)

print("Leap Year" if is_leap(y1) else "Common Year")
print("Leap Year" if is_leap(y2) else "Common Year")