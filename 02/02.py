
with open('02/input.txt') as f:
    read_data = f.read()
f.closed

print(read_data)

boxes = read_data.rstrip().split('\n')



char2 = 0
char3 = 0

for box in read_data.rstrip().split('\n'):
    l = list(box)
    l.sort()
    print(l)

    multi = 1

    _char2 = False
    _char3 = False
    for c in range(1, len(l)):

        if(l[c-1] == l[c]):
            multi = multi + 1
        else:
            if(multi==2):
                print('got 2 with ', l[c-1])
                _char2 = True
            if(multi==3):
                print('got 3 with ', l[c-1])
                _char3 = True

            multi = 1

    if(multi==2):
        print('got 2 with ', l[c-1])
        _char2 = True
    if(multi==3):
        print('got 3 with ', l[c-1])
        _char3 = True


    char2 = char2 + _char2
    char3 = char3 + _char3

    print(char2, ' ', char3)

print('Solution: ', char2*char3)

# bruteforce the second part
for box1 in range(0, len(boxes)):
    for box2 in range(box1, len(boxes)):
        #print('check ', box1, ' and ', box2)
        box_c1 = list(boxes[box1])
        box_c2 = list(boxes[box2])

        delta = 0
        for c in range(0, len(box_c1)):
            if(box_c1[c] != box_c2[c]):
                delta = delta + 1

                if(delta > 1):
                    break

        if(delta == 1):
            # bpacnmglhizqygfsjixtkwudr
            print('Solution:\n', boxes[box1], '\n', boxes[box2])


print('Bye...')




