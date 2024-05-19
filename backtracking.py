import math


def count_dist(map_data, a_idx, b_idx):
    a_data = map_data[a_idx][:3]
    b_data = map_data[b_idx][:3]

    return math.sqrt(sum((a_data - b_data) ** 2))


"""
curr_idx - текущий индекс клетки
path - массив, путь до текущей клетки
prev_dist - расстояние от предыдущей клетки до итоговой
prev_movement_idx - индекс прошлого движения, используем чтобы не ходить "туда-сюда"
"""
def get_backtracking(back_from_idx, back_to_idx):
    init_dist = count_dist(back_from_idx, back_to_idx)

    def inner(curr_idx, path, prev_dist, prev_movement_idx):
        pass