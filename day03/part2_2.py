import sys, fileinput, string

filename = sys.argv[1]

key = string.ascii_lowercase + string.ascii_uppercase
#print(key.index("p")) # 15

numberOfElves = 3 #global variable
sum = 0
i = 0
lines = []
for line in fileinput.input(files = filename):
    
    line = line.strip()
    
    lines.append(line)

    if len(lines) == numberOfElves:
        first = lines[0]
        
        for c in first:
            match = True
            for line in lines:
                if c in line:
                    match = match & True
                else:
                    match = match & False
            if match:
                #print("c: ", c, "line: ", line)
                value = key.index(c) + 1
                sum += value
                break
        
        lines = []
        

print(sum)