import numpy as np
import re
import matplotlib.pyplot as plt



class Tree(object):
    def __init__(self):
        self.n_nodes = None
        self.nodes = []
        self.meta = []
        self.n_meta = None
 


def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

with open('08/input.txt') as f:
#with open('08/input_test.txt') as f:
    read_data = f.read()
f.closed

# read data in convert to integer
in_data = [int(item) for item in read_data.rstrip().split(' ')]


def getMetaSum(node):
    s = np.sum(node.meta)

    for n in node.nodes:
        s += getMetaSum(n)

    return s


def getValue(node):

    if node.n_nodes == 0:
        return sum(node.meta)

    nval = 0
    for m in node.meta:
        if m > 0 and m <= node.n_nodes:
            nval += getValue(node.nodes[m-1])

    return nval


def printNode(node, depth):
    print('\t'*depth, 'N_META: ', node.n_meta)

    for n in node.nodes:
        printNode(n, depth+1)


def parseNode(node):
    node.n_nodes = in_data.pop(0)
    node.n_meta = in_data.pop(0)

    # now all child nodes
    for n in range(0, node.n_nodes):
        # add node
        node.nodes.append(Tree())
        # parse data init node
        parseNode(node.nodes[-1])

    # get meta data
    for m in range(0, node.n_meta):
        node.meta.append(in_data.pop(0))



root = Tree()
parseNode(root)

printNode(root, 0)

quit()

print('Solution 1: ', getMetaSum(root))
print('Solution 2: ', getValue(root))

quit()
