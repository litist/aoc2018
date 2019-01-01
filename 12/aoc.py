import numpy as np
import re
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

with open('12/input.txt') as fin:
#with open('12/input_test.txt') as fin:
    read_data = fin.read()
fin.closed


# initial state: ###.......##....#.#.#..###.##..##.....#....#.#.....##.###...###.#...###.###.#.###...#.####.##.#....#

pots = []
for c in list('###.......##....#.#.#..###.##..##.....#....#.#.....##.###...###.#...###.###.#.###...#.####.##.#....#'):
#for c in list('#..#.#..##......###...###'):
    if c == '#':
        pots.append(1)
    else:
        pots.append(0)

print(pots)


rules = {}
for i in range(0,32):
    rules[i] = 0


# #.### => #
valid = re.compile(r"([#.]{5}) => ([#.])")
for claim in read_data.rstrip().split('\n'):
    res = valid.search(claim)
    #print(claim, displaymatch(valid.search(claim)))  # Valid.
    if(None == res):
        print('Failed to match on ', claim)
        break

    # interpret as interger and save into dict
    rule = list(res.groups()[0])
    idx = 0
    for i in range(0, 5):
        if rule[i] == '#':
            idx += np.power(2, i)
    
    if res.groups()[1] == '#':
        rules[idx] = 1
    else:
        rules[idx] = 0

print(rules)

N_GEN = 20



# each generation extends it by 2 pots to each side
gen = np.zeros((N_GEN*2*2+len(pots)))
gen[N_GEN*2:(N_GEN*2+len(pots))] = pots

for generation in range(1, N_GEN+1):
    new_gen = np.zeros(len(gen))
    for l in range(2, len(gen)-2):
        # convert to index
        idx = 0
        for i in range(0, 5):
            if gen[l+i-2] == 1:
                idx += np.power(2, i)

        new_gen[l] = rules[idx]
    gen = new_gen

    for c in gen:
        print(int(c), end='')
    print('')


print('Solution 1: ', np.sum(np.multiply(gen, np.array(range(0,len(gen)))-N_GEN*2)))


N_GEN = 142
sol_142 = []
for i in list('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'):
    sol_142.append(int(i))
print('Solution 2 test: ', np.sum(np.multiply(sol_142, np.array(range(0,len(sol_142)))-N_GEN*2)))

# after ~130 generation we have a pattern of 00000011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110000
# which shifts by one to the right after each next generation
# there 26 x 11000
# i have one example solution for generation 142 it is 9256
def solve_pots(generation):
    # mean reduces sum -> 3328
    gen_sum = 0
    for i in range(0, 26):
        gen_sum += 1+i*5 + 2 + i*5
    # the 28 has we acquired by using one solution
    return (generation-28)*2*26 + gen_sum

print(solve_pots(142))

# 2 600 000 001 872
print(solve_pots(50000000000))

