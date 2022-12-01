import sys, fileinput, heapq

filename = sys.argv[1]

currentElf = 0
elfList = [] # 'heap' of elves

for line in fileinput.input(files = filename):
    if(not line.isspace()):
        n = int(line.strip())
        currentElf += n
    else:
        heapq.heappush(elfList, currentElf)
        currentElf = 0
heapq.heappush(elfList, currentElf) #last elf

print(elfList)

largest = heapq.nlargest(1, elfList)

print("Largest: " + str(largest))

print("\nName of the file currently being read is: ", fileinput.filename())