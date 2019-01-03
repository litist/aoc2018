
# coding: utf-8

# In[127]:


import numpy as np

input = np.loadtxt('input.txt', dtype=int)

freq = 0
dup = [freq]
found = False

# add first round of freq
for i in input:
    freq += i
    #print('i: {} freq: {}'.format(i, freq))
    #if np.isin(dup, freq):
    if np.any(dup == freq):
        print('Found duplicate: {:d}'.format(freq))
        found = True
        break
    dup = np.append(dup, freq)

# fast forward
ff = int(np.floor( (dup.max()-dup.min())/dup[-1] ))
freq = dup[-1]*ff
print('fas forward to {} with factor {}'.format(freq, ff))
while(not found):
    for i in input:
        freq += i
        #print('i: {} freq: {}'.format(i, freq))
        #if np.isin(dup, freq):
        if np.any(dup == freq):
            print('Found duplicate: {:d}'.format(freq))
            found = True
            break
        dup = np.append(dup, freq)
    if found:
        break
    print(dup.size)
print(dup)


# In[76]:


print(input)


# In[100]:


get_ipython().run_line_magic('matplotlib', 'inline')
from ipywidgets import interactive, fixed
#%matplotlib notebook
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

# build one freq loop
one_loop = np.append(np.empty([0], int), 0)
for f in input:
    print('length {} last: {} f {} '.format(one_loop.size, one_loop[-1], f))
    one_loop = np.append(one_loop, one_loop[-1] + f)
    


plt.plot(one_loop)
print(one_loop)
#plt.show()

