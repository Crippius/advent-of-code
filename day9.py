
# https://adventofcode.com/2021/day/9

def remove_dups(lst, coordinates):
    for i in coordinates:
        if i not in lst:
            lst.append(i)
    return lst

def find_basin(table, row, column): 
    return len(find_basin_mask(table, row, column, []))

def find_basin_mask(table, row, column, coords):

    coords += [(row, column)]

    if row != 0 and table[row][column] < table[row-1][column] and table[row-1][column] != 9:
        coords = remove_dups(coords, find_basin_mask(table, row-1, column, coords))

    if row != len(table)-1 and table[row][column] < table[row+1][column] and table[row+1][column] != 9:
        coords = remove_dups(coords, find_basin_mask(table, row+1, column, coords))
        

    if column != 0 and table[row][column] < table[row][column-1] and table[row][column-1] != 9:
        coords = remove_dups(coords, find_basin_mask(table, row, column-1, coords))
        
    if column != len(table[row])-1 and table[row][column] < table[row][column+1] and table[row][column+1] != 9:
        coords = remove_dups(coords, find_basin_mask(table, row, column+1, coords))

    return set(coords)
    

def find_lowest_point(table, row, column):
    lowest_point_coord = []

    if row != 0 and table[row][column] > table[row-1][column]:
        pointer = table[row][column]
        i=1
        while row-i != -1 and pointer > table[row-i][column]:
            pointer = table[row-i][column]
            i += 1
        lowest_point_coord += find_lowest_point(table, row-i+1, column)
    
    
    if row != len(table)-1 and table[row][column] > table[row+1][column]:
        pointer = table[row][column]
        i=1
        while row+i != len(table) and pointer > table[row+i][column]:
            pointer = table[row+i][column]
            i += 1
        lowest_point_coord += find_lowest_point(table, row+i-1, column)


    if column != 0 and table[row][column] > table[row][column-1]:
        pointer = table[row][column]
        i=1
        while column-i != -1 and pointer > table[row][column-i]:
            pointer = table[row][column-i]
            i += 1
        lowest_point_coord += find_lowest_point(table, row, column-i+1)

    if column != len(table[row])-1 and table[row][column] > table[row][column+1]:
        pointer = table[row][column]
        i=1
        while column+i != len(table[row]) and pointer > table[row][column+i]:
            pointer = table[row][column+i]
            i += 1
        lowest_point_coord += find_lowest_point(table, row, column+i-1)
    
    
    if len(lowest_point_coord) == 0 and table[row][column] != 9:
        return [(row, column)]
    
    return lowest_point_coord




def main():
    
    input_data = open("day9_input.txt", "r")
    
    
    data = input_data.readlines()
    heightmap = [] 
    for line in data:
        tmp = []
        for num in line[:-1]: 
            tmp.append(int(num))
        heightmap.append(tmp)

    lowest_points = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[i])):
            lowest_points = remove_dups(lowest_points, find_lowest_point(heightmap, i, j))

    result = 0
    for i, j in lowest_points:
        result += heightmap[i][j] + 1
    print(result)

    basins = []
    for i, j in lowest_points:
        count = find_basin(heightmap, i, j)
        basins.append(count)
    
    solution = 1
    for i in range(3):
        solution *= max(basins)
        basins.remove(max(basins))
    print(solution)



if __name__ == "__main__":
    main()

