
# https://adventofcode.com/2021/day/22



def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != ""  and input != "\n" else 0

on_off_struct = {"on":1, "off":0}

def main():
    
    input_data = open("day22_input.txt", "r")

    
    reactor_map = {}
    check = input_data.readline()
    while EOF_check(check):

        on_off = check[:check.find(" ")]
        xi = int(check[check.find("=")+1:check.find(".")])
        xf = int(check[check.find(".")+2:check.find(",")])
        check = check[check.find(",")+1:]
        yi = int(check[check.find("=")+1:check.find(".")])
        yf = int(check[check.find(".")+2:check.find(",")])
        check = check[check.find(",")+1:]
        zi = int(check[check.find("=")+1:check.find(".")])
        zf = int(check[check.find(".")+2:check.find(",")])

        for x in range(xi, xf+1):
            for y in range(yi, yf+1):
                for z in range(zi, zf+1):
                    if (x, y, z) not in reactor_map:
                        reactor_map[(x, y, z)] = 0
                    reactor_map[(x, y, z)] = on_off_struct[on_off]

        check = input_data.readline()
    counter = 0
    for i in reactor_map.keys():
        counter += reactor_map[i]
    print(counter)
    for x in range(xi, xf+1):
            for y in range(yi, yf+1):
                for z in range(zi, zf+1):
                    if (x, y, z) not in reactor_map:
                        reactor_map[(x, y, z)] = 0
                    reactor_map[(x, y, z)] = on_off_struct[on_off]
    
    check = input_data.readline()
    while EOF_check(check):
        on_off = check[:check.find(" ")]
        xi = int(check[check.find("=")+1:check.find(".")])
        xf = int(check[check.find(".")+2:check.find(",")])
        check = check[check.find(",")+1:]
        yi = int(check[check.find("=")+1:check.find(".")])
        yf = int(check[check.find(".")+2:check.find(",")])
        check = check[check.find(",")+1:]
        zi = int(check[check.find("=")+1:check.find(".")])
        zf = int(check[check.find(".")+2:check.find(",")])

        for x in range(xi, xf+1):
            for y in range(yi, yf+1):
                for z in range(zi, zf+1):
                    if (x, y, z) not in reactor_map:
                        reactor_map[(x, y, z)] = 0
                    reactor_map[(x, y, z)] = on_off_struct[on_off]
    counter = 0
    for i in reactor_map.keys():
        counter += reactor_map[i]
    print(counter)

if __name__ == "__main__":
    main()
