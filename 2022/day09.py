
def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0

def vector_sub(arg1, arg2):
    if len(arg1) != len(arg2):
        raise Exception
    
    new_vector = []
    for i in range(len(arg1)):
        new_vector.append(arg1[i]-arg2[i])
    return tuple(new_vector)

class Rope():

    def __init__(self):
        
        self.head_x = 0
        self.head_y = 0
        self.tail_x = 0
        self.tail_y = 0
    
    def move(self, dir):

        self.head_x += dir[0]
        self.head_y += dir[1]

        return self.move_tail()

    def move_tail(self):
        x_diff = self.head_x-self.tail_x
        y_diff = self.head_y-self.tail_y

        if abs(x_diff)+abs(y_diff) >= 3 or abs(x_diff) == 2 or abs(y_diff) == 2:
            self.tail_x += sign(x_diff)
            self.tail_y += sign(y_diff)
            return (sign(x_diff), sign(y_diff))
        return (0, 0)

    def head_coords(self):
        return (self.head_x, self.head_y)
    def tail_coords(self):
        return (self.tail_x, self.tail_y)



def exec_instr(lst, length=1):

    dir_dict = {"U":(0, 1), "D":(0, -1), "R":(1, 0), "L":(-1, 0)}

    rope = []
    for i in range(length):
        rope.append(Rope())
    
    positions = []

    for instr in lst:
        dir, times = instr
        dir = dir_dict[dir]
        orig = dir

        for i in range(times):
            for part in range(len(rope)):
                dir = rope[part].move(dir)
            positions.append(rope[-1].tail_coords())
            dir = orig
    
    return set(positions)



if __name__ == "__main__":

    fp = open("day09_input.txt", "r")

    list_of_instr = []
    instr = fp.readline()
    while instr != "":
        dir, times = instr.split()
        list_of_instr.append((dir, int(times)))

        instr = fp.readline()
    
    print(f"The tail of the rope with length 1 has moved in: {len(exec_instr(list_of_instr, length=1))} different positions")

    print(f"The tail of the rope with length 9 has moved in: {len(exec_instr(list_of_instr, length=9))} different positions")

    fp.close()