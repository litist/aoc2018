import numpy as np
import re
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation



def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())


with open('17/input.txt') as fin:
#with open('17/input_test.txt') as fin:
    read_data = fin.read()
fin.closed


clay = []

regex = re.compile(r"([xy])=(\d+), ([xy])=(\d+)..(\d+)")

for d in read_data.rstrip().split('\n'):
    # before register set
    res = regex.search(d)
    #print(d, displaymatch(regex.search(d)))  # Valid.
    if(None == res):
        print('Failed to match on ', d)
    #data_sets[-1].append([int(x) for x in res.groups()])

    if res.groups()[0] == 'x':
        for y in range(int(res.groups()[3]), int(res.groups()[4])+1):
            clay.append((y, int(res.groups()[1])))
    else:
        for x in range(int(res.groups()[3]), int(res.groups()[4])+1):
            clay.append((int(res.groups()[1]), x))

# print(clay)

min_x = min([x[1] for x in clay])
max_x = max([x[1] for x in clay])

min_y = min([y[0] for y in clay])
max_y = max([y[0] for y in clay])



ground = [['.' for _ in range(min_x-1, max_x+2)] for _ in range(0, max_y + 3)]

for c in clay:
    ground[c[0]][c[1] - min_x + 1] = '#'


def g2i(g):
    gp = np.zeros((len(ground), len(ground[0])))

    for c in range(len(ground)):
        for r in range(len(ground[0])):
            if ground[c][r] == '#':
                gp[c,r] = 1

            if ground[c][r] == '|':
                gp[c,r] = 2
            if ground[c][r] == '~':
                gp[c,r] = 3
            if ground[c][r] == '+':
                gp[c,r] = 4

    X = plt.figure(figsize=(len(ground[0])/100, len(ground)/100), dpi=100)
    plt.imshow(gp, interpolation='none', aspect='equal')

    plt.savefig('17/water.png', dpi=400)
    plt.show()

quit


def check_source(s_p):

    s = [s_p[0], s_p[1]]

    if ground[s[0]+1][s[1]] in ['#', '~']:
        # need to put parent in charge of resolving this
        # print('source is on water level')
        return [s_p[2]]

    while ground[s[0]+1][s[1]] not in ['#', '~']:
        # we are still falling
        s[0] += 1
        ground[s[0]][s[1]] = '|'

        if s[0] + 1 == len(ground):
            print('Reached end of scan with position:', s, ' for source ', s)
            return []

    
#    elif ground[s[0]-1][s[1]] == '#':
        # we hit soil

    new_s = []

    # check if ther is a wall on the left side
    for lx in range(s[1], 0-1, -1):
        if ground[s[0]][lx] == '#':
            # we hit a wall
            break

        if ground[s[0]+1][lx] in ['#', '~']:
            # go on, mark as wet
            ground[s[0]][lx] = '|'
            continue

        if ground[s[0]+1][lx] in ['.', '+', '|']:
            # water can drop. add new source
            ground[s[0]][lx] = '+'
            new_s.append([s[0],lx, s_p])
            #print('Add new source on left side', new_s[-1])
            break


    # check if there is a wall on the right side
    for lx in range(s[1], len(ground[0]), 1):
        if ground[s[0]][lx] == '#':
            # we hit a wall
            break

        if ground[s[0]+1][lx] in ['#', '~']:
            # go on, mark as wet
            ground[s[0]][lx] = '|'
            continue

        if ground[s[0]+1][lx]  in ['.', '+', '|']:
            # water can drop. add new source
            ground[s[0]][lx] = '+'
            new_s.append([s[0], lx, s_p])
            #print('Add new source on right side', new_s[-1])
            break

    if len(new_s) == 0:
        # both sides are closed, we need to put water on both sides
        for lx in range(s[1], len(ground[0]), 1):
            if ground[s[0]][lx] == '#':
                break
            else:
                ground[s[0]][lx] = '~'

        for lx in range(s[1], 0-1, -1):
            if ground[s[0]][lx] == '#':
                break
            else:
                ground[s[0]][lx] = '~'

        return [s_p]
    
    return new_s



def getWet():
    wet = 0
    for c in range(min_y, max_y+1):
        for r in range(0, max_x - min_x + 2):
            if ground[c][r] in ['~', '|', '+']:
                wet += 1

    return wet

def getStillWater():
    wet = 0
    for c in range(min_y, max_y+1):
        for r in range(0, max_x - min_x + 2):
            if ground[c][r] in ['~']:
                wet += 1

    return wet




# start by setting spring
ground[0][500-min_x+1] = '+'
glob_s = [[0, 500 - min_x + 1]]

while(len(glob_s)>0):
    # print('glob_s:', glob_s)
    glob_s = sorted(glob_s, key=lambda x:x[0])
    ret = check_source(glob_s.pop(0))
    # print('check_source returned: ', ret)
    for a in ret:
        for s in glob_s:
            if s[0] == a[0] and s[1] == a[1]:
                # already in istr, do not add
                break
        else:
            glob_s.append(a)

# 40867 wrong
print('Solution: ', getWet())
print('Solution 2: ', getStillWater())
g2i(ground)
