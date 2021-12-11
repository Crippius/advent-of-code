# https://adventofcode.com/2021/day/11

def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" else 0

def flash(table, i, j): # Increments every number in the table except for the placeholders
    
    if table[i][j] != -1:
        table[i][j] += 1
    return table


def check_flash(table): # Checks if a flash (num >= 10) happened during a particular iteration
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] >= 10:
                return 1
    return 0 # Returns 1 if a flash has been found, 0 otherwise



def main():
    
    input_data = open("day11_input.txt", "r") # Getting inputs and inserting them to 'octos' list

    octos = []

    check = input_data.readline()
    while EOF_check(check):
        octos.append([int(i) for i in check if i != "\n"])
        check = input_data.readline()
    
    # Initializations
    total_octos = len(octos) * len(octos[0]) # Total number of Dumbo octopuses (100)
    flashes = 0 # Number of flashes after X generations
    part2_check = 0 # Check condition for breaking out of the loop

    gen = 0
    while True: # While a generation where every octopus flashes has been found
        
        gen_flashes = 0 # Number of flashes for a single generation

        for i in range(len(octos)): # Incrementing every number by 1
            for j in range(len(octos[i])):
                octos = flash(octos, i, j)
      
        while check_flash(octos): # While a number >= 10 is found in the list
            
            tmp = [] # Temporary list to store the coordinates where an octopus flashes

            for i in range(len(octos)):
                for j in range(len(octos[i])):
                    if octos[i][j] >= 10: 
                        octos[i][j] = -1   # If the octopus flashes (num >= 10) substitute them with a placeholder (-1)
                        tmp.append([i, j]) # and store its coordinates in temporary list

            for i, j in tmp: # Now for every octopus that has flashed...

                start_i = -1 if i != 0 else 0 
                end_i = 1 if i != len(octos)-1 else 0
                                                        # (Conditions to avoid edge cases)
                start_j = -1 if j != 0 else 0
                end_j = 1 if j != len(octos[i])-1 else 0

                for row in range(start_i, end_i+1):
                    for col in range(start_j, end_j+1):
                        octos = flash(octos, i+row, j+col) # ... increment every number around these coordinates

        for i in octos:
            gen_flashes += i.count(-1) # Count the number of octopus that have flashed
        flashes += gen_flashes         # And add it to the counter

        gen += 1 # Commence a new generation and set all placeholders to 0
        octos = [[j if j != -1 else 0 for j in i] for i in octos]
        
        if gen == 100: # Result for part 1
            print(f"The total number of flashes after 100 steps is {flashes}\n") #  1625
            if part2_check == 1:
                break

        if gen_flashes == total_octos: # Result for part 2
            part2_check = 1
            print(f"The first step where all octopuses flash together is: the {gen}th one") # 243
            if gen >= 100:
                break
    
    input_data.close()


if __name__ == "__main__":
    main()


# One of my first approaches that used recursion and I really liked, but unfortunately couldn't handle some exceptions, 
# like the flashes on the row before the current one and that were caused by another, different flash
# |
# v
# def flash(table, i, j):

#     if table[i][j] != -1:
#         table[i][j] += 1

#     if table[i][j] >= 10:

#         table[i][j] = 0 

#         start_i = -1 if i != 0 else 0
#         end_i = 1 if i != len(table) else 0

#         start_j = -1 if j != 0 else 0
#         end_j = 1 if j != len(table[i]) else 0

#         for row in range(start_i, end_i):
#             for col in range(start_j, end_j):
#                 table = flash(table, i+row, j+col)

#     return table