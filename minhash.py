"""
minhash.py

A simple minwise hashing implementation.
"""

from functools import reduce
from math import inf
from random import randint
import json

class MinHasher:
    """
    Generate hash function parameters. Return and save to file.
    Parameters are in the form of (a,b,c) tuples corresponding to the hash
    function ax + b (mod c).
    """
    def generateParameters(outfile):
        PRIME = 2003
        COUNT = 160

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
    @staticmethod
    def getVocab(sets):
        vocab_set = reduce(lambda x, y : x.union(y), list(sets.values()))
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
    Minhash signatures are returned as lists.
    """
    def minhash(self, in_set):
        signature = [inf] * len(self.hash_params)
        for shingle in in_set:
            rownum = self.vocabulary[shingle]
            for i in range(len(self.hash_params)):
                hashed_rownum = MinHasher.getHash(rownum, self.hash_params[i])
                if hashed_rownum < signature[i]:
                    signature[i] = hashed_rownum
        return signature

    """
    Get signatures for all sets.
    Output: { set_id : signature }
    """
    def getAllSignatures(self, progress=True):
        count = 0
        total = len(self.sets)

        if len(self.signatures) == len(self.sets):
            if progress:
                print('MH: Found saved signatures. No need to generate.')
            return self.signatures

        if progress:
            print('MH: Generating all signatures...')

        sigs = {}
        for set_id, dataset in self.sets.items():
            if progress and count % 100 == 0:
                print('MH:', count, "done.", total - count, "left.")
            signature = self.minhash(dataset)
            sigs[set_id] = signature
            count += 1

        self.signatures = sigs
        if self.save_sigs != "":
            if progress:
                print('MH: Done generating. Writing to file', self.save_sigs)
            out_f = open(self.save_sigs, 'w')
            json.dump(sigs, out_f)
            out_f.close()
            if progress:
                print('MH: Done writing signatures.')
        else:
            if progress:
                print('MH: Done generating.')
        return sigs

    """
    Constructor.
    datasets must be a dictionary of the form { set_id : set }
    hashparam_file should be a file path. The file should contain lines each of
    the form a,b,c where a, b, and c will be used as universal hash function
    parameters.
    """
    def __init__(self, datasets, hashparam_file="minhash_params",
            generate=False, vocab=None, load_sigs="", save_sigs=""):
        self.sets = datasets
        if vocab:
            print('MH: Vocabulary given. No need to compute.')
            self.vocabulary = vocab
        else:
            print('MH: Getting vocabulary...')
            self.vocabulary = MinHasher.getVocab(datasets)
            print('MH: Done.')
        if generate:
            print('MH: Generating hashes.')
            self.hash_params = MinHasher.generateParameters(hashparam_file)
        else:
            print('MH: Loading hashes.')
            self.hash_params = MinHasher.loadParameters(hashparam_file)
        if load_sigs == "":
            self.signatures = {} # no need to compute all signatures unless required.
                             # all signatures will be computed and saved when
                             # first requested.
        else:
            print('MH: Loading precomputed signatures.')
            self.signatures = json.load(open(load_sigs, 'r'))
        self.save_sigs = save_sigs

