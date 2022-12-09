import sys, fileinput

filename = sys.argv[1]

# initial states
s = (0,0) # start
tail = (0,0) # tail
head = (0,0) # head
rope = [] # rope

rope_length = 2
rope.append(head)
for i in range(0, rope_length - 2):
    rope.append((0,0))
rope.append(tail)

print("rope:", rope)


visited = set() # set of visited coordinates

def move(head,tail,dir, dist):
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
    
    #print("move in", dir_value)
    # move head in direction
    #move head
    head = (head[0] + dir_value[0], head[1] + dir_value[1])

    for i in range(1, rope_length):
        print("check rope", i)
        last = rope[i-1]
        print(last)
        curr = rope[i]
        print(curr)
        

    # check tail
    # if head == 2 in direction, move tail in direction (1)
    if head[0] == tail[0] + 2*dir_value[0] and head[1] == tail[1] + 2*dir_value[1]:
        tail = (tail[0] + dir_value[0], tail[1] + dir_value[1])

    # else if head and tail aren't touching, and aren't in same row, move one step diagonally
    #check if touching
    if not touching(head,tail) and tail[0] != head[0] and tail[1] != head[1]:
        head, tail = move_diag(head,tail)

    # after each move, add tail to visited
    visited.add(tail)

    if not touching(head,tail):
        print("not touching!")
        exit()

    return head, tail

def move_diag(head,tail):
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

    return head, tail

def touching(head,tail):
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

        for i in range(0, int(dist)):
            head, tail = move(head,tail,dir, dist)
        #print("head",head)
        #print("tail",tail)

file.close()

print("head",head)
print("tail",tail)

print("visited", visited)
print("positions:", len(visited))