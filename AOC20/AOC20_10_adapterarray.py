# https://adventofcode.com/2020/day/10
# https://www.reddit.com/r/adventofcode/comments/k52psu/2020_day_10_solutions/

# In addition, your device has a built-in joltage adapter rated for 3 jolts higher than 
# the highest-rated adapter in your bag. (If your adapter list were 3, 9, and 6, your device's 
# built-in adapter would be rated for 12 jolts.)
# Treat the charging outlet near your seat as having an effective joltage rating of 0.

data = """16
10
15
5
1
11
7
19
6
12
4"""

# With these adapters, your device's built-in joltage adapter would be rated for 
# 19 + 3 = 22 jolts, 3 higher than the highest-rated adapter.

# In this example, when using every adapter, there are 7 differences of 1 jolt and 5 
# differences of 3 jolts.

# Find a chain that uses all of your adapters to connect the charging outlet to 
# your device's built-in adapter and count the joltage differences between the 
# charging outlet, the adapters, and your device. 
# What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

# part 2
# 

debug = False
printit = True
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "AOC20/aoc20_10_data2.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [int(s) for s in data.split("\n")]

data.append(0)
data = sorted(data)
device_joltage = data[-1] + 3
data.append(device_joltage)
pp(data)

ones, twos, threes = [], [], []
pp(len(data[1:]), "length of data")

for i in range(len(data[1:])):
    current = data[i+1]
    #pp(current, "current")
    previous = data[i]
    #pp(previous, "previous")
    difference = current - previous
    #pp(difference, "difference")
    if difference == 1:
        ones.append(current)
    elif difference == 2:
        twos.append(current)
    elif difference == 3:
        threes.append(current)
    else:
        print("somethings wrong")
        break
        


pp(len(ones), "number of 1 jolt differences", True)
pp(len(twos), "number of 2 jolt differences", True)
pp(len(threes), "number of 3 jolt differences", True)

pp(len(ones)*len(threes), "product of numbers of 1 and 3 jolt differences", True)

skippables = []
tripleones, doubleones, onetwos, twoones = 0,0,0,0
permutations = 1
index = 1
while index < len(data[1:-1]):
#for index, n in enumerate(data[1:-1], start=1):
    n = data[i]
    if n in threes:
        pass
        #skippables += 0
    elif n in twos:
        if data[index+1] in ones:
            skippables.append(n)
            twoones+=1
            permutations *= 2
    elif n in ones:
        if data[index+1] in ones:
            doubleones+=1
            skippables.append(n)
            permutations *= 2
            if data[index+2] in ones:
                tripleones+=1
                skippables.append(n)
            #    permutations *= 2
        elif data[index+1] in twos:
                skippables.append(n)
                twoones+=1
                permutations *= 2

#skippables = list(dict.fromkeys(skippables))
#permutations = 2 ** len(skippables)
pp(doubleones, "double ones")
pp(tripleones, "triple ones")
pp(onetwos, "one twos")
pp(twoones, "two ones")
pp(skippables, "skippables")
pp(len(skippables), "number of skippables")
pp(permutations, "permutations")

helper = 19208
helper = 2**2
pp(helper, "helper")

# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
# (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
        
# 8 -- 3
# 19208 -- 15

# 2**13