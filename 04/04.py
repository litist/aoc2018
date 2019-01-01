import numpy as np
import re
import matplotlib.pyplot as plt


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

with open('04/input.txt') as f:
#with open('04/input_test') as f:
    read_data = f.read()
f.closed

# import guard shifts to sort them
shift = []

# [1518-06-03 00:16]
valid = re.compile(r"\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\](.*)")#[a2-9tjqk]{5}$")
for claim in read_data.rstrip().split('\n'):
    res = valid.search(claim)
    #print(displaymatch(valid.search(claim)))  # Valid.
    if(None == claim):
        print('Failed to match on ', claim)
        break

    # convert date into a global time to make it easy to sort it
    globaltime = int(res.groups()[0])*12*31*24*60+ \
                    int(res.groups()[1])*31*24*60+ \
                       int(res.groups()[2])*24*60+ \
                          int(res.groups()[3])*60+ \
                              int(res.groups()[4])


    shift.append((globaltime, int(res.groups()[0]), int(res.groups()[1]), int(res.groups()[2]), int(res.groups()[3]), int(res.groups()[4]), res.groups()[5].lstrip()))
    #fabric[res.groups()[1]:(res.groups()[1] + res.groups()[3] - 1), res.groups()[2]:(res.groups()[2] + res.groups()[4] - 1)] += 1
    #fabric[int(res.groups()[1]):(int(res.groups()[1]) + int(res.groups()[3])), int(res.groups()[2]):(int(res.groups()[2]) + int(res.groups()[4]))] += 1

    #print(shift[-1])

# sort after our global time
b = sorted(shift, key = lambda x : x[0])

f = open("04/input_sorted.txt", "w")
for a in b:
    f.write('{} {}\n'.format(a[5], a[6]))
f.close

# dictionrary to save sleep for each guard
guards = {}


current_guard = -1
sleep_minute = -1

valid = re.compile(r"Guard #(\d+) begins shift")
sleep = re.compile(r"falls asleep")
awake = re.compile(r"wakes up")

# parse sorted shifts and save into guards dict
for a in b:
    res = valid.search(a[6])
    #print(displaymatch(valid.search(claim)))  # Valid.
    if(None != res):
        current_guard = int(res.groups()[0])

        # only add if not in list
        if not current_guard in guards:
            guards[current_guard] = np.zeros(60)
        
        continue


    res = sleep.search(a[6])
    #print(displaymatch(valid.search(claim)))  # Valid.
    if(None != res):
        sleep_minute = int(a[5])
        continue

    res = awake.search(a[6])
    #print(displaymatch(valid.search(claim)))  # Valid.
    if(None != res):
        guards[current_guard][sleep_minute:int(a[5])] += 1
        if current_guard == 3361:
            print(sleep_minute, '->',int(a[5]), '::', guards[current_guard])
        sleep_minute = -1


max_sleep_min = -1
max_sleep_guard = -1
for g in guards:
    if np.sum(guards[g]) > max_sleep_min:
        max_sleep_min = np.sum(guards[g])
        max_sleep_guard = g
        print('Guard {} sleeps for {}'.format(g, max_sleep_min))

max_sleep_pos = np.argmax(guards[max_sleep_guard])
print('Guard maxarg is {} from \n{}'.format(max_sleep_pos, guards[max_sleep_guard]))

#110913 too high
print('Solution 1: ', max_sleep_guard*max_sleep_pos)



max_sleep_min = -1
max_sleep_guard = -1
for g in guards:
    if np.max(guards[g]) > max_sleep_min:
        max_sleep_min = np.max(guards[g])
        max_sleep_pos = np.argmax(guards[g])
        max_sleep_guard = g
        print('Guard {} sleeps for {} @ {}'.format(g, max_sleep_min, max_sleep_pos))

print('Solution 2: ', max_sleep_guard*max_sleep_pos)
