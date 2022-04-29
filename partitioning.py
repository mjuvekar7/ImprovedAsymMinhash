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
            partition.append(sets_sorted[last_end : last_end + depth + 1])
            last_end += depth + 1
        else:
            partition.append(sets_sorted[last_end : last_end + depth])
            last_end += depth
    return partition

"""
Partition that minimizes the sum
\sum_{part} |part| max(part)
"""
def paddingMinimizingPartition(sets, nparts):
    pass # TODO

