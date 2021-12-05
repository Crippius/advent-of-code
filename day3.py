
# https://adventofcode.com/2021/day/3

def my_round(value): # Python's built in function 'round()' rounded 0.5 to a zero, while in this exercise I needed it to become a 1
    return 1 if value >= 0.5 else 0   # So I created my own round function (that only works with values between 0 and 1)

def bin_to_dec(bin_num): # Converts a binary number into a decimal one
    dec = 0

    for i in range(0, len(bin_num)):
        dec += int(bin_num[i])*(2**(len(bin_num)-i-1))
    
    return dec

def find_criteria_report(inputs, criteria): # Function for part 2
                                # Parameters: 'inputs', the input data, and 'criteria', == 1 if I want to get the most common value 
    conditions = []                                                                   # == 0 if I want to get the least common one
    count = 0           # Initializations
    candidates = inputs
    while len(candidates) != 1: # While the candidate has not been found
        tmp = []
        count = 0
        for candidate in candidates:
            check = 1
            for j in range(len(conditions)):
                if candidate[j] != conditions[j]:
                    check = 0

            if check == 1:  # If the candidate follows all conditions it passes the next round
                tmp.append(candidate)
                count += 1

        if len(conditions) != len(tmp[0]):  # An if condition to get around the edge case in which two candidates have  
            result = my_round(sum([int(i[len(conditions)]) for i in tmp])/count) # an equal number of characters but the last one

        max = result if criteria == 1 else 1-result # Where the criteria is involved
        conditions.append(str(max)) # Added new condition to the list
        candidates = tmp # Checking the remaining candidates
    
    return candidates[0] # Return the last candidate

def main(): 

    # Part 1
    input_data = open("day3_input.txt", "r")
        
        
    byte = input_data.readline()[:-1]   # Initializations
    length = len(byte)  
    counter = [0 for i in range(0, length)] # [0, 0, ..., 0]
    total = 0

    while byte != "": # While not at EOF
        for i in range (0, length):    # If byte[i] == 0, counter is not affected, otherwise it's incremented by 1
            counter[i] += int(byte[i])
        total += 1
        byte = input_data.readline()[:-1]

    for i in range (length):  # If there were more 0s than 1s, the mean is < than 0.5 so it's rounded down to 0 (The mode)
        counter[i] = str(round(counter[i]/total)) # Otherwise the mean is > than 0.5 so it's rounded up to 1

    gamma = "".join(counter) # 010100111001
    gamma = bin_to_dec(gamma) # 1337

    epsilon = [] # Finding epsilon...
    for i in range(length):
        epsilon.append("1" if counter[i] == "0" else "0")

    epsilon = "".join(epsilon) # 101011000110
    epsilon = bin_to_dec(epsilon) # 2758

    solution = gamma * epsilon
    print(f"The power consumption of the submarine is: {solution}\n") # 3687446

    # Part 2
    input_data.seek(0)

    # Todo: correct answer with limited memory
    inputs = [i[:-1] for i in input_data.readlines()] # Getting ALL inputs
        
    
    ox_candidate = find_criteria_report(inputs, 1)
                                                    # Most of the work is done inside the function...
    co2_candidate = find_criteria_report(inputs, 0)

    solution = bin_to_dec(co2_candidate) * bin_to_dec(ox_candidate)
    print(f"The life support rating of the submarine is: {solution}") # 4406844

    input_data.close()

            

if __name__ == "__main__":
    main()