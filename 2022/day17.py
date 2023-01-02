from time import sleep


class Block():

    def __init__(self, i, offset) -> None:

        type_of_blocks = [[(2, 0), (3, 0), (4, 0), (5, 0)],         # Horizontal Block
                          [(2, 1), (3, 0), (3, 1), (3, 2), (4, 1)], # Plus Block
                          [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)], # _| Block
                          [(2, 0), (2, 1), (2, 2), (2, 3)],         # Vertical Block
                          [(2, 0), (3, 0), (2, 1), (3, 1)]]         # Cube Block

        self.blocks = [(x, y+offset) for x, y in type_of_blocks[i]]
    
    def can_drop(self, obstables):
        for x, y in self.blocks:
            if (x, y-1) in obstables:
                return False
        return True
    
    def drop(self):
        self.blocks = [(x, y-1) for x, y in self.blocks]

    def can_move(self, dir, obstacles, boundaries):
        dir_dict = {"<":-1, ">":+1}

        for x, y in self.blocks:
            if (x+dir_dict[dir], y) in obstacles or not (x+dir_dict[dir] in range(boundaries[0], boundaries[1])):
                return False
        return True

    def move(self, dir):

        dir_dict = {"<":-1, ">":+1}

        self.blocks = [(x+dir_dict[dir], y) for x, y in self.blocks]

class Wind():

    def __init__(self, flow) -> None:
        self.flow = flow
        self.curr = 0
    
    def get_flow(self):
        dir = self.flow[self.curr]
        self.curr = (self.curr+1)%len(self.flow)
        return dir

class Chamber():

    def __init__(self) -> None:
    
        self.y_boundaries = (0, 6+1)

        self.blocks = [(i, 0) for i in range(self.y_boundaries[0], self.y_boundaries[1])]

        self.max_heights = [0 for i in range(self.y_boundaries[0], self.y_boundaries[1])]

    def show_cavern(self, more=[]):

        min_x = min(i[0] for i in self.blocks+more)
        min_y = min(i[1] for i in self.blocks+more)
        max_x = max(i[0] for i in self.blocks+more)
        max_y = max(i[1] for i in self.blocks+more)

        for y in reversed(list(range(min_y, max_y+2))):
            for x in range(min_x, max_x+1):
                print("#" if (x, y) in self.blocks+more else ".", end="")
            print()

    def max_height(self):
        return max(self.max_heights) 

    def add_elements(self, new_block:Block):

        for x, y in new_block.blocks:
            self.blocks.append((x, y))
            if y > self.max_heights[x]:
                self.max_heights[x] = y

    def drop_block(self, block:Block, wind:Wind):
        while True: # Why doesn't Python have do-while loops???
            dir = wind.get_flow()

            if block.can_move(dir, self.blocks, self.y_boundaries):
                block.move(dir)
            
            if not block.can_drop(self.blocks):
                break
            block.drop()
        
        self.add_elements(block)

    

if __name__ == "__main__":

    fp = open("day17_input.txt", "r")

    flow = fp.readline()

    wind = Wind(flow)
    chamber = Chamber()

    period = 1

    while ((len(wind.flow)*period) % 5):
        period += 1
    
    found_cycle = False
 
    cycle_blocks_dict = {}
    height_dict = {}

    times = 1000000000000
    for i in range(times):
        block = Block(i%5, 3+1+chamber.max_height())  

        if not (i % (period*len(wind.flow))): # Same starting input and block
            last_blocks = [x for x, y in chamber.blocks[-30*6:]]
            for cycle, cycle_blocks in cycle_blocks_dict.items():

    
                if cycle_blocks == last_blocks:
                    period = i-cycle
                    found_cycle = True
                    height_dict[i] = chamber.max_height()
                    break
            if found_cycle:
                break
            cycle_blocks_dict[i] = last_blocks
            height_dict[i] = chamber.max_height()

        chamber.drop_block(block, wind)

        

        if i == 2022:
            print(chamber.max_height())

    total = chamber.max_height()
    total = (height_dict[i]-height_dict[i-period])*((times-i)//period)

    last_cycles = (times-i)%period
    for i in range(last_cycles):
        block = Block(i%5, 3+1+chamber.max_height())  
        chamber.drop_block(block, wind)

    total += chamber.max_height()
    print(total)

    fp.close()