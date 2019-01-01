import numpy as np
import re
import matplotlib.pyplot as plt


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

with open('06/input.txt') as f:
    read_data = f.read()
f.closed


coords = []

valid = re.compile(r"(\d+), (\d+)")
for claim in read_data.rstrip().split('\n'):
    res = valid.search(claim)
    print(displaymatch(valid.search(claim)))  # Valid.
    if(None == claim):
        print('Failed to match on ', claim)
        break
    coords.append((int(res.groups()[0]), int(res.groups()[1]), len(coords)+1))


    #fabric[res.groups()[1]:(res.groups()[1] + res.groups()[3] - 1), res.groups()[2]:(res.groups()[2] + res.groups()[4] - 1)] += 1
    #fabric[int(res.groups()[1]):(int(res.groups()[1]) + int(res.groups()[3])), int(res.groups()[2]):(int(res.groups()[2]) + int(res.groups()[4]))] += 1

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


        # add all manhattan distances
        for coord in coords:
            manhattan[(x,y)] += np.abs(coord[0] - x) + np.abs(coord[1] - y)


print('Solution 2:', np.sum(manhattan<10000))

plt.subplot(121)
plt.imshow(manhattan)

for coord in coords:

    plt.text(coord[1], coord[0], '.{}'.format(coord[2]))


plt.subplot(122)
plt.imshow(manhattan<10000)

plt.show()

quit()
