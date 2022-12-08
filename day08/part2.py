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
best_score = 0
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
        up_view = 0
        for up in range(y-1,-1,-1):
            up_view += 1
            if m[up][x] >= t:
                up_visible = False
                up_view = y-up
                break
        #print("up_view:",up_view) 
        #print("checking up:",x,up)
                
        #check down
        dn_visible = True
        dn_view = 0
        for dn in range(y+1,h):
            dn_view += 1
            if m[dn][x] >= t:
                dn_visible = False
                break
            #print("checking down:",x,dn)

        #check left
        lf_visible = True
        lf_view = 0
        for lf in range(x-1,-1,-1):
            lf_view += 1
            if m[y][lf] >= t:
                lf_visible = False
                break
            #print("checking left:",lf,y)

        #check right
        rt_visible = True
        rt_view = 0
        for rt in range(x+1,w):
            rt_view += 1
            if m[y][rt] >= t:
                rt_visible = False
                break
            #print("checking right:",rt,y)

        # if visible in any direction, it's visible!
        #print("up",up_visible)
        #print("dn",dn_visible)
        #print("lf",lf_visible)
        #print("rt",rt_visible)
        #if up_visible or dn_visible or lf_visible or rt_visible:
        #    visible += 1

        # calculate scenic score
        scenic_score = up_view*dn_view*lf_view*rt_view
        #print("scenic score: ", scenic_score)

        # find the highest scenic score from all trees
        if scenic_score > best_score:
            best_score = scenic_score

print("best score: ", best_score)
