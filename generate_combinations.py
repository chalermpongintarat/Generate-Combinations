#!/urs/local/bin/python

import os
import os.path
import subprocess

from itertools import combinations

# Get all combination of [1, 2, 3]
# of length 3
picking = 1

# EU
comb = combinations(['ch', 'sk', 'ta', 'th', 'al', 'bu', 'cr', 'de', 'ge', 'hu', 'ir', 'it', 'po', 'ro', 'sr', 'sl', 'sn', 'sp', 'uk', 'us'], picking)

# NA
# comb = combinations(['ch', 'sk', 'ta', 'th', 'vn', 'de', 'ge', 'ca', 'me', 'us', 'cl', 'pe'], picking)

with open("/Users/chalermpong/Desktop/generate_combinations/eu/picking_"+str(picking)+".txt", "w") as file:
	for i in comb:
		i = ', '.join(map(str, i))
		i = i
		file.write("%s\n" % i)