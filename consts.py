import numpy as np

ALL_MOVEMENTS = np.array([
    [0, 1, -1],
    [1, 0, -1],
    [1, -1, 0],
    [0, -1, 1],
    [-1, 0, 1],
    [-1, 1, 0]
])

PLAIN_TYPE = 1

river_movements = ALL_MOVEMENTS[0:2]

RIVERS_COUNT = 40

MAX_RIVER_LENGTH = 7

RIVER_TYPE = 10


HILLS_COUNT = 10

HILLS_TYPE = 100


ROUTE_TYPE = 1000

types_map = {
    PLAIN_TYPE: "Plain",
    HILLS_TYPE: "Hill",
    RIVER_TYPE: "River",
    ROUTE_TYPE: "Route"
}

vfunc = np.vectorize(types_map.get)

