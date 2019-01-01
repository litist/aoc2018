import numpy as np


def marbleGame(N_MARBLES, N_PLAYERS):

    #N_MARBLES = 25
    #N_PLAYERS = 5

    c_player = -1
    p_score = []

    for p in range(0, N_PLAYERS):
        p_score.append(0)

    marbles = [0]
    c_mar = 0

    for marble in range(1, N_MARBLES+1):
        # inc player index
        c_player = np.mod(c_player + 1, N_PLAYERS)

        if np.mod(marble, 23) == 0:
            # remove marble 7 places countclockwise
            c_mar = np.mod(c_mar + len(marbles) - 7, len(marbles))

            mp = marbles.pop(c_mar)
            # add to score of player
            p_score[c_player] += marble + mp

            #print('Multiple of 23, popped: ', mp)

            continue


        c_mar = np.mod(c_mar + 1, len(marbles)) + 1

        # add to marbles
        marbles.insert(c_mar, marble)

        #print(c_mar, ' | ', marbles)

    print(p_score)
    print(np.max(p_score))

marbleGame(25, 5)
marbleGame(1618, 10)
marbleGame(7078400, 452)




