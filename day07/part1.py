import sys, fileinput

filename = sys.argv[1]

directories = []

class Directory:
    
    def __init__(self, name, size=0, files = []):
        self.files = [] # list of tuples (filename, size)
        self.name = name
        self.parent = None
        self.children = []
        self.size = 0
        directories.append(self)

def calculateSize(directory):
    for file in directory.files:
        directory.size += int(file[1])
    for child in directory.children:
        calculateSize(child)
        directory.size += child.size
    

root = Directory("/") # root directory
current = root # current directory
command = ""
line = ""
last_line = ""
skipped = ""

with open(filename) as file:
    while True:
        if skipped != "":
            #print("skipped:", skipped)
            raw_line = skipped
            line = raw_line.strip().split(" ")
        else:
            raw_line = file.readline()
            if not raw_line:
                break
            line = raw_line.strip().split(" ")

        if line[0] == "$": # command
            skipped = ""
            #print("comm:", line)
            command = line
            if line[1] == "cd": # change directory
                if line[2] == "..": # moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
                    #print(".. to",current.parent)
                    current = current.parent
                if line[2] == "/": # switches the current directory to the outermost directory, /.
                    current = root
                else:  # moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
                    #print("cd",line[2])
                    for child in current.children:
                        if child.name == line[2]:
                            current = child

            if line[1] == "ls": # list directory
                #print("ls",current.name)
                # read next line and continue reading data until the next command
                #last_line = line
                raw_line = file.readline() # get next line
                if not raw_line:
                        break
                line = raw_line.strip().split(" ")
                #print("line",line)

                while line[0] != "$": # while not a command
                    #print("data:",line)
                    if line[0] == "dir": # current directory contains a directory line[1]
                        #print("dir",line[1],"has parent",current.name)
                        new_dir = Directory(line[1])
                        new_dir.parent = current
                        current.children.append(new_dir)
                    else: #means that the current directory contains a file
                        #print("add",line[1],"to",current.name)
                        current.files.append((line[1],line[0]))
                        #current.size += int(line[0])
                        #print("file",line)
                    
                    # get next line
                    #last_line = line
                    raw_line = file.readline()
                    if not raw_line:
                        break
                    line = raw_line.strip().split(" ")

                #print("skipped command:", raw_line)
                skipped = raw_line

        last_line = line            
file.close()
### end of reading file ###

calculateSize(root)

for directory in directories:
    print(directory.name, directory.size)

print("--")

sum = 0
for directory in directories:
    if directory.size <= 100000:
        print(directory.name, directory.size)
        sum += directory.size

print("--")
print(sum)