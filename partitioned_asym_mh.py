"""
partitioned_asym_mh.py

Partitioned asymmetric minhash.
"""

from asym_minhash import AsymmetricMinwiseHasher
from lsh import band_hash

"""
A partitioned asymmetric minwise hashing index.
"""
class PartitionedAsymMH:
    """
    Query the partitioned index.
    Return all candidates.
    """
    def query(self, q_set):
        candidates = set()
        for mher in self.asym_minhashers:
            candidates = candidates.union(mher.query(q_set))
        return candidates

    """
    Constructor.
    """
    def __init__(self, sets, lsh_b, lsh_r, part_func, n, lsh_hashfunc=band_hash,
            minhashfile=""):
        # LSH params
        self.b = lsh_b
        self.r = lsh_r
        self.sets = sets
        
        # Partitioning-related
        self.part_fn = part_func
        self.nparts = n
        self.partition = part_func(sets, n)

        # Create asymmetric minhashers
        amhs = []
        for part in self.partition:
            amhs.append(AsymmetricMinwiseHasher(part, lsh_b, lsh_r,
                lsh_hashfunc=lsh_hashfunc, minhashfile=minhashfile))

        self.asym_minhashers = amhs

