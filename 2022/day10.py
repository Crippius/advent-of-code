
def find_signal_strength(list_of_instr, important_cycles):
    calc_time = {"noop":1, "addx":2}
    cycle = 0
    x = 1

    signal_strengths = []

    for instr in list_of_instr:
        instr, add = instr
        for _ in range(calc_time[instr]):
            cycle += 1
            if cycle in important_cycles:
                signal_strengths.append(x*cycle)
        x += add
    return signal_strengths

def draw_pixels(list_of_instr, width=3):
    calc_time = {"noop":1, "addx":2}

    cycle = 0
    x = 1

    pixels = []
    row = []
    for instr in list_of_instr:
        instr, add = instr
        for _ in range(calc_time[instr]):
            if cycle%40 in range(x-width//2, 1+x+width//2):
                row.append("#")
            else:
                row.append(" ")
            cycle += 1
            if not cycle%40:
                pixels.append(row)
                row = [] 
            
        x += add
    return pixels

if __name__ == "__main__":

    fp = open("day10_input.txt", "r")

    list_of_instr = []

    instr = fp.readline()
    while instr != "":
        instr = instr[:-1]
        if instr == "noop":
            list_of_instr.append((instr, 0))
        else:
            instr, times = instr.split()
            list_of_instr.append((instr, int(times)))
        instr = fp.readline()

    important_cycles = [20, 60, 100, 140, 180, 220]
    print(f"The sum of the signal strengths in the specific cycles is: {sum(find_signal_strength(list_of_instr, important_cycles))}")

    print("The final drawing of the CRT is:")
    for i in draw_pixels(list_of_instr):
        print("".join(i))

    fp.close()