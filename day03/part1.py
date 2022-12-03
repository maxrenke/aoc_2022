import sys, fileinput, string

filename = sys.argv[1]

key = string.ascii_lowercase + string.ascii_uppercase
#print(key.index("p")) # 15

sum = 0

for line in fileinput.input(files = filename):
    line = line.strip()
    #print(line)
    length = len(line)
    p1 = line[0:length//2]
    #print("p1",p1)
    p2 = line[length//2:]
    #print("p2",p2)

    i = 0
    common = set()
    for c in p1:
        if( c in p2 ): #match
            common.add(c)
    #print("common",common)
    for c2 in common:
        value = key.index(c2) + 1
        #print(value)
        sum += value

print(sum)