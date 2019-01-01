import numpy as np
import re
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation



def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())


with open('16/input.txt') as fin:
#with open('16/input_test.txt') as fin:
    read_data = fin.read()
fin.closed

# read data sets
idata = read_data.rstrip().split('\n')

regex_before = re.compile(r"\[(\d+), (\d+), (\d+), (\d+)\]")
regex_opcode = re.compile(r"(\d+) (\d+) (\d+) (\d+)")

data_sets = []

for set_id in range(0, int(np.floor((len(idata)+1)/4))):
    data_sets.append([])

    # before register set
    res = regex_before.search(idata[4*set_id + 0])
    #print(idata[4*set_id + 0], displaymatch(regex_before.search(idata[4*set_id + 0])))  # Valid.
    if(None == res):
        print('Failed to match on ', idata[4*set_id + 0])
    data_sets[-1].append([int(x) for x in res.groups()])

    # read opcode
    res = regex_opcode.search(idata[4*set_id + 1])
    #print(idata[4*set_id + 1], displaymatch(regex_opcode.search(idata[4*set_id + 1])))  # Valid.
    if(None == res):
        print('Failed to match on ', idata[4*set_id + 1])
    data_sets[-1].append([int(x) for x in res.groups()])


    # after register set
    res = regex_before.search(idata[4*set_id + 2])
    #print(idata[4*set_id + 2], displaymatch(regex_before.search(idata[4*set_id + 2])))  # Valid.
    if(None == res):
        print('Failed to match on ', idata[4*set_id + 2])
    data_sets[-1].append([int(x) for x in res.groups()])


# read in program instructions
with open('16/input_2.txt') as fin:
    read_data = fin.read()
fin.closed

program = []

for code in read_data.rstrip().split('\n'):

    # read opcode
    res = regex_opcode.search(code)
    #print(idata[4*set_id + 1], displaymatch(regex_opcode.search(idata[4*set_id + 1])))  # Valid.
    if(None == res):
        print('Failed to match on ', code)
    program.append([int(x) for x in res.groups()])



def operation(code, A, B, C, regs):

    if code == 0:
        # addr (add register) stores into register C the result of adding register A and register B.
        regs[C] = regs[A] + regs[B]
    elif code == 1:
        # addi (add immediate) stores into register C the result of adding register A and value B.
        regs[C] = regs[A] + B

    elif code == 2:
        # mulr (multiply register) stores into register C the result of multiplying register A and register B.
        regs[C] = regs[A] * regs[B]
    elif code == 3:
        # muli (multiply immediate) stores into register C the result of multiplying register A and value B.
        regs[C] = regs[A] * B

    elif code == 4:
        # banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
        regs[C] = regs[A] & regs[B]
    elif code == 5:
        # bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
        regs[C] = regs[A] & B

    elif code == 6:
        # borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
        regs[C] = (regs[A] | regs[B])
    elif code == 7:
        # bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
        regs[C] = (regs[A] | B)

    elif code == 8:
        # setr (set register) copies the contents of register A into register C. (Input B is ignored.)
        regs[C] = regs[A]
    elif code == 9:
        # seti (set immediate) stores value A into register C. (Input B is ignored.)
        regs[C] = A

    elif code == 10:
        # gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
        regs[C] = (A > regs[B])
    elif code == 11:
        # gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
        regs[C] = (regs[A] > B)
    elif code == 12:
        # gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
        regs[C] = (regs[A] > regs[B])
    

    elif code == 13:
        # eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
        regs[C] = (A == regs[B])
    elif code == 14:
        # eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
        regs[C] = (regs[A] == B)
    elif code == 15:
        # eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set t
        regs[C] = (regs[A] == regs[B])

    else:
        print('Unknown OP-code: ', code)

    return regs


        


def checkDateSets(dataset):

    passes = []
    for op in range(16):
        ret = operation(op, dataset[1][1], dataset[1][2], dataset[1][3], list(dataset[0]))
        if ret == dataset[2]:
            #print(dataset, 'set passed for op ', op)
            passes.append(op)
    
    #if passes == 0:
    #    print(dataset, 'No valid op found')

    # print(passes)
    return passes




threepasses = 0
for ds in data_sets:
    passes = checkDateSets(ds)

    ds.append(passes)

    if len(passes) >= 3:
        threepasses += 1
    

print('Solution 1: ', threepasses)


op = {}

for _ in range(16):
    # get first singular solution
    for ds in data_sets:
        if len(ds[3]) == 1:
            break
    else:
        print('Something is wrong')
        quit

    # save this set
    op[ds[1][0]] = ds[3][0]

    # remove dataset which use this op
    data_sets = list(filter(lambda x:x[1][0] != ds[1][0], data_sets))

    # remove the op form multi list
    for a in data_sets:
        a[3] = list(filter(lambda x:x!=ds[3][0], a[3]))


regs = [0, 0, 0, 0]
for p in program:
    regs = operation(op[p[0]], p[1], p[2], p[3], regs)

print('Solution 2: ', regs[0])


quit()
