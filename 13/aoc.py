import numpy as np
import re
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation



with open('13/input.txt') as fin:
#with open('13/input_test.txt') as fin:
    read_data = fin.read()
fin.closed



#track = np.empty((150,150), dtype=np.character)
track = np.zeros((150,150), dtype=np.uint8)
#track = np.zeros((13,13), dtype=np.uint8)


row_c = 0
for row in read_data.rstrip().split('\n'):

    col_c = 0
    for col in list(row):
        track[row_c, col_c] = (ord(col))
        col_c += 1

    row_c += 1

# for x in range(0,len(track)):
#     for y in range(0,len(track)):
#         print('{}'.format(chr(track[x,y])), end='')
#     print('')

carts = []
# find all carts
for x in range(0,len(track)):
    for y in range(0,len(track)):
        if chr(track[y,x]) in ['>', '<']:
            carts.append([x,y, y*len(track)+x, chr(track[y,x]), 0, len(carts)])
            track[y,x] = ord('-')
        if chr(track[y,x]) in ['v', '^']:
            carts.append([x,y, y*len(track)+x, chr(track[y,x]), 0, len(carts)])
            track[y,x] = ord('|')

# for x in range(0,len(track)):
#     for y in range(0,len(track)):
#         print('{}'.format(chr(track[x,y])), end='')
#     print('')

print(carts)


def printTrack(track_, carts_):
    ptrack = np.copy(track_)

    for cart in carts_:
        ptrack[cart[1], cart[0]] = ord(cart[3])

    for y in range(0,len(ptrack)):
        for x in range(0,len(ptrack)):
            print('{}'.format(chr(ptrack[y,x])), end='')
        print('')
    

print('Init')
#printTrack(track, [])

tick = 0
#for tick in range(100):
while True:
    #tick += 1
    #print('Tick: ', tick)

    # sort carts
    carts = sorted(carts, key=lambda x:x[2])

    if(len(carts)==1):
        print('Only one cart is left', carts)
        # 111,136
        # 112,136
        # 111,136
        quit()


    collider = []
    for cart in carts:
        if cart[2] in collider:
            print('Cart in collider, skipping: ', cart)
            continue

        if chr(track[cart[1], cart[0]]) not in ['/', '\\', '-', '|', '+']:
            print('cart left track', cart, ' found: ', chr(track[cart[1], cart[0]]))

        # move cart to direction
        if cart[3] == '>':
            cart[0] += 1
        if cart[3] == '<':
            cart[0] -= 1
        if cart[3] == '^':
            cart[1] -= 1
        if cart[3] == 'v':
            cart[1] += 1

        # update position for sorting
        cart[2] = cart[1]*len(track)+cart[0]

        # check if we collide
        if np.sum(np.array([c[2] for c in carts]) == cart[2]) == 2:
            print(': Collision detected by: ', cart, ' for: ', list(filter(lambda x:x[2]==cart[2], carts)))
            print(carts)

            # printTrack(track, carts)
            collider.append(cart[2])
            # carts = list(filter(lambda x:x[2]!=cart[2], carts))
            continue


        # did we hit a intersection
        if track[cart[1], cart[0]] == ord('+'):
            if cart[3] == '>':
                if cart[4] == 0:
                    # turn left
                    cart[3] = '^'
                if cart[4] == 2:
                    #turn right
                    cart[3] = 'v'
                # going straight does not do need an action

            elif cart[3] == '<':
                if cart[4] == 0:
                    # turn left
                    cart[3] = 'v'
                if cart[4] == 2:
                    #turn right
                    cart[3] = '^'
                # going straight does not do need an action

            elif cart[3] == 'v':
                if cart[4] == 0:
                    # turn left
                    cart[3] = '>'
                if cart[4] == 2:
                    #turn right
                    cart[3] = '<'
                # going straight does not do need an action

            elif cart[3] == '^':
                if cart[4] == 0:
                    # turn left
                    cart[3] = '<'
                if cart[4] == 2:
                    #turn right
                    cart[3] = '>'
                # going straight does not do need an action

            # increase turn count
            cart[4] = np.mod(cart[4]+1, 3)

        # do we turn
        if track[cart[1], cart[0]] == ord('/'):
            if cart[3] == '>':
                cart[3] = '^'
            elif cart[3] == '^':
                cart[3] = '>'
            elif cart[3] == '<':
                cart[3] = 'v'
            elif cart[3] == 'v':
                cart[3] = '<'

        # do we turn
        if track[cart[1], cart[0]] == ord('\\'):
            if cart[3] == '>':
                cart[3] = 'v'
            elif cart[3] == '^':
                cart[3] = '<'
            elif cart[3] == '<':
                cart[3] = '^'
            elif cart[3] == 'v':
                cart[3] = '>'


        if(len(carts)==1):
            print('Only one cart is left', carts, ' current_cart: ', cart)

    carts = list(filter(lambda x:x[2] not in collider, carts))

    # printTrack(track, carts)







quit()


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


print('Solution: ', np.sum(np.multiply(gen, np.array(range(0,len(gen)))-N_GEN*2)))


N_GEN = 142
sol_142 = []
for i in list('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110001100011000110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'):
    sol_142.append(int(i))
print('Solution: ', np.sum(np.multiply(sol_142, np.array(range(0,len(sol_142)))-N_GEN*2)))

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

