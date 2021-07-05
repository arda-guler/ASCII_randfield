import random
from os import system, name
import time
import math

def generateArtASCII(x_size=50, y_size=50, mode="lines_rects"):

    #--------------------------------
    #        ASCII CHARACTERS
    #--------------------------------

    dots = [".", "o", "O"]
    crosses = ["+", "x", "X"]
    squares = ["#", "H"]
    singles = dots + crosses + squares

    horizontal_chars = ["-", "=", "_"]
    vertical_chars = ["|", "!", "I"]
    diagonals = ["/", "\\"]

    #--------------------------------
    #          CANVAS SETUP
    #--------------------------------

    canvas = []

    def canvas_reset():
        for y in range(y_size):
            canvas.append([])
            for x in range(x_size):
                canvas[y].append(" ")

    #--------------------------------
    #          ART ELEMENTS
    #--------------------------------

    # fill canvas with random single characters

    def only_dots():
        for y in range(y_size):
            for x in range(x_size):
                canvas[y][x] = random.choice(dots)

    def only_crosses():
        for y in range(y_size):
            for x in range(x_size):
                canvas[y][x] = random.choice(crosses)

    def only_squares():
        for y in range(y_size):
            for x in range(x_size):
                canvas[y][x] = random.choice(squares)

    def mixed_singles():
        for y in range(y_size):
            for x in range(x_size):
                canvas[y][x] = random.choice(singles)

    # draw line with random length and direction

    def line():
        index = [random.randint(0, y_size-1), random.randint(0, x_size-1)] # y, x
        length = random.randint(2, int((y_size * x_size) ** 0.5))
        direction = random.randint(1, 8)

        if direction == 1 or direction == 5:
            line_char = random.choice(vertical_chars)

        if direction == 3 or direction == 7:
            line_char = random.choice(horizontal_chars)

        if direction == 2 or direction == 6:
            line_char = diagonals[0]

        if direction == 4 or direction == 8:
            line_char = diagonals[1]

        line_length = 0
        
        while True:
            line_length += 1
            if direction == 1:
                index[0] -= 1
            elif direction == 2:
                index[0] -= 1
                index[1] += 1
            elif direction == 3:
                index[1] += 1
            elif direction == 4:
                index[0] += 1
                index[1] += 1
            elif direction == 5:
                index[0] -= 1
            elif direction == 6:
                index[0] += 1
                index[1] -= 1
            elif direction == 7:
                index[1] -= 1
            elif direction == 8:
                index[0] -= 1
                index[1] -= 1

            # stop if we try to draw a line out of bounds, or we reach the length we wanted
            if (line_length >= length):
                break

            try:
                canvas[index[0]][index[1]] = line_char
            except IndexError:
                break

    # draw random rectangle with a random character
    
    def rectangle():
        area_char = random.choice(singles)

        start_index = [random.randint(0, y_size-3), random.randint(0, x_size-3)] # y, x
        finish_index = [random.randint(start_index[0]+1, y_size-1), random.randint(start_index[1]+1, x_size-1)] # y, x

        current_index = [start_index[0], start_index[1]]

        while True:
            try:
                canvas[current_index[0]][current_index[1]] = area_char
            except:
                break
            
            if current_index[1] > finish_index[1]:
                if current_index[0] < finish_index[0]:
                    current_index[0] += 1
                    current_index[1] = start_index[1]
                else:
                    break
            else:
                current_index[1] += 1

    # draw random disc with a random character

    def disc():
        area_char = random.choice(singles)

        center_index = [random.randint(0, y_size), random.randint(0, x_size)] # y, x
        radius = random.randint(0, int((x_size * y_size)**0.4))

        current_angle = 0 # degrees
        current_radius = 0
        current_index = center_index

        while True:
            if current_angle >= 360 and current_radius < radius:
                current_angle = 0
                current_radius += 1
            elif current_angle >= 360 and current_radius >= radius:
                break
            else:
                current_angle += 1

            # y = r * sin(angle)
            # x = r * cos(angle)

            current_index = [int(center_index[0] + current_radius * math.sin(math.radians(current_angle))),
                             int(center_index[1] + current_radius * math.cos(math.radians(current_angle)))]

            if (current_index[0] < 0 or current_index[0] > y_size or
                current_index[1] < 0 or current_index[1] > x_size):
                pass
            else:
                try:
                    canvas[current_index[0]][current_index[1]] = area_char
                except:
                    pass

    #--------------------------------
    #          ART MODES
    #--------------------------------

    # first of all, have a canvas ready
    canvas_reset()

    if mode == "dots":
        only_dots()

    elif mode == "crosses":
        only_crosses()

    elif mode == "squares":
        only_squares()

    elif mode == "mixed_singles":
        mixed_singles()

    elif mode == "discs":
        for i in range(0, int((x_size * y_size)**0.2)):
            disc()

    elif mode == "lines":
        for i in range(0, int((x_size * y_size)**0.5)):
            line()

    elif mode == "rectangles":
        for i in range(0, int((x_size * y_size)**0.5)):
            rectangle()

    elif mode == "lines_rects":
        for i in range(0, int((x_size * y_size)**0.4)):
            rectangle()
        for i in range(0, int((x_size * y_size)**0.4)):
            line()

    elif mode == "mixed":
        for r in range(0, 10):
            mixed_singles()
            for i in range(0, int((x_size * y_size)**0.2)):
                rectangle()
            for i in range(0, int((x_size * y_size)**0.2)):
                disc()
            for i in range(0, int((x_size * y_size)**0.2)):
                line()
        
    #--------------------------------
    #       DISPLAY RESULT
    #--------------------------------

    strings = []
    for i in range(y_size):
        strings.append("".join(canvas[i]))

    for string in strings:
        string = string + "\n"
        print(string)

x_in = input("X:")
y_in = input("Y:")
mode = input("MODE:")
stream = input("Stream? (y/N):")

if not x_in:
    x_in = 100
else:
    x_in = int(x_in)

if not y_in:
    y_in = 15
else:
    y_in = int(y_in)

if not mode:
    mode = "lines_rects"

if stream == "y" or stream == "Y":
    stream = True
else:
    stream = False

generateArtASCII(x_in, y_in, mode)
while stream:
    try:
        if name == "nt":
            system("cls")
        else:
            system("clear")
    except:
        pass

    generateArtASCII(x_in, y_in, mode)
    time.sleep(0.1)
    
    


