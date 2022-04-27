"""
minhash.py
Author: Mandar Juvekar

A simple minwise hashing implementation.
"""

from functools import reduce
from math import inf
from random import randint

class MinHasher:
    """
    Generate hash function parameters. Return and save to file.
    Parameters are in the form of (a,b,c) tuples corresponding to the hash
    function ax + b (mod c).
    """
    def generateParameters(outfile):
        PRIME = 2003
        COUNT = 128

        hashes = []
        f = open(outfile, 'w')
        for i in range(COUNT):
            a = randint(1, PRIME - 1)
            b = randint(1, PRIME - 1)
            f.write(str(a) + ',' + str(b) + ',' + str(PRIME) + '\n')
            hashes.append((a,b,PRIME))
        f.close()
        return hashes

    """
    Load hash function parameters from a file.
    File format: line of the form a,b,c for each hash.
    """
    def loadParameters(infile):
        return [(int(l[0]), int(l[1]), int(l[2])) for l in
                   map(lambda x: x.split(','),
                       filter(lambda x: x != '',
                              open(infile, 'r').read().splitlines()))]

    """
    Get the vocabulary of a collection of sets.
    A vocabulary is a dictionary that assigns each unique element a numeric ID.
    """
    def getVocab(sets):
        vocab_set = reduce(lambda x, y : x.union(y), sets)
        vocab_count = 0
        vocabulary = {}
        for word in vocab_set:
            vocabulary[word] = vocab_count
            vocab_count += 1

        return vocabulary

    """
    Given hash function parameters, get the hash of x.
    """
    def getHash(x, params):
        a, b, c = params
        return (a * x + b) % c

    """
    Generate the minhash signature of a set.
    """
    def minhash(self, in_set):
        signature = [inf] * len(self.hash_params)
        for shingle in in_set:
            rownum = self.vocabulary[shingle]
            for i in range(len(self.hash_params)):
                hashed_rownum = get_hash(rownum, self.hash_params[i])
                if hashed_rownum < signature[i]:
                    signature[i] = hashed_rownum
        return signature

    """
    Constructor.
    """
    def __init__(self, datasets, hashparam_file="minhash_params", generate=False):
        self.sets = datasets
        self.vocabulary = getVocab(datasets)
        if generate:
            self.hash_params = generateParameters(hashparam_file)
        else:
            self.hash_params = loadParameters(hashparam_file)

