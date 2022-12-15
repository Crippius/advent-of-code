

def check_boundaries(*limits):
    for x, start, end in limits:
        if not (x >= start and x <= end):
            return False
    return True



def is_visible(row, col, forest, dir):

    dir_directions = {"N":(-1, 0), "S":(1, 0), "W":(0, -1), "E":(0, 1)}

    y, x = row, col

    incr_y, incr_x = dir_directions[dir]

    x += incr_x
    y += incr_y
    while check_boundaries((y, 0, len(forest)-1), (x, 0, len(forest[0])-1)):
        if forest[y][x] >= forest[row][col]:
            return False
        
        x += incr_x
        y += incr_y
    return True
        
def is_visible_all_dirs(row, col, forest):
    for dir in ("N", "S", "W", "E"):
        if is_visible(row, col, forest, dir):
            return True
    return False

def calc_scenic_score(row, col, forest):
    
    scenic_score = 1

    dir_directions = {"N":(-1, 0), "S":(1, 0), "W":(0, -1), "E":(0, 1)}

    for dir in ("N", "S", "W", "E"):
        y, x = row, col

        incr_y, incr_x = dir_directions[dir]

        x += incr_x
        y += incr_y

        visible_trees = 0
        while check_boundaries((y, 0, len(forest)-1), (x, 0, len(forest[0])-1)):
            visible_trees += 1
            if forest[y][x] >= forest[row][col]:
                break
            
            x += incr_x
            y += incr_y

        scenic_score *= visible_trees
    
    return scenic_score



if __name__ == "__main__":

    fp = open("day08_input.txt", "r")

    line = fp.readline()

    forest = []

    while line != "":
        forest.append([int(i) for i in line[:-1]])
        line = fp.readline()
    
    visible_trees = 0
    best_scenic_score = 0
    for row in range(len(forest)):
        for col in range(len(forest[row])):
            visible_trees += is_visible_all_dirs(row, col, forest)
            scenic_score = calc_scenic_score(row, col, forest)

            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score
    
    print(f"The number of visible trees from the border of the forest is: {visible_trees}")
    print(f"The best scenic score in the forest is: {best_scenic_score}")
        
    fp.close()