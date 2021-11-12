import pygeohash
import numpy as np
import collections


def find_path(world_map, source_hash, destination_hash, debug=False):
    (source_x, source_y) = get_hash_location(source_hash)
    (destination_x, destination_y) = get_hash_location(destination_hash)
    if debug:
        print("source:", source_x, source_y, "destination:", destination_x, destination_y)

    world_width, world_height = world_map.shape
    queue = collections.deque([[source_hash]])
    seen = {source_hash}
    while queue:
        path = queue.popleft()
        x, y = get_hash_location(path[-1])
        if world_map[x][y] == destination_hash:
            queue.append(path + [destination_hash])
            return path
        if debug:
            print('check', x, y, world_map[x][y])
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < world_width and 0 <= y2 < world_height and is_hash_open(world_map[x2][y2]) and world_map[x2][y2] not in seen:
                if debug:
                    print('neighbour', x2, y2, world_map[x2][y2])
                queue.append(path + [world_map[x2][y2]])
                seen.add(world_map[x2][y2])


def get_hash_location(g_hash):
    (x, y) = pygeohash.decode(g_hash[:-1])
    x = abs(int(x))
    y = abs(int(y))
    return x, y


def get_hash_state(g_hash):
    return g_hash[-1]


def is_hash_open(g_hash):
    return get_hash_state(g_hash) == 'O'


# Test
if __name__ == "__main__":
    world_map = np.array([
        ["7zzzO", "kpbxO", "kpcrO", "kpfpO", "kpfzO", "kpgxO", "kpurO", "kpuzO", "kpvxO", "kpyrO"],
        ["ebpvO", "s00tO", "s01mO", "s04jO", "s04vO", "s05tO", "s0hmO", "s0hvO", "s0jtO", "s0nmO"],
        ["ebrgO", "s02eC", "s037O", "s065O", "s06gO", "s07eO", "s0k7O", "s0kgC", "s0meO", "s0q7O"],
        ["ebxcO", "s089C", "s093O", "s0d1O", "s0dcO", "s0e9O", "s0s3O", "s0scC", "s0t9O", "s0w3O"],
        ["ebxyO", "s08wC", "s09qO", "s0dnO", "s0dyO", "s0ewO", "s0sqO", "s0syC", "s0twO", "s0wqO"],
        ["ebzuO", "s0bsC", "s0ckO", "s0fhO", "s0fuO", "s0gsO", "s0ukO", "s0uuC", "s0vsO", "s0ykO"],
        ["ecpfO", "s10dC", "s116O", "s144O", "s14fO", "s15dO", "s1h6O", "s1hfC", "s1jdO", "s1n6O"],
        ["ecpzO", "s10xC", "s11rO", "s14pO", "s14zO", "s15xO", "s1hrO", "s1hzC", "s1jxO", "s1nrO"],
        ["ecrvO", "s12tC", "s13mO", "s16jO", "s16vO", "s17tO", "s1kmO", "s1kvC", "s1mtO", "s1qmO"],
        ["ecxgO", "s18eC", "s197C", "s1d5C", "s1dgC", "s1eeC", "s1s7C", "s1sgC", "s1teO", "s1w7O"]
    ])
    path = find_path(world_map, "s16jO", "s0meO")
    print(path)
