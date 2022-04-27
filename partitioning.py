"""
Partition into equal width partitions.
Input: a dictionary of the form {set_id : set}, a positive integer nparts
Output: an equal width partitioning of the set (list of dictionaries each of the
        form {set_id : set})
"""
def equalWidthPartition(sets, nparts):
    """
    is the argument 'sets' referring to one {set_id :set} instance or does refer to a dictionary that contains multiple instances of {set_id : set}?

    If it contains one instance of {set_id : set} only, it would be easy to just partition the values in that instance into nparts and return the nparts as dictionaries
    However, if there were multiple {set_id : set} instances, how does one partition them without accounting for if those different instances of {set_id : set} were unrelated?
    Is it possible to jumble all all the dictionary values of the different instances into one big set and then partition from there? 

    On return, what keys will the partitioned dictionaries be described with?
    """

    pass # TODO


"""
Partition into equal depth partitions.
Input: a dictionary of the form {set_id : set}, a positive integer nparts
Output: an equal depth partition (same output format as above).
"""
def equalDepthPartition(sets, nparts):
    """
    What does an equal depth partition mean?
    """
    pass # TODO

"""


TODO figure this out
"""
def ourPartitioningScheme(sets, nparts):
    pass # TODO



# equal frequency
def equifreq(arr1, m):   
    a = len(arr1)
    n = int(a / m)
    for i in range(0, m):
        arr = []
        for j in range(i * n, (i + 1) * n):
            if j >= a:
                break
            arr = arr + [arr1[j]]
        print(arr)
 
# equal width
def equiwidth(arr1, m):
    a = len(arr1)
    w = int((max(arr1) - min(arr1)) / m)
    min1 = min(arr1)
    arr = []
    for i in range(0, m + 1):
        arr = arr + [min1 + w * i]
    arri=[]
     
    for i in range(0, m):
        temp = []
        for j in arr1:
            if j >= arr[i] and j <= arr[i+1]:
                temp += [j]
        arri += [temp]
    print(arri)
 