class MinHasher:
    """
    Generate hash function parameters. Return and save to file.
    Parameters are in the form of (a,b,c) tuples corresponding to the hash
    function ax + b (mod c).
    """
    def generateParameters(outfile):
        pass

    """
    Load hash function parameters from a file.
    File format: line of the form a,b,c for each hash.
    """
    def loadParameters(infile):
        pass

    """
    Get the vocabulary of a collection of sets.
    """
    def getVocab(sets):
        pass

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
        pass

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

