import numpy as np
import re
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation


N_RECIPIES = 540561



recipies = [3, 7, 1, 0, 1, 0]

elves_one = 4
elves_two = 3
 
rec_l = list(map(lambda x:int(x), list(str(N_RECIPIES))))

while True:

    # make new recipies
    s = recipies[elves_one] + recipies[elves_two]
    #print(elves_one, elves_two, '|', recipies, ' add', s)
    for digit in list(str(s)):
        recipies.append(int(digit))
        
        #pos = len(recipies) - len(list(str(N_RECIPIES)))
        #if ''.join(map(lambda x:str(x), recipies[pos:(pos+len(list(str(N_RECIPIES))))])) == str(N_RECIPIES):
        if recipies[-6:] == rec_l:
            # 20254833
            print('Found it')




    
    # change current recipies
    elves_one = np.mod(elves_one + recipies[elves_one]+1, len(recipies))
    elves_two = np.mod(elves_two + recipies[elves_two]+1, len(recipies))





recipies = [3, 7]

elves_one = 0
elves_two = 1

while len(recipies) < N_RECIPIES+10:

    # make new recipies
    s = recipies[elves_one] + recipies[elves_two]
    #print(elves_one, elves_two, '|', recipies, ' add', s)
    for digit in list(str(s)):
        recipies.append(int(digit))
    
    # change current recipies
    elves_one = np.mod(elves_one + recipies[elves_one]+1, len(recipies))
    elves_two = np.mod(elves_two + recipies[elves_two]+1, len(recipies))

#print(recipies)

#print(recipies[9:(9+10)])

# After 18 recipes, the scores of the next ten would be 9251071085.
print(''.join(map(lambda x:str(x), recipies[18:(18+10)])))

# After 2018 recipes, the scores of the next ten would be 5941429882.
print(''.join(map(lambda x:str(x), recipies[2018:(2018+10)])))

print(''.join(map(lambda x:str(x), recipies[N_RECIPIES:(N_RECIPIES+10)])))


#    while s > 0:



