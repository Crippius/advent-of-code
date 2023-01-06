from day12 import add_vector
from time import sleep
def area(x, y):
    return (x[1]-x[0])*(y[1]-y[0])

def intercept(*args):
    lst = list(tuple(args[0]))
    for arg in args[1:]:
        new = []
        for i in lst:
            if i in arg:
                new.append(i)
        lst = new
    return lst

class Elf():

    move_dict = {"X":(0, 0), "N":(0, -1), "S":(0, +1), "W":(-1, 0), "E":(+1, 0)}

    def __init__(self, coords) -> None:
        
        self.coords = coords
        self.x, self.y = coords
        self.dirs = ["N", "S", "W", "E"]
        self.proposed_move = self.dirs[0]



    def get_dirs(self, dir="X"):

        dir_dict = {"X":(-1, 1, -1, 1), "N":(-1, 1, -1, -1), "S":(-1, 1, 1, 1), "W":(-1, -1, -1, 1), "E":(1, 1, -1, 1)}
        
        x_min, x_max, y_min, y_max = dir_dict[dir]

        dirs = []
        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max+1):
                dirs.append((self.x+x, self.y+y))
        if dir == "X":
            dirs.remove(self.coords)
        return dirs
    
    def move_elf(self, coords):
        self.coords = coords
        self.x, self.y = self.coords

    def reset_dirs(self):
        self.dirs = self.dirs[1:] + [self.dirs[0]]
        self.proposed_move = self.dirs[0]
    
    def change_dir(self):
        index = self.dirs.index(self.proposed_move)
        self.proposed_move = self.dirs[(index+1)%len(self.dirs)]
    
    def propose_move(self, forced=False):

        if not forced:
            next_step = add_vector(self.coords, Elf.move_dict[self.proposed_move])
            self.change_dir()
        else:
            next_step = add_vector(self.coords, Elf.move_dict[forced])

        return next_step
        


    

class Group_of_Elves():

    def __init__(self, elves) -> None:
        self.elves = elves
    
    def move_elves(self):

        orig = [elf.coords for elf in self.elves]

        proposed_moves = []
        for elf in self.elves:
            if not len(intercept(orig, elf.get_dirs("X"))):
                proposed_moves.append(elf.coords)
                continue
                
            found = False
            for _ in range(4):
                if not len(intercept(orig, elf.get_dirs(elf.proposed_move))):
                    # print(elf.coords, "Proposing:", elf.proposed_move)
                    proposed_moves.append(elf.propose_move())
                    found = True
                    break
                else:
                    elf.change_dir()

            if not found:
                proposed_moves.append(elf.coords)
        
        moved = False
        for i, coords in enumerate(proposed_moves):
            self.elves[i].reset_dirs()
            if proposed_moves.count(coords) == 1:
                if coords != self.elves[i].coords:
                    moved = True
                self.elves[i].move_elf(coords)
        
        return moved
        
    def print_ground(self):
        x_min, x_max = min([elf.x for elf in self.elves]), max([elf.x for elf in self.elves])
        y_min, y_max = min([elf.y for elf in self.elves]), max([elf.y for elf in self.elves])

        lst_of_coords = [elf.coords for elf in self.elves]
        for y in range(y_min-1, y_max+2):
            print(f"{y}\t", end="")
            for x in range(x_min-1, x_max+2):
                print("# " if (x, y) in lst_of_coords else ". ", end="")
            print()
        print()
    
    def get_limits(self):
        x_min, x_max = min([elf.x for elf in self.elves]), max([elf.x for elf in self.elves])
        y_min, y_max = min([elf.y for elf in self.elves]), max([elf.y for elf in self.elves])
        return x_min, x_max, y_min, y_max 
    


if __name__ == "__main__":

    fp = open("day23_input.txt", "r")


    elves = []

    y = 0
    line = fp.readline()
    while line != "":
        for x in range(len(line)):
            if line[x] == "#":
                elves.append(Elf((x, y)))

        y += 1
        line = fp.readline()

    elves = Group_of_Elves(elves)

    # elves.print_ground()
    round = 0
    while True:
        round += 1
        moved = elves.move_elves()
        # elves.print_ground()
        if round == 10:
            x_min, x_max, y_min, y_max = elves.get_limits()
            print("empty tiles:",area((x_min, x_max+1), (y_min, y_max+1))-len(elves.elves))

        if not moved:
            print("not moved at round:", round)
            break


    
    
    


    fp.close()