"""
partitioning.py

Functions to partition collections of sets.
"""

from math import inf

"""
Partition into equal width partitions.
Input: a dictionary of the form {set_id : set}, a positive integer nparts
Output: an equal width partitioning of the set (list of dictionaries each of the
        form {set_id : set})
"""
def equalWidthPartition(sets, nparts):
    sets_sorted = sorted(sets.items(), key=lambda x: len(x[1]))
    width = (len(sets_sorted[-1][1]) - len(sets_sorted[0][1])) / nparts
    min1 = len(sets_sorted[0][1])
    boundaries = [min1 + i * width for i in range(nparts)]
    boundaries.append(inf)

    partition = []
    for i in range(nparts):
        temp = []
        for s in sets_sorted:
            if len(s[1]) >= boundaries[i] and len(s[1]) < boundaries[i+1]:
                temp.append(s)
        partition.append(dict(temp))

    return partition

"""
Partition into equal depth partitions.
Input: a dictionary of the form {set_id : set}, a positive integer nparts
Output: an equal depth partition (same output format as above).
"""
def equalDepthPartition(sets, nparts):
    partition = []
    sets_sorted = sorted(sets.items(), key=lambda x: len(x[1]))
    depth = int(len(sets) / nparts)
    mod = len(sets) % nparts
    last_end = 0
    for i in range(nparts):
        if i < mod:
            partition.append(dict(sets_sorted[last_end : last_end + depth + 1]))
            last_end += depth + 1
        else:
            partition.append(dict(sets_sorted[last_end : last_end + depth]))
            last_end += depth
    return partition

"""
Partition that minimizes the sum
\sum_{part} |part| max(part)
with the added restriction that parts must be contiguous when the sets are
sorted by cardinality.
"""
def paddingMinimizingPartition(sets, nparts):
    k = len(sets)
    sets_sorted = sorted(sets.items(), key=lambda x: len(x[1]))
    dp_array = [[inf for _ in range(nparts+1)] for _ in range(k+1)]
    solns = [[[] for _ in range(nparts+1)] for _ in range(k+1)]

    # Base cases
    dp_array[k][0] = 0
    solns[k][0] = [k]
    for j in range(1, nparts + 1):
        dp_array[k][j] = inf
    for i in range(k):
        dp_array[i][0] = inf

    # Build DP array
    for i in reversed(range(k - 1)):
        for j in range(1, nparts + 1):
            min_cost = inf
            min_l = i
            for l in range(i, k):
                cost = (l-i+1) * len(sets_sorted[l][1]) + dp_array[l+1][j-1]
                if cost < min_cost:
                    min_cost = cost
                    min_l = l
            dp_array[i][j] = min_cost
            solns[i][j] = [i] + solns[min_l + 1][j - 1]

    # our partition is now solns[0][nparts]
    boundaries = solns[0][nparts]
    print(boundaries)
    partition = []
    for n in range(nparts):
        partition.append(dict(sets_sorted[boundaries[n] : boundaries[n+1]]))
    return partition

