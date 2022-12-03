import sys, fileinput, string

filename = sys.argv[1]

key = string.ascii_lowercase + string.ascii_uppercase
#print(key.index("p")) # 15

sum = 0
i = 0
for line in fileinput.input(files = filename):
    line = line.strip()
    if i == 0:
        line1 = line
        i += 1
    elif i == 1:
        line2 = line
        i += 1
    elif i == 2:
        line3 = line
        common = set()
        value = 0
        for c in line1:
            if c in line2 and c in line3:
                common.add(c)
        for c2 in common:
            value = key.index(c2) + 1
    
        sum += value
        #print(sum)
        i = 0

print(sum)