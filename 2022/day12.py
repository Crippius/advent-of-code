from day08 import check_boundaries


def add_vector(*vectors):
    if len(vectors) == 0:
        raise Exception()
    final_vector = [0]*len(vectors[0])
    
    for vector in vectors:
        if len(vector) != len(final_vector):
            raise Exception
        for i in range(len(vector)):
            final_vector[i] += vector[i]
    return tuple(final_vector)


def find_init_conditions(grid):
    start, end = (0, 0), (0, 0)
    for i, row in enumerate(grid):
        if "S" in row:
            start = (row.find("S"), i)
        if "E" in row:
            end = (row.find("E"), i)
    return start, end


def climbable(grid, start, end):
    height_dict = {letter:height for height, letter in enumerate("abcdefghijklmnopqrstuvwxyz")}
    height_dict["S"] = height_dict["a"]
    height_dict["E"] = height_dict["z"]

    start_height = height_dict[grid[start[1]][start[0]]]
    end_height = height_dict[grid[end[1]][end[0]]]

    return end_height-start_height <= 1


def find_neighbors(grid, point):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start = point

    neighbors = []

    for dir in dirs:
        point = start
        point = add_vector(point, dir)
    
        if check_boundaries((point[0], 0, len(grid[0])-1), (point[1], 0, len(grid)-1)) and climbable(grid, start, point):
            neighbors.append(point)

    return neighbors


def shortest_path(grid, start, end):
    start_x, start_y = start
    end_x, end_y = end

    distance_grid = []
    for _ in range(len(grid)):
        row = []
        for __ in range(len(grid[0])):
            row.append(float("+inf"))
        distance_grid.append(row)

    distance_grid[start_y][start_x] = 0
    exploration_queue = [start]

    while len(exploration_queue):
        
        current_x, current_y = exploration_queue.pop(0)
        
        for neighbor_x, neighbor_y in find_neighbors(grid, (current_x, current_y)):
           
            if distance_grid[neighbor_y][neighbor_x] == float("+inf"):
                distance_grid[neighbor_y][neighbor_x] = distance_grid[current_y][current_x] + 1
                exploration_queue += [(neighbor_x, neighbor_y)]

    return distance_grid[end_y][end_x]
    
            

if __name__ == "__main__":

    fp = open("day12_input.txt", "r")

    grid = []
    row = fp.readline()
    while row != "":
        grid.append(row[:-1])
        row = fp.readline()
    start, end = find_init_conditions(grid)

    min_steps = shortest_path(grid, start, end)
    print(f"The shortest path from S to E is: {min_steps}")

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "a":
                curr_min_steps = shortest_path(grid, (x, y), end)
                if curr_min_steps < min_steps:
                    min_steps = curr_min_steps
    print(f"The shortest path from any a to E is: {min_steps}")
    
    fp.close()