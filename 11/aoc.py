import numpy as np



def buildGrid(serial):
    # build fuel grid
    grid = np.zeros((301,301))

    for x in range(1, 301):
        for y in range(1, 301):
            # Find the fuel cell's rack ID, which is its X coordinate plus 10.
            rack_id = x + 10

            # Begin with a power level of the rack ID times the Y coordinate.
            power_lvl = rack_id * y

            # Increase the power level by the value of the grid serial number (your puzzle input).
            power_lvl += serial
            # Set the power level to itself multiplied by the rack ID.
            power_lvl *= rack_id
            # Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
            hundreds = int(np.floor(np.mod(power_lvl, 1000) / 100))
            # Subtract 5 from the power level.
            power_lvl = hundreds - 5

            grid[x,y] = power_lvl
    return grid


# # Fuel cell at  122,79, grid serial number 57: power level -5.
# print('check 1(-5): ', buildGrid(57)[122,79])
# # Fuel cell at 217,196, grid serial number 39: power level  0.
# print('check 2(0): ', buildGrid(39)[217,196])
# # Fuel cell at 101,153, grid serial number 71: power level  4.
# print('check 3(4): ', buildGrid(71)[101,153])


g = buildGrid(7857)

# find largest 3x3 grid
fmax = -1000
posmax = (0,0)
for x in range(1,301-2):
    for y in range(1,301-2):
        #print(g[x:x+3, y:y+3])
        f33 = np.sum(g[x:x+3, y:y+3])

        if f33 > fmax:
            fmax = f33
            posmax = (x,y)
            print('{} at {},{}'.format(fmax, posmax[0], posmax[1]))
print('Maxfuel {} is at {},{}'.format(fmax, posmax[0], posmax[1]))

# find largest 3x3 grid
fmax = -1000
posmax = (0,0,0)
#for size in range(1,301):
for size in range(1,301):
    for x in range(1,301-size+1):
        for y in range(1,301-size+1):
            #print(g[x:x+3, y:y+3])
            f33 = np.sum(g[x:x+size, y:y+size])

            if f33 > fmax:
                fmax = f33
                posmax = (x,y,size)
                print('{} at {},{},{}'.format(fmax, posmax[0], posmax[1], posmax[2]))

print('Maxfuel {} is at {},{},{}'.format(fmax, posmax[0], posmax[1], posmax[2]))




