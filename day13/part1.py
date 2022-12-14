import sys, fileinput

filename = sys.argv[1]

with open(filename) as file:
    lines = file.read().strip().split("\n\n")

def compareLists(l, r):
    #print("compare ", l, r)
    try:
        length = len(l)
        #print(l)
    except:
        length = 1
    for i in range(0,length):
        try:
            a = l[i]
            #print(a)
            b = r[i]
            #print(b)
        except:
            a = l
            b = r
        if isinstance(a, list) and isinstance(b, list):
            #print("compare list", a, b)
            if len(b) < len(a):
                #print("false")
                return False                
            if compareLists(a[0], b[0]):
                #print(a[0])
                #print(b[0])
               # print("true")
                pass
            return compareLists(a[1:], b[1:])
        elif isinstance(a, int) and isinstance(b, int):
            #print("compare int", a, b)
            if a == b or a < b:
                pass
            else:
                return False
        else:
            # convert to list
            #print("convert to list", a, b)
            if isinstance(a, int):
                a = [a]
            if isinstance(b, int):
                b = [b]
            return compareLists(a , b)
    
    return True

ans = 0
for i, line in enumerate(lines):
    #print("line: ", line)
    left, right = map(eval, line.split("\n"))
    #print(i, left, right)

    if compareLists(left, right):
        #print("right order: ", left, right)
        ans += (i+1)

print(ans)
    