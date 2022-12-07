import sys, fileinput, queue

filename = sys.argv[1]

distinct_chars = 14

for line in fileinput.input(files = filename):
    seen = []
    print(line.strip())
    for i in enumerate(line):
        c = i[1]
        seen.append(c)
        if i[0] > distinct_chars - 1:
            seen.pop(0)
        if len(set(seen)) == distinct_chars:
            start_of_packet = i[0] + 1
            print(start_of_packet)
            break