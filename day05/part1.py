import sys, fileinput, re

filename = sys.argv[1]

# Set a global variable for file input
full_input = []

# Read the file into a list
for line in fileinput.input(files = filename):
    full_input.append(line)

# Get the index of the first blank line
newline = full_input.index('\n')

# Get the first part of the file
stack_input = full_input[:newline]
# Get the second part of the file
move_input = full_input[newline+1:]

# Handle stack input

# Remove last element of stack_input (just indexes)
number_of_stacks_line = stack_input.pop().strip()
number_of_stacks = len(number_of_stacks_line)//3 #assumes number of stacks is 1-9

# Initialize stacks
stacks = []
for i in range(0,number_of_stacks): stacks.append([])

# Add elements to stacks
for s in stack_input:
    # strip whitespace
    s = s.rstrip()

    # Split the line into a list of elements
    substrings = [s[i:i+4] for i in range(0, len(s), 4)]
    #print(substrings)
    
    i = 0
    for crate in substrings:
        # strip the whitespace and brackets
        crate = crate.replace('[', '')
        crate = crate.replace(']', '')
        crate = crate.replace(' ', '')
        
        #print(i, crate)
        if len(crate) != 0 : stacks[i].append(crate)
        i += 1

# Stacks are now initialized
print("stacks: ", stacks)

# Handle move input
#print(move_input)
moves = []
for move in move_input:
    minput = [word for word in move.split() if word.isdigit()]
    # minput now has the format [number_of_crates, from_stack, to_stack]
    moves.append(minput)

# Now make the moves
print(moves)
for move in moves:
    #print(move)
    n = int(move[0])
    #print("n: ", n)
    from_stack = int(move[1]) - 1
    #print("from_stack: ", from_stack)
    to_stack = int(move[2]) - 1
    #print("to_stack: ", to_stack)
    for i in range(0,n):
        # pop from front [pop(0)] from_stack and insert at beginning of to_stack [insert(0)]
        stacks[to_stack].insert(0,stacks[from_stack].pop(0))
        #print(stacks)

# After the rearrangement procedure completes, what crate ends up on top of each stack?
elf_message = ""
for stack in stacks:
    if len(stack) != 0 : elf_message += stack[0]

print("elf_message: ", elf_message)