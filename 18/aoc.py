import numpy as np
import re
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation


with open('18/input.txt') as fin:
#with open('18/input_test.txt') as fin:
    read_data = fin.read()
fin.closed


print('input', len(read_data.rstrip().split('\n')), len(read_data.rstrip().split('\n')[0]))


# area is 50x50 but we add one on each side to make edge handling easier
area = np.zeros((2+len(read_data.rstrip().split('\n')), 2+len(read_data.rstrip().split('\n')[0])), dtype = np.int8)

c_idx = 0
for col in read_data.rstrip().split('\n'):
    c_idx += 1

    r_idx = 0
    for r in list(col):
        r_idx += 1

        if r == '.':
            area[c_idx][r_idx] = 1
        elif r == '|':
            # tree
            area[c_idx][r_idx] = 2
        elif r == '#':
            # lumberyard
            area[c_idx][r_idx] = 3
        else:
            print('Unknown type: ', r)

def printAcre(iarea):
    m = [' ', '.', '|', '#']
    for c in range(1, iarea.shape[0]-1):
        for r in range(1, iarea.shape[0]-1):
            print(m[iarea[c,r]], end='')
        print('')


def step(iarea):

    oarea = np.zeros(iarea.shape, dtype = np.int8)

    for c in range(1, iarea.shape[0]-1):
        for r in range(1, iarea.shape[0]-1):

            if iarea[r,c] == 1:
                # is open field
                if np.sum(iarea[(r-1):(r+2), (c-1):(c+2)] == 2) >= 3:
                    oarea[r,c] = 2
                else:
                    oarea[r,c] = 1
                # print(area[(r-1):(r+2), (c-1):(c+2)])
            elif iarea[r,c] == 2:
                # is open field
                if np.sum(iarea[(r-1):(r+2), (c-1):(c+2)] == 3) >= 3:
                    oarea[r,c] = 3
                else:
                    oarea[r,c] = 2
                # print(area[(r-1):(r+2), (c-1):(c+2)])
            elif iarea[r,c] == 3:
                # lumberyard
                # check for at least 2 lumber yards, as we count ourselves as well
                if np.sum(iarea[(r-1):(r+2), (c-1):(c+2)] == 3) >= 2 and np.sum(iarea[(r-1):(r+2), (c-1):(c+2)] == 2) >= 1:
                    oarea[r,c] = 3
                else:
                    oarea[r,c] = 1
                # print(area[(r-1):(r+2), (c-1):(c+2)])
            else:
                print('Malformed acre.', iarea[r,c])
    
    return oarea




# from 431 on we see a loop
# 431 and 466 are same -> period: 35

# 431+ X + N*35 = 1000000000
# X + N*35 = 1000000000 - 431
# X = (1000000000 - 431) % 35

for minute in range(431 + np.mod(1000000000-431, 35)):
    area = step(area)
    if minute == 9:
        print('Solution 1: ', np.sum(area==2)*np.sum(area==3) )
print('Solution 2: ', minute+1, np.sum(area==2)*np.sum(area==3))
#printAcre(area)

