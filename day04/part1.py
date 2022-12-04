import sys, fileinput

filename = sys.argv[1]

total = 0

for line in fileinput.input(files = filename):
    
    line = line.strip()
    sline = line.split(",")
    left = sline[0]
    right = sline[1]

    # make left
    #print(left)
    left_split = left.split("-")
    left_start = int(left_split[0])
    left_end = int(left_split[1])
    
    left_array = bytearray(left_end+1)
    for i in range(left_start, left_end+1):
        left_array[i] = 1
    
    #print(left_array)

    # make right
    #print(right)
    right_split = right.split("-")
    right_start = int(right_split[0])
    right_end = int(right_split[1])
    
    right_array = bytearray(right_end+1)
    for i in range(right_start, right_end+1):
        right_array[i] = 1
    
    #print(right_array)

    if left_end > right_end:
        right_array.extend(bytearray(left_end-right_end))

    else:
        left_array.extend(bytearray(right_end-left_end))
    
    #print("l",left_array)
    #print("r",right_array)

    masked_array = bytearray(len(left_array))
    for i in range(len(left_array)):
        masked_array[i] = left_array[i] & right_array[i]
    
    #print("m",masked_array)
    #print("c",left_array == masked_array or right_array == masked_array)

    if left_array == masked_array or right_array == masked_array:
        total += 1

print(total)
    

    