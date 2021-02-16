# https://adventofcode.com/2020/day/9
# https://www.reddit.com/r/adventofcode/comments/k52psu/2020_day_09_solutions/

# XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive 
# should be the sum of any two of the 25 immediately previous numbers. 
# The two numbers will have different values, and there might be more than one such pair.

data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

# In this example, after the 5-number preamble, almost every number is the sum of two 
# of the previous 5 numbers; the only number that does not follow this rule is 127.

# The first step of attacking the weakness in the XMAS data is to find the first number 
# in the list (after the preamble) which is not the sum of two of the 25 numbers before it. 
# What is the first number that does not have this property?


debug = True
printit = False
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "AOC20/aoc20_9_data.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [int(s) for s in data.split("\n")]

preamble = 25
if debug:
    preamble = 5

pp(data)
