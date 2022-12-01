import sys, fileinput, heapq

filename = sys.argv[1]

currentElf = 0
elfList = [] # 'heap' of elves

for line in fileinput.input(files = filename):
    print(line)
    if(not line.isspace()):
        n = int(line.strip())
        currentElf += n
    else:
        heapq.heappush(elfList, currentElf)
        currentElf = 0
heapq.heappush(elfList, currentElf) #last elf

print(elfList)

largest = heapq.nlargest(3, elfList) #part2 - get the top 3 elves

print("3 Largest List: " + str(largest))
print("Total: " + str(sum(largest)))

print("\nName of the file currently being read is: ", fileinput.filename())