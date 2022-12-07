import sys, fileinput, queue

filename = sys.argv[1]

for line in fileinput.input(files = filename):
    seen = []
    print(line.strip())
    for i in enumerate(line):
        c = i[1]
        seen.append(c)
        if i[0] > 3:
            seen.pop(0)
        if len(set(seen)) == 4:
            start_of_packet = i[0] + 1
            print(start_of_packet)
            break