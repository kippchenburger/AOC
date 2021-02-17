# https://adventofcode.com/2020/day/11
# https://www.reddit.com/r/adventofcode/comments/k52psu/2020_day_10_solutions/

data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

debug = True
printit = True
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print(name, ": ", subject)

print("\n----------------------------------")   # reading file

file = "AOC20/data_aoc20_9.txt"
if not debug:
    with open(file) as f:
        data = f.read()
data = [[t for t in s] for s in data.split("\n")]

for i in data:
    pp(i)
maxY = len(data)
maxX = len(data[0])

def checkseat(x, y, seats):
    adjacent_seats = []
    # for seat 1,1 -> 0,0 0,1 0,2
    #                 1,0     1,2
    #                 2,0 2,1 2,2
    limX = [-1,1]
    limY = [-1,1]
    if x == 0:
        limX = [0,1]
    if x == maxX:
        limX = [-1,0]
    if y == 0:
        limY = [0,1]
    if y == maxY:
        limY = [-1,0]
    for y in seats[limY[0]:limY[1]+1]:
        for x in seats[limX[0]:limX[1]+1]:
            pass


