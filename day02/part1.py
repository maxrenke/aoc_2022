import sys, fileinput, heapq

filename = sys.argv[1]

# A - Rock
# B - Paper
# C - Scissors

# X - Rock
# Y - Paper
# Z - Scissors

# Loss = 0
# Draw = 3
# Win = 6

#   A B C
# X 3 0 6
# Y 6 3 0
# Z 0 6 3

m = [[3,0,6],
     [6,3,0],
     [0,6,3]]

def getIndex(value):
    if( value == 'A'):
        return 0
    if( value == 'B'):
        return 1
    if( value == 'C'):
        return 2
    if( value == 'X'):
        return 0
    if( value == 'Y'):
        return 1
    if( value == 'Z'):
        return 2

sum = 0

for line in fileinput.input(files = filename):
    line = line.strip().split(" ")
    #print(line)

    sum += m[getIndex(line[1])][getIndex(line[0])] + (getIndex(line[1])+1)

print("Final Score: ",sum)