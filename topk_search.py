"""
topk_search.py

Implementation of top-k set containment searches.
"""

"""
Set containment.
"""
def cont(Q, X):
    return len(Q.intersection(X)) / len(Q)

"""
Top k search with an asymmetric minhasher (well, any class that has a 'query'
function)
"""
def top_k_search_amh(q_set, amher, k, data):
    conts = [(s_id, cont(q_set, data[s_id])) for s_id in amher.query(q_set)]
    return [(data_id, c) for data_id, c in
                sorted(filter(lambda x: x[1] > 0, conts),
                       key=lambda x: x[1], reverse=True)[:k]]

"""
Brute force top k search.
"""
def top_k_search_baseline(q_set, data, k):
    conts = [(data_id, cont(q_set, data_set)) for
                   data_id, data_set in data.items()]
    return [(data_id, c) for data_id, c in
                sorted(filter(lambda x: x[1] > 0, conts),
                       key=lambda x: x[1], reverse=True)[:k]]

