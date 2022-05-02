"""
partitioned_asym_mh.py

Partitioned asymmetric minhash.
"""

from asym_minhash import AsymmetricMinwiseHasher
from lsh import band_hash
from minhash import MinHasher

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
    Loading currently only works when part_func is deterministic.
    """
    def __init__(self, sets, lsh_b, lsh_r, part_func, n, lsh_hashfunc=band_hash,
            minhashfile="", vocab=None, load_sigs_pfx="", save_sigs_pfx=""):
        # LSH params
        self.b = lsh_b
        self.r = lsh_r
        self.sets = sets
        
        # Partitioning-related
        self.part_fn = part_func
        self.nparts = n
        print('PAMH: Partitioning sets.')
        self.partition = part_func(sets, n)

        if vocab == None:
            vocab = MinHasher.getVocab(sets)

        # Load/save data
        if load_sigs_pfx == "":
            loads = [""] * n
        else:
            loads = [load_sigs_pfx + str(i) + '.json' for i in range(n)]

        if save_sigs_pfx == "":
            saves = [""] * n
        else:
            saves = [save_sigs_pfx + str(i) + '.json' for i in range(n)]

        # Create asymmetric minhashers
        amhs = []
        for i in range(n):
            print('PAMH: Initializing AMH for part number', i)
            amher = AsymmetricMinwiseHasher(self.partition[i], lsh_b, lsh_r,
                    lsh_hashfunc=lsh_hashfunc, minhashfile=minhashfile,
                    vocab=vocab,
                    load_sigs=loads[i], save_sigs=saves[i])
            amhs.append(amher)

        self.asym_minhashers = amhs

