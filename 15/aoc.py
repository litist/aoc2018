import numpy as np
import re
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation



#with open('15/input.txt') as fin:
with open('15/input_test.txt') as fin:
    read_data = fin.read()
fin.closed

def printArena(track_, U_):
    ptrack = np.copy(track_)

    for u in U_:
        ptrack[u[0], u[1]] = ord(u[2])

    for y in range(0,len(ptrack)):
        for x in range(0,len(ptrack)):
            print('{}'.format(chr(ptrack[y,x])), end='')
        for u in U_:
            if y == u[0]:
                print(' ', u[2], u[4], ' | ', end='')
        print('')



#track = np.empty((150,150), dtype=np.character)
arena = np.zeros((33,33), dtype=np.uint)
arena = np.zeros((9,9), dtype=np.uint)
#track = np.zeros((13,13), dtype=np.uint8)

U = []
G = []
E = []


start_HP = 200

row_c = 0
for row in read_data.rstrip().split('\n'):

    col_c = 0
    for col in list(row):
        if col == 'G':
            G.append([row_c, col_c])
            U.append([row_c, col_c, 'G', 0, start_HP])
            arena[row_c, col_c] = ord('.')
        elif col == 'E':
            E.append([row_c, col_c])
            U.append([row_c, col_c, 'E', 0, start_HP])
            arena[row_c, col_c] = ord('.')
        else:
            arena[row_c, col_c] = ord(col)
        
        col_c += 1

    row_c += 1



printArena(arena, [])

BORDER = 1234567
STARTVAL = 8888

def calcDistance(arena_, unit, enemys, friends):

    dist = np.zeros(np.shape(arena_), dtype=np.int)

    for y in range(len(dist)):
        for x in range(len(dist)):
            if arena_[y,x] == ord('#'):
                dist[y,x] = BORDER
            else:
                dist[y,x] = STARTVAL
    
    # add all friends as blocking elements
    for f in friends:
        dist[f[0], f[1]] = BORDER

    # set distance for current unit as starting point
    dist[unit[0], unit[1]] = 0


    running = True
    while running:
        running = False

        for y in range(1,len(dist)-1):
            for x in range(1,len(dist)-1):
                # check if location is valid
                if BORDER == dist[y,x]:
                    continue

                mn = np.min([dist[y-1,x], dist[y+1,x], dist[y,x-1], dist[y,x+1]])
                if (mn != STARTVAL) and (mn != BORDER) and((mn+1) < dist[y,x]):
                    dist[y,x] = mn + 1
                    running = True

#    for y in range(0,len(dist)):
#        for x in range(0,len(dist)):
#            if dist[y,x] == BORDER:
#                print('#', end='')
#            elif dist[y,x] == STARTVAL:
#                print(' ', end='')
#            else:
#                print(dist[y,x], end='')
#        print('')

    # select a target with lowest distance
    # we assume the G/E are sorted in readin order
    target = []
    target_dist = STARTVAL
    for t in enemys:
        if dist[t[0], t[1]] < target_dist:
            target = t
            target_dist = dist[t[0], t[1]]
            #print('Found ', t, ' with dist: ', target_dist)

    if len(target)==0:
        #print(unit, ': no Enenmy to attack in range')
        return unit

    if target_dist == 1:
        #print(unit, 'F2F we do not move')
        return unit


    # retrieve shortest path to the target which uses reading order first
    path = [target]
    while target_dist > 0:
        # first check above
        if dist[path[-1][0]-1, path[-1][1]] == target_dist - 1:
            path.append([path[-1][0]-1, path[-1][1]])
            target_dist -= 1
            continue
        # check left
        if dist[path[-1][0], path[-1][1]-1] == target_dist - 1:
            path.append([path[-1][0], path[-1][1]-1])
            target_dist -= 1
            continue
        # right
        if dist[path[-1][0], path[-1][1]+1] == target_dist - 1:
            path.append([path[-1][0], path[-1][1]+1])
            target_dist -= 1
            continue
        # down
        if dist[path[-1][0]+1, path[-1][1]] == target_dist - 1:
            path.append([path[-1][0]+1, path[-1][1]])
            target_dist -= 1
            continue

    # print('Reverse Path is: ', path)
    return path[-2]


def combat(unit, U_):
    attack_space = [None, None, None, None]
    for u in U_:
        # search above
        if u[2] != unit[2] and u[1] == unit[1] and u[0] == unit[0] - 1:
            #print(unit, ': found enemy to attack: ', u)
            attack_space[0] = u
        # left
        if u[2] != unit[2] and u[1] == unit[1]-1 and u[0] == unit[0]:
            #print(unit, ': found enemy to attack: ', u)
            attack_space[1] = u
        if u[2] != unit[2] and u[1] == unit[1]+1 and u[0] == unit[0]:
            #print(unit, ': found enemy to attack: ', u)
            attack_space[2] = u
        if u[2] != unit[2] and u[1] == unit[1] and u[0] == unit[0]+1:
            #print(unit, ': found enemy to attack: ', u)
            attack_space[3] = u

    # select appropriate target from searchspace
    #print(unit, ' Attackvector: ', attack_space)

    attack_on = None
    for a in attack_space:
        if a != None:
            if attack_on == None:
                attack_on = a
            elif attack_on[4] > a[4]:
                attack_on = a

    # do the attack
    if attack_on != None: 
        attack_on[4] -= 3


for round in range(0,150):

    for u in U:
        # ignore units which are dead
        if u[4] <= 0:
            continue

        pos = calcDistance(arena, u, list(filter(lambda x:x[2]!=u[2] and x[4]>0, U)), list(filter(lambda x:x[2]==u[2] and x[4]>0, U)))
        u[0] = pos[0]
        u[1] = pos[1]

        combat(u, list(filter(lambda x:x[4]>0, U)))

    # remove dead units
    U = list(filter(lambda x:x[4]>0, U))

    # sort E and G before next round
    for u in U:
        u[3] = u[0]*len(arena) + u[1]
    
    U = sorted(U, key=lambda x:x[3])

    # print
    print('Round ', round)
    printArena(arena, U)

    if( len(list(filter(lambda x:x[2]=='G', U)))==0 or len(list(filter(lambda x:x[2]=='E', U)))==0):
        print('Enemy defeated.')
        sum = 0
        for u in U:
            sum += u[4]
        # 220320 is too low
        print('Solution:', (round)*sum)
        quit()










quit()
