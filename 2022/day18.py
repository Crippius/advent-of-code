from day12 import add_vector

def adj_cubes(cube):
    directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    return [add_vector(cube, direction) for direction in directions]

if __name__ == "__main__":

    fp = open("day18_input.txt")

    cubes = []
    cube = fp.readline()
    while cube != "":
        cube = tuple(map(int, cube.split(",")))
        cubes.append(cube)
        cube = fp.readline()

    surface_area = 0
    for cube in cubes:
        for new_cube in adj_cubes(cube):
            if not (new_cube in cubes):
                surface_area += 1
    
    print(surface_area)

    all_x, all_y, all_z = zip(*cubes)

    minx, maxx = min(all_x), max(all_x)
    miny, maxy = min(all_y), max(all_y)
    minz, maxz = min(all_z), max(all_z)
    all_cubes = [(x,y,z) for x in range(minx-1,maxx+2) for y in range(miny-1,maxy+2) for z in range(minz-1,maxz+2)]

    empty_cubes = list(tuple((all_cubes)))
    for cube in cubes:
        empty_cubes.remove(cube)

    visited = [(minx-1, miny-1, minz-1)]
    while visited != []:
        new_cube = visited.pop()
        if new_cube in empty_cubes:
            empty_cubes.remove(new_cube)
            visited += adj_cubes(new_cube)
    
    exterior_surface_area = surface_area
    for remaining_cube in empty_cubes: # Not reachable == empty cubes inside set of cubes that contains them
        for new_cube in adj_cubes(remaining_cube):
            if new_cube in cubes:
                exterior_surface_area -= 1
    
    print(exterior_surface_area)

    fp.close()