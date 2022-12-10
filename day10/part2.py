import sys, fileinput

filename = sys.argv[1]

x = 1 # x register
clk = 0 # clock cycle
ptr = 0 # program counter
inst = [""] # current instruction
halt = False
signal_sum = 0
CRT = ""
sprite = [0,2]

with open(filename) as file:
    line = ""
    while True:
        # print state
        #print("b:clk",clk,"ptr",ptr,"inst",inst,"x",x)

        if halt:
            break
        
        #print(sprite)
        i = clk % 40
        sprite = [x, x+2]
        #print(i, sprite[0], sprite[1])
        if i >= sprite[0] and i <= sprite[1]:
            CRT += "X"
        else:
            CRT += "."

        if clk % 40 == 0:
            print(CRT)
            CRT = ""
        

        
        if ptr == 0: # new instruction
            # execute instruction
            if inst[0] == "noop":
                pass # do nothing
            elif inst[0] == "addx":
                #print("add ",inst[1])
                #print("add ",int(inst[1]))
                x = x + int(inst[1])
                #print(x)

            # get next line
            line = file.readline().strip()
            if not line:
                #print("end of file")
                halt = True # halt
            inst = line.split(" ") # split line
            if inst[0] == "noop":
                ptr += 1 # increment program counter
            elif inst[0] == "addx":
                #print("addx")
                ptr += 2 # increment program counter

       


        # print state
        #print("a:clk",clk,"ptr",ptr,"inst",inst,"x",x)

        # tick the clock cycle
        clk += 1
        sprite[0] += 1
        sprite[1] += 1
        ptr -= 1

file.close()

# solution

#print("signal sum",signal_sum)