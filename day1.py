
# https://adventofcode.com/2021/day/1

def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" else 0

def main():

    # Opening the input file on read mode
    with open("day1_input.txt", "r") as input_data:
        # Part 1

        count = 0     # Initializations
        check = "foo" # (Temporary string to enter the while loop)

        previous = int(input_data.readline()) # Reading first lines
        depth = int(input_data.readline())

        while EOF_check(check):
            if previous < depth:
                count += 1
            
            check = input_data.readline() # 'check' reads line before assigning it to depth to check if the EOF was reached
            if EOF_check(check): # Assigning new data before restarting the while loop
                previous = depth    
                depth = int(check)
            

        print(f"Solution Part 1: There are {count} measurements larger than the previous one\n") # 1688
        input_data.close()
    
    with open("day1_input.txt", "r") as input_data:
        # Part 2

        count = 0  # Same initializations
        check = "foo"

        previous = [int(input_data.readline()), int(input_data.readline()), int(input_data.readline())]
        depth = [previous[1], previous[2], int(input_data.readline())] # Using lists to compare triplets
    

        while EOF_check(check):
            if sum(previous) < sum(depth):
                count += 1
            
            check = input_data.readline() # Same thing as part 1
            if EOF_check(check):
                previous = depth
                depth = [depth[1], depth[2], int(check)]

        print("Solution Part 2: There are %d sums larger than the previous one" % count) # 1728

        input_data.close()


# Initial solution, correct but used a giant list to store all data, new one stores only the necessary with limited memory
# |
# v

# def main():

#     with open("C:/Users/cripp/Google Drive/programming/advent of code 2021/day1_input.txt", "r") as input_data:
#         # Part 1
#         count = 0
#         depths = input_data.readlines()

#         depths = [int(i[:-1]) for i in depths]
#         for i in range(1, len(depths)):
#             if depths[i-1] < depths[i]:
#                 count += 1

#         # 1688 (Completed)
#         print("Solution Part 1: There are %d measurements larger than the previous one\n" % count)

#         # Part 2
#         multi_depths = []
#         for i in range(1, len(depths)-1):
#             multi_depths.append([depths[i-1], depths[i], depths[i+1]])

#         count = 0
#         for i in range(1, len(multi_depths)):
#             print(multi_depths[i-1], multi_depths[i],
#                   1 if sum(multi_depths[i-1]) < sum(multi_depths[i]) else 0)
#             if sum(multi_depths[i-1]) < sum(multi_depths[i]):
#                 count += 1

#         # 1728 (Completed)
#         print("Solution Part 2: There are %d sums larger than the previous one\n" % count)

#         input_data.close()



if __name__ == "__main__":
    main()
