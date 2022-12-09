import sys, fileinput

filename = sys.argv[1]

# initial states
s = (0,0) # start
tail = (0,0) # tail
head = (0,0) # head

visited = set() # set of visited coordinates

def move(dir, dist):
    global head
    global tail
    dist = int(dist)
    dir_value = (0,0)
    if dir == "R":
        dir_value = (1,0)
    elif dir == "L":
        dir_value = (-1,0)
    elif dir == "U":
        dir_value = (0,1)
    elif dir == "D":
        dir_value = (0,-1)
    
    for i in range(0, dist):
        #print("move in", dir_value)
        # move head in direction
        #move head
        head = (head[0] + dir_value[0], head[1] + dir_value[1])

        # check tail
        # if head == 2 in direction, move tail in direction (1)
        if head[0] == tail[0] + 2*dir_value[0] and head[1] == tail[1] + 2*dir_value[1]:
            tail = (tail[0] + dir_value[0], tail[1] + dir_value[1])

        # else if head and tail aren't touching, and aren't in same row, move one step diagonally
        #check if touching
        if not touching() and tail[0] != head[0] and tail[1] != head[1]:
            move_diag()

        # after each move, add tail to visited
        visited.add(tail)

        if not touching():
            print("not touching!")
            exit()

def move_diag():
    global tail
    #print("move diag")
    x = 0
    y = 0

    # above or below
    if tail[1] < head[1]:
        y = 1
    else:
        y = -1

    # left or right
    if tail[0] < head[0]:
        x = 1
    else:
        x = -1

    # move tail in direction
    tail = (tail[0] + x, tail[1] + y)
    visited.add(tail)

def touching():
    global tail
    global head
    #print( "tail", tail, "head", head)
    x1 = tail[0]
    x2 = head[0]
    y1 = tail[1]
    y2 = head[1]
    distance = (((x2 - x1) ** 2) + (y2 - y1) ** 2) ** (1 / 2)
    #print("distance", distance)

    if distance <= 2: #within 2
        return True
    return False

# add tail to visited (at start)
visited.add(tail) 

# read file and execute instructions
with open(filename) as file:
    while True:
        # get next line and strip newline
        line = file.readline().strip()
        # if line is empty, end of file reached
        if not line:
            break
        # do something with line
        line = line.split(" ")
        dir = line[0]
        dist = line[1]
        #print("dir: " + dir + " dist: " + dist)

        move(dir, dist)
        #print("head",head)
        #print("tail",tail)

file.close()

print("head",head)
print("tail",tail)

print("visited", visited)
print("positions:", len(visited))