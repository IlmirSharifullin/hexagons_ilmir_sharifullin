import random

import numpy as np

from consts import ALL_MOVEMENTS, RIVERS_COUNT, MAX_RIVER_LENGTH, river_movements, RIVER_TYPE, HILLS_COUNT, \
    HILLS_TYPE, ROUTE_TYPE

np.random.seed(42)
random.seed(42)


def is_valid_point(point, c):
    return np.all(point >= 0) and np.all(point < 2 * c + 1)


def generate_rivers(map_data, hex_idxs, c):
    river_map = np.copy(map_data)
    for i in range(RIVERS_COUNT):
        length = random.randint(1, MAX_RIVER_LENGTH)
        current_idx = random.choice(hex_idxs)
        current = river_map[current_idx, :3]

        for _ in range(length):
            movement = random.choice(river_movements)
            new_point = current + movement
            if is_valid_point(new_point, c):
                new_point_idx = np.where((river_map[:, :3] == new_point).all(axis=1))[0]

                river_map[new_point_idx, 3] = RIVER_TYPE
                current = new_point
    return river_map


def generate_hills(map_data, hex_idxs, c):
    hills_map = np.copy(map_data)

    for _ in range(HILLS_COUNT):
        random_idx = random.choice(hex_idxs)
        point = hills_map[random_idx, :3]
        hills_map[random_idx, 3] = HILLS_TYPE
        for movement in ALL_MOVEMENTS:
            neighbor_point = point + movement
            if is_valid_point(neighbor_point, c):
                neighbor_point_idx = np.where((hills_map[:, :3] == neighbor_point).all(axis=1))[0]
                hills_map[neighbor_point_idx, 3] = HILLS_TYPE

    return hills_map


def visualize_solve(route_map, route_path):
    for cell_idx in route_path:
        route_map[cell_idx][-1] = ROUTE_TYPE

    return route_map
