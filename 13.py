import re

def main():
    try:
        n = int(input().strip())
        if n < 2 or n > 10:
            print(-1)
            return
        courses = []
        for _ in range(n):
            name = input().strip()
            if not re.fullmatch(r"[A-Za-z]+\d{4}", name):
                print(-1)
                return
            h = int(input().strip())
            if h < 1 or h > 3:
                print(-1)
                return
            slots = []
            for _ in range(h):
                t = input().strip()
                if len(t) != 2 or t[0] not in "12345" or t[1] not in "123456789abc":
                    print(-1)
                    return
                slots.append(t)
            if len(set(slots)) != len(slots):
                print(-1)
                return
            courses.append((name, slots))
    except (ValueError, EOFError):
        print(-1)
        return

    result = []
    for i in range(n):
        for j in range(i + 1, n):
            for s in courses[i][1]:
                if s in courses[j][1]:
                    result.append(f"{courses[i][0]},{courses[j][0]},{s}")
    if result:
        print("\n".join(result))
    else:
        print("correct")

main()