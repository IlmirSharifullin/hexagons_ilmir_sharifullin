from base import create_map, get_hex_idxs
from generations import generate_rivers, generate_hills
from show import show

MAX_DIST = 20


def main():
    map_data = create_map(MAX_DIST)
    hexagon_idxs = get_hex_idxs(map_data, MAX_DIST)
    map_data = generate_rivers(map_data, hexagon_idxs, MAX_DIST)
    map_data = generate_hills(map_data, hexagon_idxs, MAX_DIST)

    hexagon_data = map_data[hexagon_idxs]
    show(hexagon_data, hexagon_idxs)

if __name__ == '__main__':
    main()