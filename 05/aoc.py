import numpy as np
import re
import matplotlib.pyplot as plt


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

with open('05/input.txt') as f:
#with open('04/input_test') as f:
    read_data = f.read()
f.closed

units = list(read_data.rstrip())

cur_pos = 1

while(cur_pos < len(units)):
    if(cur_pos<1):
        cur_pos = 1
    d = ord(units[cur_pos]) - ord(units[cur_pos-1])
    if(d == 32 or d == -32):
        #print('found units: @ {} {}'.format(cur_pos, units[cur_pos-1], units[cur_pos]))
        units.pop(cur_pos)
        units.pop(cur_pos-1)
        cur_pos -= 1
    else:
        cur_pos += 1

print('Solution 1: ', len(units))


for pu in range(ord('A'), ord('Z')+1):

    units = list(read_data.rstrip())

    # remove units of one type
    cur_pos = 0
    while(cur_pos < len(units)):
        if(ord(units[cur_pos])==pu or ord(units[cur_pos])==(pu+32)):
            units.pop(cur_pos)
        else:
            cur_pos += 1
        
    cur_pos = 1
    while(cur_pos < len(units)):
        if(cur_pos<1):
            cur_pos = 1
        d = ord(units[cur_pos]) - ord(units[cur_pos-1])
        if(d == 32 or d == -32):
            #print('found units: @ {} {}'.format(cur_pos, units[cur_pos-1], units[cur_pos]))
            units.pop(cur_pos)
            units.pop(cur_pos-1)
            cur_pos -= 1
        else:
            cur_pos += 1

    print('Solution 2: ', len(units))    
