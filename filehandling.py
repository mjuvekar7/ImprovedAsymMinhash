"""
filehandling.py

Main executing code.
"""

import sys
import os

from asym_minhash import AsymmetricMinwiseHasher

"""
Convert a file into the set of its lines.
"""
def file2set(filename):
    return set(open(filename, 'r').read().splitlines())

"""
Load all files in a directory as data.
Output:
    - The datasets loaded, in the form of a dictionary {filename : set}
    - The union of all sets loaded where each element has a numeric id (the "vocabulary")
"""
def load_data(directory):
    print('Loading data from:', directory)
    files = [os.path.join(directory, f) for f in os.listdir(directory)]
    datasets = {}
    vocab_set = set()
    for filename in files:
        file_shingles = file2set(filename)
        datasets[filename] = file_shingles
        vocab_set = vocab_set.union(file_shingles)

    vocab_count = 0
    vocabulary = {}
    for word in vocab_set:
        vocabulary[word] = vocab_count
        vocab_count += 1

    print('Number of sets loaded:', len(datasets))
    print('Vocabulary size:', vocab_count)
    return datasets, vocabulary

