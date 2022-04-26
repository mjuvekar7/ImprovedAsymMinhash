import minhash

class LSHIndex:
    """
    Input: dictionary of form {set_name : minhash_signature}
    Output: LSH index, i.e. list of LSH_B dicts each of the form
    {bucket_id : set_id}.
    """
    def build_lsh_index(signatures):
        pass

    """
    Get the LSH of a signature.
    """
    def lsh_hash(self, signature):
        pass
    
    """
    Given a query signature, find all candidates.
    """
    def query(self, q_signature):
        pass

    """
    Constructor.
    """
    def __init__(self, lsh_b, lsh_r, lsh_hashfunc, signatures):
        self.b = lsh_b
        self.r = lsh_r
        self.hashfunc = lsh_hashfunc
        self.index = build_lsh_index(signatures)

