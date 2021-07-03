import random
import time
from os import system, name

buffer = []

line1 = 1
line2 = 11
line3 = 22
line4 = 33
line5 = 44
line6 = 55
line7 = 66

lines = [line1, line2, line3, line4, line5, line6, line7]

for y in range(0,17):
    buffer.append([])
    for x in range(0, 77):
        buffer[y].append(" ")

while True:

    for y in range(1, 17):
        buffer[0] = []

        for x in range(0, 77):
            match = False
            for line in lines:
                if x == line:
                    match = True

            if match:
                buffer[0].append("#")
            else:
                buffer[0].append(" ")

        buffer[16-y] = buffer[15-y]

    for line in range(0, 7):
        if lines[line] - 1 == lines[line - 1] or lines[line] - 1 < 0:
            lines[line] += random.randint(0, 1)
        elif (line + 1 <= 6 and lines[line] + 1 == lines[line + 1]) or lines[line] + 1 > 77:
            lines[line] += random.randint(-1, 0)
        else:
            lines[line] += random.randint(-1, 1)

    strings = []
    for y in range(0, 17):
        strings.append("".join(buffer[y]))

    for string in strings:
        string = string + "\n"
        print(string)

    time.sleep(0.07)

    try:
        if name == "nt":
            system("cls")
        else:
            system("clear")
    except:
        pass
        
