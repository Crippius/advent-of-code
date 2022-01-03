
# https://adventofcode.com/2021/day/15

def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" and input != "\n" else 0

memo = {}



def find_best_path(map, i=0, j=0, last=(0, 0)):
    min = float("+inf")
    
    if i == len(map)-1 and j == len(map[i])-1:
        return map[i][j]
    elif (i, j) in memo:
        return memo[(i, j)]
    else:
        if i != len(map)-1:
            path = map[i][j] + find_best_path(map, i+1, j, (i, j))
            if path < min:
                min = path
            

        if j != len(map[i])-1:
            path = map[i][j] + find_best_path(map, i, j+1, (i, j))
            if path < min:
                min = path    
        
        if i != 0 and (i-1, j) != last:
            path = map[i][j] + find_best_path(map, i-1, j, (i, j))
            if path < min:
                min = path

    memo[(i, j)] = min
    return min



def main():
    input_data = open("day15_input.txt", "r")

    risk_map = []

    check = input_data.readline()
    while EOF_check(check):
        tmp = []
        for i in check[:-1]:
            tmp.append(int(i))
        risk_map.append(tmp)
        check = input_data.readline()
    print(risk_map)
    for i in range(len(risk_map)):
        risk_map[i] = risk_map[i]*5
    print(find_best_path(risk_map)-risk_map[0][0])


    

if __name__ == "__main__":
    main()