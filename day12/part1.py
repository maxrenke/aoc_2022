import sys, fileinput, heapq

filename = sys.argv[1]

grid = [[]]
row = 0
col = 0

with open(filename) as file:
    line = ""
    while True:

        # get next line
        line = file.readline().strip()
        if line == "": break

        for c in line:
            c_val = ord(c) - 96
            if c_val == -13: # start
                c_val = 0
            if c_val == -27: # end
                c_val = 25
            grid[col].append(c_val)

        row = len(grid[col])
        grid.append([])
        col += 1

file.close()

# print grid (for debugging)
for gc in grid:
    for c in gc:
        print(c, end=" ")
    print()

# Do DFS :)

# define start
# ( value , x , y )
#end = (0,2,5)
start = (0,0,0)

visited = set()
heap = [(0,start[0],start[1])]
#heapq.heapify(heap)
visited.add(start)

def neighbors(x,y):
    global row
    global col
    up = (x,y-1)
    down = (x,y+1)
    left = (x-1,y)
    right = (x+1,y)

    dirs = [up, down, left, right]
    valid = []
    for d in dirs:
        xx = d[0]
        yy = d[1]
        if xx >= 0 and xx < row and yy >= 0 and yy < col:
            # if (xx,yy) is at most 1 higher than (x,y)
            dest_height = grid[yy][xx]
            curr_height = grid[y][x]

            #print("x: " + str(x) + " y: " + str(y) + " xx: " + str(xx) + " yy: " + str(yy))
            #print("dest_height: " + str(dest_height) + " curr_height: " + str(curr_height))

            if dest_height <= curr_height + 1:
                valid.append(d)

    print(valid)

    return valid

     
    
    #filteredList = list(filter(lambda z: z[0] >= 0 and z[0] < row and z[1] >= 0 and z[1] <= col and grid[x][y] < grid[z[0]][z[1]], [up, down, left, right]))
    #print(filteredList)
    #return filteredList
    

while heap:
    print(heap)
    #curr = heapq.heappop(heap)
    #steps = curr[0]
    #x = curr[1]
    #y = curr[2]

    steps, x, y = heapq.heappop(heap)

    #print("(", x, ",", y, ") steps: " + str(steps))
    # check if visited
    if (x,y) in visited:
        continue
    visited.add((x,y))

    # check if at end
    if grid[x][y] == 25:
        print("Found it! Steps: " + str(steps))
        break

    for (i,j) in neighbors(x,y):
        if (i,j) not in visited:
            heapq.heappush(heap, (steps + 1, i, j))

print(visited)
# print grid (for debugging)
for i in range(0, col):
    for j in range(0, row):
        if (i,j) in visited:
            print("X", end=" ")
        else:
            print(grid[i][j], end=" ")
    print()