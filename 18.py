n = int(input())
board = [input().strip() for _ in range(n)]

def count_lines(lines):
    result = {"B": 0, "W": 0}
    for line in lines:
        for i in range(1, len(line) - 3):
            seg = line[i:i + 3]
            if line[i - 1] == "." and line[i + 3] == "." and seg in ("BBB", "WWW"):
                result[seg[0]] += 1
    return result

horizontal = count_lines(board)
columns = ["".join(board[r][c] for r in range(n)) for c in range(n)]
vertical = count_lines(columns)

print("Horizontal:" , horizontal["B"] + horizontal  ["W"])
print("Vertical:"   , vertical  ["B"] + vertical    ["W"])
print("Black:"      , horizontal["B"] + vertical    ["B"])
print("White:"      , horizontal["W"] + vertical    ["W"])
