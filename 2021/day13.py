
# https://adventofcode.com/2021/day/13

def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" and input != "\n" else 0

def main():

    input_data = open("day13_input.txt", "r") 

    thermal_map = []

    check = input_data.readline()
    while EOF_check(check):       # Inserting coordinates into 'thermal_map' as (x, y) couples (ex. (5, 0))
        check = check.split(",")

        x, y = int(check[0]), int(check[1])
        thermal_map.append((x, y))

        check = input_data.readline()


    instructions = []
    check = input_data.readline()
    while EOF_check(check):       # Inserting into 'instructions' (coord, position) couples (ex. ('y', 7))
        check = check.split("=")
        var, pos = check[0][-1], int(check[1])
        instructions.append((var, pos))
        check = input_data.readline()

    for var, pos in instructions:
        tmp = [] # New positions of points after X instruction

        for x, y in thermal_map: 
            if var == "y":                      # If a point was already in the right location (y < pos), pos + y - pos == y (No change)
                tmp.append((x, pos-abs(y-pos))) # Otherwise (y > pos), pos - y + pos == 2*pos - y (Reflected position relative to pos)
            if var == "x":                       
                tmp.append((pos-abs(x-pos), y)) # (Same thing with x)
        
        thermal_map = tmp # Updating position after folding

        if (var, pos) == instructions[0]: # For part 1
            print(f"The number of points after the first fold is: {len(set(thermal_map))}\n") # 802
    
    thermal_map = set(thermal_map) # Removing duplicates

    # Printing the secret code

    y_max = float("-inf") # Finding how big the code is
    x_max = float("-inf")  
    for x, y in thermal_map:
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y

    print("The secret code after following all instructions is:") # FKHFZGUB
    for y in range(y_max+1):
        render = []
        for x in range(x_max+1):
            if (x, y) not in thermal_map: # Adding '#' if in that position a point is found, otherwise a space is added 
                render.append(" ")
            else:
                render.append("#")
        print("".join(render))
    
    input_data.close()



if __name__ == "__main__":
    main()