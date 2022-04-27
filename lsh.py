"""
lsh.py
Author: Mandar Juvekar

A simple locality sensitive hashing implementation.
Designed for use with minhash.
"""

"""
An example band hash function that can be given to the LSHIndex constructor.
"""
def band_hash(signature):
    return hash(str(band))


"""
An LSH index.
"""
class LSHIndex:
    """
    Input: self.signatures should be of the form {set_name : minhash_signature}
    Output: LSH index, i.e. list of b dicts each of the form
    {bucket_id : set_id}.
    """
    def build_lsh_index(self):
        index = [{}] * self.b
        for set_id, sig in self.signatures.items():
            for band_num in range(self.b):
                band = sig[band_num * self.r : (band_num + 1) * self.r]
                bucket = self.hashfunc(band)
                if bucket in index[band_num]:
                    index[band_num][bucket].add(set_id)
                else:
                    index[band_num][bucket] = {set_id}
        return index

    """
    Get the LSH of a signature.
    The output is a list specifying where each band gets hashed.
    """
    def lsh_hash(self, signature):
        lsh = []
        for band_num in range(self.b):
            band = signature[band_num * self.r : (band_num + 1) * self.r ]
            bucket = self.hashfunc(band)
            lsh.append(bucket)
        return lsh
    
    """
    Given a query signature, find all candidates.
    """
    def query(self, q_signature):
        candidates = set()
        buckets = self.lsh_hash(q_signature)
        for band_num in range(self.b):
            bucket = buckets[band_num]
            if bucket in self.index[band_num]:
                candidates = candidates.union(self.index[band_num][bucket])
        return candidates

    """
    Constructor.
    lsh_signatures should be a dictionary of the form { set_id : signature }.
    lsh_hashfunc should be a function that takes a band and hashes to an integer.
    """
    def __init__(self, lsh_b, lsh_r, lsh_hashfunc, lsh_signatures):
        self.signatures = lsh_signatures
        self.b = lsh_b
        self.r = lsh_r
        self.hashfunc = lsh_hashfunc
        self.index = self.build_lsh_index()

