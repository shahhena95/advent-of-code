from collections import defaultdict
volumes = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]

dimensions = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]

print volumes.sort() == dimensions.sort()

dist = defaultdict(int)
for mask in xrange(1, 1<<len(dimensions)):
    p = [d for i, d in enumerate(dimensions) if (mask & (1 << i)) > 0]
    if sum(p) == 150: dist[len(p)] += 1

print "total:", sum(dist.values())
print "min:", dist[min(dist.keys())]
