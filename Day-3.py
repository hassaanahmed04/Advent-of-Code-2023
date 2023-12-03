# Day 3 q 1
import re
with open('D:/test.txt', 'r') as f:
    data = f.read().split()
result = 0
for y, line in enumerate(data):
    for m in re.compile(r"\d+").finditer(line):
        include = False
        for x in range(m.start(), m.end()):
            for y2 in range(y-1, y+2):
                if y2 < 0 or y2 >= len(data):
                    continue
                for x2 in range(x-1, x+2):
                    if x2 < 0 or x2 >= len(line):
                        continue
                    if data[y2][x2] not in (".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        include = True
        if include:
            result += int(m.group())
print(result)