# https://adventofcode.com/2021/day/6

def main():
    
    input_data = open("day6_input.txt", "r")

    lanternfish = [int(i) for i in input_data.readline().split(",")] # Inserting in list initial fish

    day_dict ={0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0} # Dividing the fish in 8 categories, depending on days before reproduction
    for fish in lanternfish:
        day_dict[fish] += 1

    for i in range(256): # For 256 days
        for j in day_dict.keys():
            if j == 0: # Save the number of fish who just reproduced 
                tmp = day_dict[j]
            else: # Decrement by a day every other fish
                day_dict[j-1] = day_dict[j]
                if j == 7: # Add to the fish that needed 7 days before reproduction the ones who just reproduced
                    day_dict[j-1] += tmp
                if j == 8: # Add to the 8th group all newborns
                    day_dict[j] = tmp
        if i == 79: # Part 1, after 80th days (considering the initial state as the first)
            result = sum([i for i in day_dict.values()])
            print(f"There are {result} lanternfish in the ocean after the 80th day\n")
    
    # Part 2
    result = sum([i for i in day_dict.values()])
    print(f"There are {result} lanternfish in the ocean after the 256 day")


# My first solution, functioning but really slow, since it counted EACH FISH every iteration
# |
# v
# def main():
#     input_data = open("day6_input.txt", "r")
#
#     lanternfish = [int(i) for i in input_data.readline().split(",")]
#     for i in range(256):
#         for j in range(len(lanternfish)):
#             lanternfish[j] -= 1
#             if lanternfish[j] == -1:
#                 lanternfish[j] = 6
#                 lanternfish.append(8)
#             if i == 79:
#                 print(len(lanternfish)) # 377030
#     print(len(lanternfish))

if __name__ == "__main__":
    main()