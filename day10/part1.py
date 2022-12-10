import sys, fileinput

filename = sys.argv[1]

x = 1 # x register
clk = 0 # clock cycle
ptr = 0 # program counter
inst = [""] # current instruction
halt = False
signal_sum = 0

with open(filename) as file:
    line = ""
    while True:
        # print state
        #print("b:clk",clk,"ptr",ptr,"inst",inst,"x",x)

        if halt:
            break

         # check signal strength
        if ((clk-20) % 40 == 0) and clk > 0:
            # calculate signal strength
            print("x",x)
            signal_strength = clk * x # clock cycle * x register
            print("strength at clk",clk,"is",signal_strength)
            signal_sum += signal_strength
        
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
        ptr -= 1

file.close()

# solution

print("signal sum",signal_sum)