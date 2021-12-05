
# https://adventofcode.com/2021/day/5

def get_coordinates(string): # Gets coordinates from string, just a long list of manipulations in this function
    if string != "": # If not at the EOF

        string = string.split(",")
        x1 = int(string[0])
        y2 = int(string[2])
        string = string[1].split(" -> ")
        y1 = int(string[0])
        x2 = int(string[1])

        return [x1, y1], [x2, y2]

def find_vents(initial, final): # Finds the trace of the vents
    x1, y1 = initial[0], initial[1] 
    x2, y2 = final[0], final[1] # Gets coordinates from list

    positions = [(x1, y1)] # Initially inserting the first values
    if x1 == x2:
        while y1 < y2: # Continue to insert values till coordinates are equal
            y1 += 1 # Advance one step at a time to final coordinates
            positions.append((x1, y1)) # Track their trace
        while y1 > y2:
            y1 -= 1
            positions.append((x1, y1))

    elif y1 == y2: # Similar pattern as the others
        while x1 < x2:
            x1 += 1
            positions.append((x1, y1))
        while x1 > x2:
            x1 -= 1
            positions.append((x1, y1))
    
    else: # For Part 2
        while x1 < x2 and y1 < y2:
            x1 += 1 # Advancing diagonally till it reaches the final position
            y1 += 1
            positions.append((x1, y1))
        while x1 < x2 and y1 > y2:
            x1 += 1
            y1 -= 1
            positions.append((x1, y1))
        while x1 > x2 and y1 < y2:
            x1 -= 1
            y1 += 1
            positions.append((x1, y1))
        while x1 > x2 and y1 > y2:
            x1 -= 1
            y1 -= 1
            positions.append((x1, y1))

    return positions # Return line
     

def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" else 0


def main():

    input_data = open("day5_input.txt", "r")
    
    all_coordinates = [] # Where all the coordinates (start to finish) are inserted
    check = input_data.readline()
    while EOF_check(check): # Filling the list
        all_coordinates.append(get_coordinates(check))
        check = input_data.readline()


    vents = [] # Filling it with ALL the lines
    for coordinates in all_coordinates:
        vents += find_vents(coordinates[0], coordinates[1])
    
    count = 0 # Check every coordinate to see if its in the vents list more than once
    for i in set(vents): # It's very inefficient (O(2**n)?) but it works! (800 seconds for the second part :O)
        if vents.count(i) >= 2: # todo: find an efficient way for this algorythm (Really needed)
            count += 1
    
    print(f"The numbers of points in which two lines overlap is: {count}") # 5092 (Without diagonals) 20484 (With diagonals)

    input_data.close() 

    
    



if __name__ == "__main__":
    main()