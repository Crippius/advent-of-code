def sign(x):
    return 1 if x > 0 else -1

class Sand():

    def __init__(self):
        
        self.start = (500, 0)
        self.pos = self.start
        self.next_pos = self.pos
    
    def drop(self):
        
        self.pos = self.next_pos

    def can_drop(self, grid):

        x, y = self.pos
        for possible_pos in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
            if possible_pos not in grid:
                self.next_pos = possible_pos
                return True
        return False
    
    def depth(self):
        return self.pos[1]
         

class Cave():

    def __init__(self, rocks, max_depth):

        self.blocks = rocks
        self.max_depth = max_depth
        self.sand_particles = 0

        self.is_full = False
        self.reached_floor = False


    def produce_sand(self):

        self.sand_particles += 1
        sand = Sand()
        while sand.can_drop(self.blocks) and sand.depth() < self.max_depth+1:
            sand.drop()
        
        self.blocks.append(sand.pos)

        if sand.pos == sand.start:
            self.is_full = True

        return sand.depth()


    def show_cavern(self):

        min_x = min(i[0] for i in self.blocks)
        min_y = min(i[1] for i in self.blocks)
        max_x = max(i[0] for i in self.blocks)
        max_y = max(i[1] for i in self.blocks)

        for y in range(min_y-1, max_y+2):
            for x in range(min_x-1, max_x+2):
                print("#" if (x, y) in self.blocks else ".", end="")
            print()



if __name__ == "__main__":

    fp = open("day14_input.txt", "r")

    rocks = []
    max_depth = 0

    set_of_rocks = fp.readline()
    while set_of_rocks != "":
        set_of_rocks = set_of_rocks.split(" -> ")
        for i_rocks in range(len(set_of_rocks)-1):
            x_start, y_start = map(int, set_of_rocks[i_rocks].split(","))
            x_end, y_end = map(int, set_of_rocks[i_rocks+1].split(","))

            x_start, x_end = min(x_start, x_end), max(x_start, x_end)
            y_start, y_end = min(y_start, y_end), max(y_start, y_end)

            for x_tmp in range(x_start, x_end+1):
                rocks.append((x_tmp, y_start))
            for y_tmp in range(y_start, y_end+1):
                rocks.append((x_start, y_tmp))             
            
            if max(y_start, y_end) > max_depth:
                max_depth = max(y_start, y_end)

        set_of_rocks = fp.readline()

    rocks = list(set(rocks))

    cave = Cave(rocks, max_depth)

    while not cave.is_full:
        sand_depth = cave.produce_sand()

        if sand_depth > cave.max_depth and not cave.reached_floor:
            print(f"The number of sand particles to reach the floor is: {cave.sand_particles-1}")
            cave.reached_floor = True

    print(f"The number of sand particles to fill the hole is: {cave.sand_particles}")

    fp.close()