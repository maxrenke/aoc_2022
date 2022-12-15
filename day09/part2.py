import sys, fileinput

filename = sys.argv[1]

# initial states
s = (0,0) # start
tail = (0,0) # tail
head = (0,0) # head
rope = [] # rope

rope_length = 10
rope.append(head)
for i in range(0, rope_length - 2):
    rope.append((0,0))
rope.append(tail)

print("rope:", rope)


visited = set() # set of visited coordinates

def move(dir, dist):
    global rope
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
    
    print("move in", dir_value)
    # move head in direction
    #move head
    rope[0] = (rope[0][0] + dir_value[0], rope[0][1] + dir_value[1])

    for i in range(1, rope_length):
        if not touching(i, i-1):
            move_knot(i, i-1, dir_value[0], dir_value[1])
            
        

    # after each move, add tail to visited
    visited.add(rope[rope_length-1])

    #if not touching(rope[0],rope[rope_length-1]):
    for i in range(0, rope_length-1):
        if not touching(i,i-1):
            print("not touching!")
            #exit()

    #return rope

def move_knot(knot1,knot2,dir_value_x,dir_value_y):
    global rope
    print("move diag")
    x = dir_value_x
    y = dir_value_y


    # move tail in direction
    rope[knot1] = (rope[knot1][0] + x, rope[knot1][1] + y)
    visited.add(rope[rope_length-1])

    #return knot1, knot2

def touching(knot1,knot2):
    global rope
    #print( "tail", tail, "head", head)
    x1 = rope[knot1][0]
    x2 = rope[knot2][0]
    y1 = rope[knot1][1]
    y2 = rope[knot2][1]
    distance = (((x2 - x1) ** 2) + (y2 - y1) ** 2) ** (1 / 2)
    #print("distance", distance)

    if distance <= 1: #within 2
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

        for i in range(0, int(dist)):
            move(dir, dist)
        #print("head",head)
        #print("tail",tail)

file.close()

print("head",rope[0])
print("tail",rope[rope_length-1])
print("rope", rope)

#print("visited", visited)
print("positions:", len(visited))