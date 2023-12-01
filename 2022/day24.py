from day12 import add_vector
from day08 import check_boundaries
from time import sleep

class Blizzard():

    opposite_dict =  {"v":"^", ">":"<", "^":"v", "<":">"}
    dir_dict = {"v":(0, +1), ">":(+1, 0), "^":(0, -1), "<":(-1, 0)}

    def __init__(self, coords, dir) -> None:
        
        self.coords = coords
        self.x, self.y = self.coords
        self.dir = dir

    def __repr__(self) -> str:
        return str(self.coords)+" "+self.dir
    
    def next_move(self):
        return add_vector(Blizzard.dir_dict[self.dir], self.coords)


    def move(self, limits):
        max_x, max_y = limits
        new_x, new_y = self.next_move()

        self.coords = (new_x%(max_x+1), new_y%(max_y+1))

 

        

class Maze():

    def __init__(self, blizzards, limits) -> None:
        
        self.blizzards = blizzards
        self.max_x, self.max_y = limits

        self.start = (0, -1)
        self.end = (self.max_x, self.max_y+1)
    
    def move_blizzards(self):
        for blizzard in self.blizzards:
            blizzard.move((self.max_x, self.max_y))
    
    def has_blizzard(self, coords):
        for blizzard in self.blizzards:
            if blizzard.coords == coords:
                count = [blizz.coords for blizz in self.blizzards].count(blizzard.coords)
                if count > 1:
                    return str(count)
                return blizzard.dir
        return "."
    
    def print_maze(self, player=(0, -1)):
        print("#."+"#"*(self.max_x+1))
        for y in range(self.max_y+1):
            line = "#"
            for x in range(self.max_x+1):
                line += self.has_blizzard((x, y)) if player != (x, y) else "E"
            line += "#"
            print(line)
        print("#"*(self.max_x+1)+".#")
    

def reset_blizzards(blizzards):

    new = []
    for blizzard in blizzards:
        x, y = blizzard.coords
        new.append(Blizzard((x, y), blizzard.dir))
    return new


    

max_step = float("+inf")

def find_best_path(maze:Maze, curr=(0, -1), step=0):
    global max_step

    if maze.has_blizzard(curr) != ".":
        # print("Nope, caught by blizzard at curr", curr)
        return -1
    if not (check_boundaries((curr[0], 0, maze.max_x)) and check_boundaries((curr[1], 0, maze.max_y))) and curr != maze.start and curr != maze.end:
        # print("Nope, out of bounds")
        return -1
    if step > max_step:
        return -1
    if curr == maze.end:
        print(f"ABBIAMO VINTO!!! ({step} passi)")   
        return step

    # print(curr, step)
    # maze.print_maze(curr)

    best = float("+inf")
    orig = reset_blizzards(maze.blizzards)
    for dir in list(Blizzard.dir_dict.values())+[(0, 0)]:
        maze.move_blizzards()
        new_coords = add_vector(curr, dir)
        # print(f"going {dir}")
        result = find_best_path(maze, new_coords, step+1)
        if result != -1 and result < best:
            best = result
        maze.blizzards = reset_blizzards(orig)
        
        if best < max_step:
            max_step = best

    return best

        

    


if __name__ == "__main__":

    fp = open("day24_input.txt", "r")

    line = fp.readline()
    y = 0
    blizzards = []
    while line != "":

        for x in range(len(line)):
            if line[x] in Blizzard.dir_dict.keys():
                blizzards.append(Blizzard((x-1, y-1), line[x]))
            
        y += 1
        line = fp.readline()
    
    maze = Maze(blizzards, (x-3, y-3))
    
    print(find_best_path(maze))

    fp.close()