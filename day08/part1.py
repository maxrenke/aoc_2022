import sys, fileinput

filename = sys.argv[1]

m = []

with open(filename) as file:
    i = 0
    while True:
        line = file.readline().strip() # get next line
        if not line:
            break
        row = []
        for c in line:
            row.append(int(c))
        m.append(row)    
        i += 1

file.close()

#print(m)
for row in m:
    print(row)


visible = 0
h = len(m)
w = len(m[0])
for x in range(0,w):
    for y in range(0,h):
        # if already on edge, skip
        if x == 0 or x == w-1 or y == 0 or y == w-1:
            #print("skipping t:",x,y)
            visible += 1
            continue
        t = m[y][x]
        #print("checking t :",x,y)
        # only look up, down, left, or right from any given tree.
        # check up
        up_visible = True
        for up in range(y-1,-1,-1):
            if m[up][x] >= t:
                up_visible = False
                break
            #print("checking up:",x,up)
                
        #check down
        dn_visible = True
        for dn in range(y+1,h):
            if m[dn][x] >= t:
                dn_visible = False
                break
            #print("checking down:",x,dn)

        #check left
        lf_visible = True
        for lf in range(x-1,-1,-1):
            if m[y][lf] >= t:
                lf_visible = False
                break
            #print("checking left:",lf,y)

        #check right
        rt_visible = True
        for rt in range(x+1,w):
            if m[y][rt] >= t:
                rt_visible = False
                break
            #print("checking right:",rt,y)

        # if visible in any direction, it's visible!
        #print("up",up_visible)
        #print("dn",dn_visible)
        #print("lf",lf_visible)
        #print("rt",rt_visible)
        if up_visible or dn_visible or lf_visible or rt_visible:
            visible += 1

print(visible)
