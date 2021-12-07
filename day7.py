
# https://adventofcode.com/2021/day/7

def mean(lst):
    return sum(lst)//len(lst)


# Used for Part 2
def summarial(value): # Calculating factorial but using + instead of *
    count = 0
    while value != 0:
        count += value
        value -= 1
    return count # Recursion not possible because numbers given are too big (with 1000+ function calls the program stops)


def main():

    input_data = open("day7_input.txt", "r") # Getting data and cleaning it
    nums = [int(i) for i in input_data.readline().split(",")]

    # N.B Part 1 and 2 done in parallel

    minimum1 = float("+inf") # Starting with maximum value possible as minimum
    minimum2 = float("+inf")

    for i in range(mean(nums)-1, mean(nums)+1): # Minimum value is in the range around the mean, as of this paper 
        tmp1 = 0                       # https://cdn.discordapp.com/attachments/541932275068174359/917782745894256640/crab-submarines.pdf
        tmp2 = 0
        for j in nums: # Calculating the amount of fuel needed to get to align:
            tmp1 += abs(i-j) # using human engineering
            tmp2 += summarial(abs(i-j)) # using crab engineering

            if tmp1 > minimum1 and tmp2 > minimum2: # If both tmps are already greater than their minimum don't bother continuing
                break

        if minimum1 > tmp1: # If tmp is lower than minimum, replace iti
            minimum1 = tmp1
        if minimum2 > tmp2:
            minimum2 = tmp2

    print(f"{minimum1} fuel was used to align using human engineering\n") # 336040
    print(f"{minimum2} fuel was used to align using crab engineering") # 94813675



if __name__ == "__main__":
    main()