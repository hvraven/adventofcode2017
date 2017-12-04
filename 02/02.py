#/usr/bin/env python3

import numpy as np

inp = np.genfromtxt('input')

sinp = np.sort(inp)
print(np.sum(sinp[:,-1] - sinp[:,0]))

ax, bx = np.indices((len(inp[0]), len(inp[0])))
ix = np.nonzero(np.fmod(inp[:,ax], inp[:,bx]) == 0)
print(np.sum(inp[ix[0:2]] // inp[ix[::2]]) - np.multiply.reduce(inp.shape))
