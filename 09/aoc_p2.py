import numpy as np

class Marble(object):
    def __init__(self):
        self.prev = self
        self.next = self
        self.value = None

def printMarbles(mar, N):

    for _ in range(N):
        print(mar.value, ' -> ', end='')
        mar = mar.next
    print('')


def marbleGame(N_MARBLES, N_PLAYERS):

    #N_MARBLES = 25
    #N_PLAYERS = 5

    c_player = -1
    p_score = []

    for _ in range(0, N_PLAYERS):
        p_score.append(0)

    
    c_mar = Marble()
    c_mar.value = 0
    
    for marble in range(1, N_MARBLES+1):

        if np.mod(marble, (N_MARBLES/100)) == 0:
            print('\r{} %'.format(100*marble/N_MARBLES),end='')

        # inc player index
        c_player = np.mod(c_player + 1, N_PLAYERS)

        if np.mod(marble, 23) == 0:
            # remove marble 7 places countclockwise
            for _ in range(7):
                c_mar = c_mar.prev

            mp = c_mar

            # unlink
            mp.prev.next = mp.next
            mp.next.prev = mp.prev
            c_mar = mp.next


            # add to score of player
            p_score[c_player] += marble + mp.value

            #print('Multiple of 23, popped: ', mp.value)

            continue


        # c_mar = np.mod(c_mar + 1, len(marbles)) + 1

        # create new marble
        m = Marble()
        m.value = marble
        m.prev = c_mar.next
        m.next = c_mar.next.next

        c_mar.next.next.prev = m
        c_mar.next.next = m

        c_mar = m

        #printMarbles(c_mar, marble)

        # add to marbles
        #marbles.insert(c_mar, marble)

        #print(c_mar, ' | ', marbles)

    print(p_score)
    print(np.max(p_score))

#marbleGame(12, 5)
#marbleGame(25, 5)
#marbleGame(1618, 10)
#marbleGame(70784, 452)

#3169872331
marbleGame(7078400, 452)




