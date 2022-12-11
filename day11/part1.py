import sys, fileinput, re, heapq

filename = sys.argv[1]

import re

monkeys = []
inspect_count = [] # index = monkey number, value = number of items inspected
rounds = 20

with open(filename) as file:
    line = ""
    while True:
        monkey_ = []
        starting_ = []
        operation_ = []
        test_operation_ = []
        true_condition_ = []
        false_condition_ = []

        try:
            # Monkey Number
            line = file.readline().strip().split(":")
            monkey_ = re.findall(r'\d+', line[0].strip())

            # Starting items
            line = file.readline().strip().split(":")
            starting_ = re.findall(r'\d+', line[1].strip())

            # Operation
            line = file.readline().strip().split(":")
            operation_ = [line[1].strip()]

            # Test Operation
            line = file.readline().strip().split(":")
            test_operation_ = re.findall(r'\d+', line[1].strip())

            # True Condition
            line = file.readline().strip().split(":")
            true_condition_ = re.findall(r'\d+', line[1].strip())

            # False Condition
            line = file.readline().strip().split(":")
            false_condition_ = re.findall(r'\d+', line[1].strip())

            # Consume New Line
            line = file.readline().strip().split(":")

            #print(monkey_, starting_, operation_, test_operation_, true_condition_, false_condition_)

            # store a variable for the inspected count
            inspect_count.append(0)
            # add monkey to monkey list
            monkeys.insert(int(monkey_[0]), [starting_, operation_, test_operation_, true_condition_, false_condition_])

        except:
            break

file.close()

# solution
for _ in range(0, rounds):
    print("--- Round ", _ + 1, " ---")
    for monkey in monkeys:
        print("Monkey ", monkeys.index(monkey), ":")
        for item in monkey[0]:
            print("  Monkey inspects an item with a worry level of ", item, ".", sep="")
            # update inspect count
            inspect_count[monkeys.index(monkey)] = inspect_count[monkeys.index(monkey)] + 1

            # perform operation
            worry = int(item)

            op = monkey[1][0]
            eq = op.find("=")
            op = op[eq + 1:]
            worry = eval(op, {'old': int(item)})

            # after operation

            # worry level *divided by 3* and rounded down to nearest integer
            worry = worry // 3
            print("    Monkey gets bored with item. Worry level is divided by 3 to ", worry, ".", sep="")

            # before test operation

            # test operation

            throw_to = -1

            if worry % int(monkey[2][0]) == 0:
                # true condition
                print("    Current worry level is divisible by ", monkey[2][0], ".", sep="")
                print("    Item with worry level ", worry, " is thrown to monkey ", monkey[3][0], ".", sep="")
                throw_to = int(monkey[3][0])
            else:
                # false condition
                print("    Current worry level is not divisible by ", monkey[2][0], ".", sep="")
                print("    Item with worry level ", worry, " is thrown to monkey ", monkey[4][0], ".", sep="")
                throw_to = int(monkey[4][0])

            # TODO : perform throw
            #monkey[0].pop(monkey[0].index(item)) # remove item from current monkey
            monkeys[throw_to][0].append(worry) # add item to next monkey
        monkey[0] = [] # has thrown all items
    
    print("\nAfter round " , _ + 1 , ", the monkeys are holding items with these worry levels:")
    for monkey in monkeys:
        print("Monkey ", monkeys.index(monkey), ": ", monkey[0], sep="")

# print inspect count
print("\nAfter ", rounds, " rounds, the monkeys have inspected ", inspect_count, " items.", sep="", end="\n\n")
largest_integers = heapq.nlargest(2, inspect_count)

monkey_business = largest_integers[0] * largest_integers[1]

print("The monkeys have done ", monkey_business, " units of monkey business.", sep="")