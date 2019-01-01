import numpy as np
import re
import matplotlib.pyplot as plt


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

with open('07/input.txt') as f:
#with open('07/input_test.txt') as f:
    read_data = f.read()
f.closed


coords = []

depends = {}

valid = re.compile(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
for claim in read_data.rstrip().split('\n'):
    res = valid.search(claim)
    print(displaymatch(valid.search(claim)))  # Valid.
    if(None == claim):
        print('Failed to match on ', claim)
        break
    #coords.append((int(res.groups()[0]), int(res.groups()[1]), len(coords)+1))

    if res.groups()[1] not in depends:
        depends[res.groups()[1]] = list(res.groups()[0])
    else:
        depends[res.groups()[1]].append(res.groups()[0])

    if res.groups()[0] not in depends:
        depends[res.groups()[0]] = []

print(depends)


for step in range(ord('A'), ord('Z') + 1):
    if chr(step) in depends:
        print(chr(step), depends[chr(step)])

MAX_WORKERS = 5
MIN_PROCESSING_TIME = 60

order = []

workers = []

processing_time = 0

while len(depends) > 0 or len(workers)>0:
    for step in range(ord('A'), ord('Z') + 1):
        if chr(step) in depends and len(depends[chr(step)]) == 0 and len(workers)<MAX_WORKERS:
            # choose this step to be done
            print(chr(step), ' selected')

            workers.append((chr(step), MIN_PROCESSING_TIME+step-ord('A')+1))
            
            depends.pop(chr(step))
            break
    
    else:
        # do worker
        workers = sorted(workers, key=lambda x : x[1])

        # remove worker
        cw = workers.pop(0)

        processing_time += cw[1]
        # reduce time for all wokers
        for w in range(0, len(workers)):
            workers[w] = (workers[w][0], workers[w][1] - cw[1])

        # worker is done with job
        job = cw[0]
        order.append(job)

        print('Worker {} is done.'.format(cw))

        # remove from all depends lists
        for st in range(ord('A'), ord('Z') + 1):
            if chr(st) in depends and job in depends[chr(st)]:
                depends[chr(st)].remove(job)
            
                print('Remove from ', chr(st) ,' list ', depends[chr(st)])


# CINYHLFMRKOGQAXUZPVSBJWDET wrong
print(''.join(order))
print('Processing time: ', processing_time)
quit
