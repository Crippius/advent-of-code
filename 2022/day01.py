
def best_n(elves, n):
    best = [0]*n
    for elf in elves:
        for i, best_i in enumerate(best):
            if elf > best_i:
                for j in range(1, i+1):
                    best[j-1] = best[j]
                best[i] = elf
    return best



if __name__ == "__main__":
    fp = open("day01_input.txt", "r")

    line = fp.readline()

    elves = []
    while line != "":
        weights = [int(line)]
        line = fp.readline()
        while line != "\n" and line != "":
            weights.append(int(line))
            line = fp.readline()
        elves.append(sum(weights))
        line = fp.readline()
    
    print(f"The elf that has the most Calories carries: {max(elves)} Calories")
    
    print(f"The top three elves carry: {sum(best_n(elves, 3))} Calories")

    fp.close()