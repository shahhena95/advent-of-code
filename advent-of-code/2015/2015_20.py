import numpy as np


#Referred to hints and solutions


goal = 33100000
houses_a = np.zeros(1000000)
houses_b = np.zeros(1000000)

for elf in xrange(1, 1000000):
    houses_a[elf::elf] += 10 * elf
    houses_b[elf:(elf+1)*50:elf] += 11 * elf
print(np.nonzero(houses_a >= goal)[0][0])
print(np.nonzero(houses_b >= goal)[0][0])
