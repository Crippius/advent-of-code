
# https://adventofcode.com/2021/day/2

def main():

    # Opening file on read mode
    with open("day02_input.txt", "r") as input_data:
        # Part 1

        forward = 0 # Initializations
        depth = 0

        input = input_data.readline()

        while input != "": # While program has not reached EOF

            input = input.split(" ") # input = [<direction>, <space>]

            if input[0] == "forward":
                forward += int(input[1])

            elif input[0] == "up":
                depth -= int(input[1])

            else:
                depth += int(input[1])
        
            input = input_data.readline()

        solution = forward*depth
        print(f"Solution Part 1: There final forward position multiplied by the final depth is: {solution}\n") # 1635930 
        
        input_data.close()
    
    with open("day02_input.txt", "r") as input_data:
        # Part 2

        forward = 0 # Initializations
        depth = 0
        aim = 0

        input = input_data.readline()

        while input != "": # Almost same thing as part 1
            input = input.split(" ")

            if input[0] == "forward":
                forward += int(input[1])
                depth += aim*int(input[1])

            elif input[0] == "up":
                aim -= int(input[1])
                
            else:
                aim += int(input[1])
        
            input = input_data.readline()

        solution = forward*depth
        print(f"Solution Part 2: There final forward position multiplied by the final depth (revised) is: {solution}") # 1781819478

        input_data.close()



if __name__ == "__main__":
    main()