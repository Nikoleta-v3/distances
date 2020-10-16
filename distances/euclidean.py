import math 

def euclidean_distance(u, v):
    """
    Computes the Euclidean distance between two vectos `u` and `v`.

    The Euclidean distance between `u` and `v`, is defined as:

    \sqrt{(u_1 - v_1) ^ 2 + ... + (u_n - v_n) ^ 2}

    Parameters
    ----------
    u : list
        Input vector.
    v : list
        Input vector.

    Returns
    -------
    euclidean : double
        The Euclidean distance between vectors `u` and `v`.
    """
    distance = 0
    
    for u_i, v_i in zip(u, v):
        distance += (u_i - v_i) ** 2
        
    return math.sqrt(distance)
