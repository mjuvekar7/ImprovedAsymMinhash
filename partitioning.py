"""
Partition into equal width partitions.
Input: a dictionary of the form {set_id : set}, a positive integer nparts
Output: an equal width partitioning of the set (list of dictionaries each of the
        form {set_id : set})
"""
from json.encoder import INFINITY


def equalWidthPartition(sets, nparts):
    """
    is the argument 'sets' referring to one {set_id :set} instance or does refer to a dictionary that contains multiple instances of {set_id : set}?

    If it contains one instance of {set_id : set} only, it would be easy to just partition the values in that instance into nparts and return the nparts as dictionaries
    However, if there were multiple {set_id : set} instances, how does one partition them without accounting for if those different instances of {set_id : set} were unrelated?
    Is it possible to jumble all all the dictionary values of the different instances into one big set and then partition from there? 

    On return, what keys will the partitioned dictionaries be described with?
    """
    map_ret = {}
    for key, seti in sets.items():
        min_v = min(seti)
        w = int((max(seti) - min_v)/ nparts)

        arr = []
        for i in range(0, nparts +  1):
            arr = arr + [min_v + w*i]
        
        arri = []
        for i in range(0, nparts):
            temp = []
            for j in seti:
                if j >= arr[i] and j <= arr[i+1]:
                    temp += [j]
            arri += [temp]

        map_ret[key] = arri
    return map_ret



"""
Partition into equal depth partitions.
Input: a dictionary of the form {set_id : set}, a positive integer nparts
Output: an equal depth partition (same output format as above).
"""
def equalDepthPartition(sets, nparts):
    """
    What does an equal depth partition mean?
    """
    map_ret = {}
    for key, seti in sets.items():
        a = len(seti)
        n = int(a/nparts)

        arr = []
        for i in range(0, nparts):
            temp = []
            for j in range(i*n, (i + 1) * n):
                if j >= a:
                    break
                temp += [seti[j]]
            arr += [temp]
        
        map_ret[key] = arr
    return map_ret

"""


TODO figure this out
"""
def ourPartitioningScheme(sets, nparts):
    pass # TODO

 

print(equalWidthPartition({"hey": [5,10,11,13,15,35,50,55,72,92,204,215], "hn": [2,10,11,13,5,35,100,55,72,92,9,21], "heyn": [2,10,11,13,15,35,50,55,72,92,9,21]}, 3))
print(equalDepthPartition({"hey": [5,10,11,13,15,35,50,55,72,92,204,215], "hn": [2,10,11,13,5,35,100,55,72,92,9,21], "heyn": [2,10,11,13,15,35,50,55,72,92,9,21]}, 3))