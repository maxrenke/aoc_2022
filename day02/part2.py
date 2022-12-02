import sys, fileinput, heapq

filename = sys.argv[1]

# A - Rock
# B - Paper
# C - Scissors

# X - Lose
# Y - Draw
# Z - Win

# Loss = 0
# Draw = 3
# Win = 6

# R - 1
# P - 2
# S - 3

#      A(R) B(P) C(S)
# X(L)  3    1    2
# Y(D)  1    2    3
# Z(W)  2    3    1

m = [[3,1,2],
     [1,2,3],
     [2,3,1]]

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

def getResult(result):
    if( result == 'X'):
        return 0
    if( result == 'Y'):
        return 3
    if( result == 'Z'):
        return 6

sum = 0

for line in fileinput.input(files = filename):
    line = line.strip().split(" ")
    #print(line)

    moveScore = m[getIndex(line[1])][getIndex(line[0])]
    moveResult = getResult(line[1])

    sum += moveScore + moveResult

print("Final Score: ",sum)