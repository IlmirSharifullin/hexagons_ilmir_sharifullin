from itertools import product

import numpy as np

from consts import PLAIN_TYPE


def create_map(max_dist):
    n = max_dist * 2 + 1
    data = np.array([i + (PLAIN_TYPE,) for i in product(range(n), repeat=3)])
    return data


def get_hex_idxs(coords_map, c):
    res = np.where((np.sum(coords_map[:, :3], axis=1) == 3 * c))[0]

    return res
