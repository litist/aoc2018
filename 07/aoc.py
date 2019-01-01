import numpy as np
import re
import matplotlib.pyplot as plt


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

#with open('07/input.txt') as f:
with open('07/input_test.txt') as f:
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



    #fabric[res.groups()[1]:(res.groups()[1] + res.groups()[3] - 1), res.groups()[2]:(res.groups()[2] + res.groups()[4] - 1)] += 1
    #fabric[int(res.groups()[1]):(int(res.groups()[1]) + int(res.groups()[3])), int(res.groups()[2]):(int(res.groups()[2]) + int(res.groups()[4]))] += 1

print(depends)


for step in range(ord('A'), ord('Z') + 1):
    if chr(step) in depends:
        print(chr(step), depends[chr(step)])

order = []

while len(depends) > 0:
    for step in range(ord('A'), ord('Z') + 1):
        if chr(step) in depends and len(depends[chr(step)]) == 0:
            # choose this step to be done
            print(chr(step), ' selected')
            order.append(chr(step))

            # remove from all depends lists
            for st in range(ord('A'), ord('Z') + 1):
                if chr(st) in depends and chr(step) in depends[chr(st)]:
                    depends[chr(st)].remove(chr(step))
                
                    print('Remove from ', chr(st) ,' list ', depends[chr(st)])
            
            depends.pop(chr(step))
            break


# CHILNRYFKMOQXZGPUVWABDSJET
print(''.join(order))



workers = []

while len(depends) > 0:
    for step in range(ord('A'), ord('Z') + 1):
        if chr(step) in depends and len(depends[chr(step)]) == 0:
            # choose this step to be done
            print(chr(step), ' selected')

            workers.append((chr(step), 60+step))
            
            depends.pop(chr(step))
            break
    
    else:
        # do worker
        workers = sorted(workers, key=lambda x : x[0])

        # reduce time for all wokers
        for w in range(0, len(workers)):
            workers[w] = (workers[w][1], workers[w][0] - workers[0][0])

        # worker is done with job
        job = workers[0][0]
        order.append(chr(job))

        # remove worker
        workers.remove(0)

        # remove from all depends lists
        for st in range(ord('A'), ord('Z') + 1):
            if chr(st) in depends and chr(step) in depends[chr(st)]:
                depends[chr(st)].remove(chr(step))
            
                print('Remove from ', chr(st) ,' list ', depends[chr(st)])






quit

print(coords)

max_x = max(coords, key=lambda x:x[0])
max_y = max(coords, key=lambda x:x[1])


manhattan = np.zeros([400,400])

c = 1
for coord in coords:
    manhattan[coord[0:2]] = c
    c+=1


for x in range(0,400):
    for y in range(0, 400):

        min_md = 400
        min_coord = -1
        # check which coords is nearest to this
        for coord in coords:
            md = np.abs(coord[0] - x) + np.abs(coord[1] - y)

            if(md == min_md):
                min_md = md
                min_coord = -1

            if(md < min_md):
                min_md = md
                min_coord = coord[2]



        if min_coord != -1:
            manhattan[(x,y)] = min_coord


A = []
for coord in coords:
    s = np.sum(np.reshape(manhattan, -1) == coord[2])
    A.append((s, coord[2]))
    

for a in sorted(A, key = lambda xx : xx[0]):
    print('Area for {} is {}'.format(a[1], a[0]))
# Area for 9 is 3907

#plt.subplot(121)
plt.imshow(manhattan)

for coord in coords:

    plt.text(coord[1], coord[0], '.{}'.format(coord[2]))

plt.show()

quit()

print(fabric)

# 101341 wrong
print(np.sum(np.reshape(fabric, -1) > 1))




valid = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")#[a2-9tjqk]{5}$")
for claim in read_data.rstrip().split('\n'):
    res = valid.search(claim)
    #print(displaymatch(valid.search(claim)))  # Valid.
    if(None == claim):
        print('Failed to match on ', claim)
        break

    #fabric[res.groups()[1]:(res.groups()[1] + res.groups()[3] - 1), res.groups()[2]:(res.groups()[2] + res.groups()[4] - 1)] += 1
    s = np.sum(fabric[int(res.groups()[1]):(int(res.groups()[1]) + int(res.groups()[3])), int(res.groups()[2]):(int(res.groups()[2]) + int(res.groups()[4]))])
    #print(s)
    if(s == int(res.groups()[3])*int(res.groups()[4])):
        print('Found solutio at id', int(res.groups()[0]))


plt.subplot(121)
plt.imshow(fabric)

plt.subplot(122)
plt.imshow(fabric == 1)
plt.show()

fabric > 1


