import sys, fileinput, re

filename = sys.argv[1]

grid = [[]]

def print_grid():
    for y in range(y_min-1,y_max+1):
        for x in range(x_min-1,x_max+1):
            print(grid[y][x], end="")
        print()

def drop_grain():
    global grid
    global grain

    #print_grid()

    before_x = grain[0]
    before_y = grain[1]
    
    # try and move (blocked by rock or sand)
    if grid[grain[1]+1][grain[0]] == 0: # down
        grain[1] += 1
    elif grid[grain[1]+1][grain[0]-1] == 0: #down and to left
        grain[1] += 1
        grain[0] -= 1
    elif grid[grain[1]+1][grain[0]+1] == 0: #down and to right
        grain[1] += 1
        grain[0] += 1
    else: # at rest
        #print("at rest")
        return True
    
    # new location
    x = grain[0]
    y = grain[1]

    # check if falling into the void
    #print( y, y_max)
    if y >= y_max:
        # into the void
        return False
    else:
        # update grid
        grid[before_y][before_x] = 0
        return drop_grain()

    print("oops")


def place_rock(line):
    points = line.split(" -> ")
    #print("points: ", points)
    for i,point in enumerate(points):
        x, y = point.split(",")
        next_x, next_y = points[i+1].split(",") if i+1 < len(points) else (x,y)
        #print(" x: ", x, " y: ", y)
        #print("nx: ", next_x, "ny: ", next_y)

        x_dir = 1 if int(next_x) > int(x) else -1
        y_dir = 1 if int(next_y) > int(y) else -1

        if x_dir == 1:
            for x in range(int(x), int(next_x)+1):
                grid[int(y)][int(x)] = 2
        else:
            for x in range(int(x), int(next_x)-1, -1):
                grid[int(y)][int(x)] = 2
        
        if y_dir == 1:
            for y in range(int(y), int(next_y)+1):
                grid[int(y)][int(x)] = 2
        else:
            for y in range(int(y), int(next_y)-1, -1):
                grid[int(y)][int(x)] = 2

with open(filename) as file:
    all = file.read()
    lines = all.strip().split("\n")

# get min and max
numbers = re.findall(r'\d+,', all)
x_max = max(int(x[:-1]) for x in numbers)
x_min = min(int(x[:-1]) for x in numbers)
numbers = re.findall(r',\d+', all)
y_max = max(int(x[1:]) for x in numbers)
y_min = min(int(x[1:]) for x in numbers)

#print("max: ", maximum)
#print("min: ", minimum)
print("x_max", x_max)
print("x_min", x_min)

print("y_max", y_max)
print("y_min", y_min)

grid = [[0] * (x_max+1) for i in range(y_max+1)]
sand_start = (500,0)
grid[sand_start[1]][sand_start[0]] = -1

for line in lines: place_rock(line)

# count dropped
dropped = 0

grain = [500, 0] # redundant
keep_dropping = True
while keep_dropping:
    grain = [500, 0]
    #print(keep_dropping)
    keep_dropping = drop_grain()
    if keep_dropping:
        dropped += 1
    #print(keep_dropping)
    #print(grain)

print_grid()

print("dropped: ", dropped)