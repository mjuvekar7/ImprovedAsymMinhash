"""
asym_minhash.py

A simple implementation of asymmetric minwise hashing.
"""

from lsh import LSHIndex, band_hash
from minhash import MinHasher

class AsymmetricMinwiseHasher:
    """
    Query index for a given set. Return all candidates.
    """
    def query(self, q_set):
        q_signature = self.minhasher.minhash(q_set)
        return self.index.query(q_signature)

    """
    Given a collection of sets, pad them to the size of the largest set.
    Input: dictionary of the form { set_id : set }
    Output: dictionary of the form {set_id : set_padded }
    """
    def padSets(sets):
        PADDING = "PaDdInG_vAlUe_"
        
        # Find largest size and compute vocab
        largest_size = 0
        vocab = set()
        for _, s in sets:
            if largest_size < len(s):
                largest_size = len(s)
            vocab = vocab.union(s)

        padded = {}
        padding_vals = []
        count = 0
        for set_id, s in sets:
            num_required = largest_size - len(s)
            if len(padding_vals) >= num_required:
                padded[set_id] = s.union(set(padding_vals[:num_required]))
            else:
                while len(padding_vals) < num_required:
                    if PADDING + str(count) not in vocab:
                        padding_vals.append(PADDING + str(count))
                    count += 1
                # On exit len(padding_vals) = num_required
                padded[set_id] = s.union(set(padding_vals))
        return padded
    
    """
    Constructor.
    sets is a dictionary of the form { set_id : set }
    lsh_hashfunc should be a function that takes a band and hashes to an integer.
    """
    def __init__(self, sets, lsh_b, lsh_r, lsh_hashfunc=band_hash, minhashfile=""):
        self.raw_sets = sets
        self.padded_sets = padSets(sets)
        if minhashfile == "":
            self.minhasher = MinHasher(self.padded_sets, hashparam_file="asym_mh_hashes",
                    generate=True)
        else:
            self.minhasher = MinHasher(self.padded_sets, hashparam_file="asym_mh_hashes",
                    generate=False)

        # Get signatures of padded sets
        self.mh_signatures = minhasher.getAllSignatures()

        # Build index
        self.index = LSHIndex(lsh_b, lsh_r, lsh_hashfunc, self.mh_signatures)

