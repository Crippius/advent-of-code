
priority_points = {}

def find_common(*strings):
    for letter in strings[0]:
        for string in strings[1:]:
            if letter not in string:
                continue
        return priority_points[letter]

    raise Exception(f"OMG Something went wrong with {strings} plz help")

if __name__ == "__main__":

    fp = open("day03_input.txt", "r")

    line = fp.readline()

    rucksacks = []
    while line != "":
        rucksacks.append(line)
        line = fp.readline()

    for i, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
        priority_points[letter] = i+1
        priority_points[letter.upper()] = i+1+26
    
    priority = 0
    for i in rucksacks:
        first, second = i[:len(i)//2], i[len(i)//2:]
        priority += find_common(first, second)

    print(f"The sum of the priorities of the duplicate items is: {priority}")

    groups = [(rucksacks[i], rucksacks[i+1], rucksacks[i+2]) for i in range(len(rucksacks)) if not i%3]

    priority = 0
    for x, y, z in groups:
        priority += find_common(x, y, z)

    print(f"The sum of the priorities of the elves badges is: {priority}")
    
    fp.close()