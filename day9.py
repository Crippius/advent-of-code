
# https://adventofcode.com/2021/day/9

# Mask function for the real find_basin function
def find_basin(table, row, column): 
    return len(find_basin_mask(table, row, column, []))


# Used in Part 2, used to find how large each basin is based on the number of coordinates
def find_basin_mask(table, row, column, coords):

    coords += [(row, column)]

    # Checking if the number directily over a number is greater or not
    if row != 0 and table[row][column] < table[row-1][column] and table[row-1][column] != 9: 
        coords += find_basin_mask(table, row-1, column, coords) # If it is greater check recursively the numbers around it
    
    # Checking the number below
    if row != len(table)-1 and table[row][column] < table[row+1][column] and table[row+1][column] != 9:
        coords += find_basin_mask(table, row+1, column, coords)
    
    # Checking the number at its left
    if column != 0 and table[row][column] < table[row][column-1] and table[row][column-1] != 9:
        coords += find_basin_mask(table, row, column-1, coords)
    
    # Checking the number at its right
    if column != len(table[row])-1 and table[row][column] < table[row][column+1] and table[row][column+1] != 9:
        coords += find_basin_mask(table, row, column+1, coords)
    
    # Returning all coordinates
    return set(coords)
    

# Used in Part 1, overcomplited function to find the lowest points
def find_lowest_point(table, row, column): # You could check if all the numbers around a cell are greater, but it would be too easy,
    lowest_point_coord = []                # so this function that receives as parameters the starting position, finds the trail that goes
                                           # to the lowest point and it returns its final position

    if row != 0 and table[row][column] > table[row-1][column]: # If it can flow to the upper cell
        pointer = table[row][column]
        i=1
        while row-i != -1 and pointer > table[row-i][column]: # While it can flow in the upper direction
            pointer = table[row-i][column]
            i += 1
        lowest_point_coord += find_lowest_point(table, row-i+1, column) # See where the trail goes after that cell
    
    
    if row != len(table)-1 and table[row][column] > table[row+1][column]: # If it can flow to the cell below
        pointer = table[row][column]
        i=1
        while row+i != len(table) and pointer > table[row+i][column]:
            pointer = table[row+i][column]
            i += 1
        lowest_point_coord += find_lowest_point(table, row+i-1, column)


    if column != 0 and table[row][column] > table[row][column-1]: # If it can flow to the cell at its left
        pointer = table[row][column]
        i=1
        while column-i != -1 and pointer > table[row][column-i]:
            pointer = table[row][column-i]
            i += 1
        lowest_point_coord += find_lowest_point(table, row, column-i+1)


    if column != len(table[row])-1 and table[row][column] > table[row][column+1]: # If it can flow to the cell at its right
        pointer = table[row][column]
        i=1
        while column+i != len(table[row]) and pointer > table[row][column+i]:
            pointer = table[row][column+i]
            i += 1
        lowest_point_coord += find_lowest_point(table, row, column+i-1)
    
    
    if len(lowest_point_coord) == 0 and table[row][column] != 9: # Base case, found the lowest point
        return [(row, column)]
    

    return lowest_point_coord



def main():
    
    input_data = open("day9_input.txt", "r") # Getting data
    
    data = input_data.readlines() # Cleaning data
    heightmap = [] 
    for line in data:
        tmp = []
        for num in line[:-1]: 
            tmp.append(int(num))
        heightmap.append(tmp) 


    lowest_points = [] # Find lowest points
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            lowest_points += find_lowest_point(heightmap, i, j)
    
    lowest_points = set(lowest_points) # Removing duplicates
    
    result = 0
    for i, j in lowest_points:
        result += heightmap[i][j] + 1

    print(f"The risk levels of all low points is: {result}\n") # 548

    basins = [] # Finding basis
    for i, j in lowest_points:
        count = find_basin(heightmap, i, j)
        basins.append(count)
    
    solution = 1 # Finding three biggest basins
    for i in range(3):
        solution *= max(basins)
        basins.remove(max(basins))
    print(f"The product of the three biggest basins is: {solution}")

    input_data.close()



if __name__ == "__main__":
    main()

