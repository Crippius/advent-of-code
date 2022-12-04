
if __name__ == "__main__":

    fp = open("day04_input.txt", "r")

    line = fp.readline()

    pair_sections = []
    while line != "":
        first, second  = line.split(",")
        s1, e1, s2, e2 = map(int, first.split("-")+second.split("-"))

        pair_sections.append(((s1, e1), (s2, e2)))
        line = fp.readline()
    
    counter_1 = 0
    counter_2 = 0
    for first, second in pair_sections:
        s1, e1 = first
        s2, e2 = second
        if (s1 in range(s2, e2+1) and e1 in range(s2, e2+1)) or (s2 in range(s1, e1+1) and e2 in range(s1, e1+1)):
            counter_1 += 1
        if (s1 in range(s2, e2+1) or e1 in range(s2, e2+1)) or (s2 in range(s1, e1+1) or e2 in range(s1, e1+1)):
            counter_2 += 1
    
    print(f"The number of pairs where one range fully contains the other is: {counter_1}")
    
    print(f"The number of pairs where one range overlaps the other is: {counter_2}")
    
    fp.close()