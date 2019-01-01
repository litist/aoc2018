import numpy as np
import re
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

with open('10/input.txt') as fin:
#with open('10/input_test.txt') as fin:
    read_data = fin.read()
fin.closed


stars = []

# position=<-42139,  10759> velocity=< 4, -1>
valid = re.compile(r"position=< ?(-?\d+),  ?(-?\d+)> velocity=< ?(-?\d+),  ?(-?\d+)>")
for claim in read_data.rstrip().split('\n'):
    res = valid.search(claim)
    #print(claim, displaymatch(valid.search(claim)))  # Valid.
    if(None == res):
        print('Failed to match on ', claim)
        break
    #coords.append((int(res.groups()[0]), int(res.groups()[1]), len(coords)+1))

    # 
    stars.append([int(res.groups()[0]), int(res.groups()[1]), int(res.groups()[2]), int(res.groups()[3])])


print(stars)


scale = 300

dim =[600, 600]
offset = (299,299)



sec = 0

min = -299
max = 299

def f(sec):
    #message = np.zeros([np.abs(np.floor(x_dim[0]/scale))+np.ceil(x_dim[1]/scale), np.abs(np.floor(y_dim[0]/scale))+np.ceil(y_dim[1]/scale)])
    message = np.zeros(dim)

    t_stars = []
    for s in stars:
        t_stars.append(int(s[0]+sec*s[2]))
        t_stars.append(int(s[1]+sec*s[3]))
    
    scale = np.ceil(np.max(np.abs(t_stars)) / 299)

    print('Scale ', scale)

    for s in stars:
        message[int((s[0]+sec*s[2])/scale+offset[0]), int((s[1]+sec*s[3])/scale+offset[1])] = 1


    return message


#im = plt.imshow(message_, animated=True)


def updatefig(*args):
    global sec
    global im
    sec += 1

    print('Time: ', sec)

    im.set_array(f(sec))

    
    return im,




fig = plt.figure()
sec = 10577
#im = plt.imshow(message, cmap='Greys',  interpolation='nearest', animated=True)#
im = plt.imshow(f(sec), cmap='gist_gray_r', animated=True)
plt.show()

quit()

fig = plt.figure()
sec = 10576
#im = plt.imshow(message, cmap='Greys',  interpolation='nearest', animated=True)#
im = plt.imshow(f(10580), cmap='gist_gray_r', animated=True)
ani = animation.FuncAnimation(fig, updatefig, interval=2000, blit=True)
plt.show()

