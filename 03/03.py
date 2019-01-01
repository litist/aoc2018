import numpy as np
import re
import matplotlib.pyplot as plt


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

with open('03/input.txt') as f:
    read_data = f.read()
f.closed

fabric = np.zeros([1000,1000])


valid = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")#[a2-9tjqk]{5}$")
for claim in read_data.rstrip().split('\n'):
    res = valid.search(claim)
    #print(displaymatch(valid.search(claim)))  # Valid.
    if(None == claim):
        print('Failed to match on ', claim)
        break

    #fabric[res.groups()[1]:(res.groups()[1] + res.groups()[3] - 1), res.groups()[2]:(res.groups()[2] + res.groups()[4] - 1)] += 1
    fabric[int(res.groups()[1]):(int(res.groups()[1]) + int(res.groups()[3])), int(res.groups()[2]):(int(res.groups()[2]) + int(res.groups()[4]))] += 1


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


