
def init_crates(fp):
    
    line = fp.readline()
    num_columns = len(line)//4

    crates = [[] for _ in range(num_columns)]

    while line != "\n":

        for i in range(num_columns):
            if line[i*4] == "[":
                crates[i].append(line[(i*4)+1])

        line = fp.readline()

    return crates

def cratemover(crates, much, fr, to, version="9000"):

    if version == "9000":
        crates[to-1] = list(reversed(crates[fr-1][:much]))+crates[to-1]
    elif version == "9001":
        crates[to-1] = crates[fr-1][:much]+crates[to-1]

    crates[fr-1] = crates[fr-1][much:]

    return crates


if __name__ == "__main__":
    
    fp = open("day05_input.txt", "r")

    crates1 = init_crates(fp)

    crates2 = list(tuple(crates1))    

    line = fp.readline()

    much, fr, to = 0, 0, 0

    while line != "":

        _, much, _, fr, _, to = line.split()
        much, fr, to = int(much), int(fr), int(to)

        crates1 = cratemover(crates1, much, fr, to, version="9000")

        crates2 = cratemover(crates2, much, fr, to, version="9001")

        line = fp.readline()


    print(f'The crates that end up at the top of the stack using CrateMover 9000 are: {"".join([i[0] for i in crates1])}')
    print(f'The crates that end up at the top of the stack using CrateMover 9001 are: {"".join([i[0] for i in crates2])}')
    
    fp.close()