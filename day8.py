
# https://adventofcode.com/2021/day/8

def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" else 0

# Function used in Part 2
def decrypt_output(outputs, configuration): # Returns number encrypted in the output
    
    nums = {"0":["top", "top left", "top right", "bottom right", "bottom left", "bottom"], # Dictionary that contains all configurations for the 10 numbers
            "1":["top right", "bottom right"],                                             #                top
            "2":["top", "top right", "middle", "bottom left", "bottom"],                   #               _____
            "3":["top", "top right", "middle", "bottom right", "bottom"],                  #     top left |     | top right
            "4":["top left", "top right", "middle", "bottom right"],                       #              |_____| middle
            "5":["top", "top left", "middle", "bottom right", "bottom"],                   #              |     |  
            "6":["top", "top left", "middle", "bottom right", "bottom left", "bottom"],    #  bottom left |_____| bottom right
            "7":["top", "top right", "bottom right"],                                      #               bottom
            "8":["top", "top left", "top right", "middle", "bottom right", "bottom left", "bottom"], 
            "9":["top", "top left", "top right", "middle", "bottom right", "bottom"]}
    
    str_num = "" # Num that will be generated is stored here
    
    #        v    
    # ex. ["adf", "ebacg", "ag", "deabgc"] 
    for output in outputs:
        tmp = []
        for letter in output:
            for config in configuration.keys():
                if configuration[config] == letter: # Finding the configuration for every output
                    tmp.append(config)

        order = ["top", "top left", "top right", "middle", "bottom right", "bottom left", "bottom"]
        tmp.sort(key = lambda i: order.index(i))  # Ordering the configuration before comparing

        for num in nums.keys(): # Checking every number to see if they both have the same configuration
            if tmp == nums[num]:
                str_num += num # If a number is found concatenate it in string
        
    return int(str_num) # Return number in integer form


# Function used in Part 2
def find_configuration(patterns): # Function that given a pattern will return the configuration of the seven segment display

    # Since in the patterns all numbers from 0 to 9 are inserted the plan to find the configuration is:
    # Thanks to the unique length of letters of the nums 1 (2 letters), 4 (3), 7 (4) and 8 (7) we can discover that the possible positions of the letters 
    # have to be decided between two letters except for the top position, which we're going to know 
    # (ex. configuration = "top"->"a", "top left"/"middle" -> "b"/"c", "top right"/"bottom right" -> "d"/"e", "bottom left"/"bottom" -> "f"/"g").
    # After this discovery we find the pattern with 5 letters that has both the letters in contention for the "top right" and "bottom right" spot ("d"/"e"), 
    # This pattern can only identify the number 3, so we can find the exact value for every other position but the mentioned ones.
    # The final step is to find the pattern that would show 5, the letter that is in this pattern between the last two will take the "top right" spot
    # the other will take the last possible place, the "bottom right" one.

    # Dict where the configuration is going to be stored
    configuration = {"top":[], "top left":[], "top right":[], "middle":[], "bottom right":[], "bottom left":[], "bottom":[]} 

    # Dict where the keys (unique numbers length) are paired to their configurations
    possible_positions = {2:["top right", "bottom right"], 
                          3:["top", "top right", "bottom right"], 
                          4:["top left", "top right", "middle", "bottom right"],
                          7:["top", "top left", "top right", "middle", "bottom right", "bottom left", "bottom"]}

    # ex. ("ae", "ade", "adfc", "gfebd" ...)
    patterns.sort(key=len) # Sorting patterns based on length, to find in an easier way the possible configurations

    for pattern in patterns:
        # A temporary dict that is used to help fill the primary configuration dictionary
        new_pattern = {"top":1, "top left":1, "top right":1, "middle":1, "bottom right":1, "bottom left":1, "bottom":1}

        if len(pattern) in possible_positions.keys(): # If it's a unique value
            for i in pattern:
                check = 1
                spots = []
                for position in possible_positions[len(pattern)]:
                    if i in configuration[position]: # If the letter has been already inserted (with less combinations) don't bother inserting others
                        check = 0
                    elif len(configuration[position]) == 0: # If the letter has never been inserted and it can be inserted in the dict key
                            spots.append(position)
                            new_pattern[position] = 0
                    elif new_pattern[position] == 0: # If the dict key is already occupied see if the check condition is successfull
                        spots.append(position)

                if check: # If the letter hasn't been already inserted
                    for spot in spots:
                        configuration[spot].append(i) # Add it where it can be found
                    
    # Example of the configuration after this step: 
    # {'top': ['g'], 'top left': ['a', 'd'], 'top right': ['e', 'c'], 'middle': ['a', 'd'], 'bottom right': ['e', 'c'], 'bottom left': ['f', 'b'], 'bottom': ['f', 'b']}

    three = ["top", "middle", "bottom"] # Fundamental pieces to create the three (without considering right side)

    three_opposite = {"bottom":"bottom left", "middle":"top left", "top":"top"} # Where the other possible position for a letter is ("top"'s letter already found)

    for pattern in patterns: # P.S. it can be done with the number 2 or 5 too, this algorythm uses 3 instead
        if len(pattern) == 5:
            check = 1
            for i in configuration["top right"]: # If both the letters contending for the "top right" spot are found in the pattern
                if i not in pattern:
                    check = 0
            if check: # If the pattern identifies 3
                for letter in pattern:
                    for i in three: # In this pattern are found the unique letters for the "middle" and "bottom" position, consequentially the position
                        if letter in configuration[i] and (i != "top right" or i != "top left"): # for the "top left" and "bottom left" are found too, 
                            configuration[i].pop(configuration[i].index(letter))                 # all letters for this positions are inserted
                            configuration[three_opposite[i]] = configuration[i]
                            configuration[i] = [letter]
    
    # Example after this step: 
    # {'top': ['g'], 'top left': ['d'], 'top right': ['e', 'c'], 'middle': ['a'], 'bottom right': ['e', 'c'], 'bottom left': ['f'], 'bottom': ['b']}
    
    for pattern in patterns: 
        if len(pattern) == 5: # Finding pattern for the number 5
            if configuration["bottom left"][0] in pattern and configuration["bottom"][0] in pattern:

                if configuration["top right"][0] in pattern: # If the first letter is in the pattern, it belong in the "top right" spot, the other 
                    configuration["bottom right"] = [configuration["top right"][1]] # to the "bottom right" one
                    configuration["top right"] = [configuration["top right"][0]]
                
                else:                                        # Otherwise, do the opposite
                    configuration["bottom right"] = [configuration["top right"][0]]
                    configuration["top right"] = [configuration["top right"][1]]
    
    for i in configuration.keys(): # Substituting lists to strings since all letters have found their positions
        configuration[i] = configuration[i][0]
    
    # Example after this step: 
    # {'top': 'g', 'top left': 'd', 'top right': 'c', 'middle': 'a', 'bottom right': 'e', 'bottom left': 'f', 'bottom': 'b'}

    return configuration

    

def main():

    input_data = open("day8_input.txt", "r") # Getting inputs
    patterns = [] 
    outputs = []

    check = input_data.readline()
    while EOF_check(check):  # Cleaning and inserting inputs in their corresponding lists
        check = check.split(" | ")
        patterns.append(check[0].split(" "))

        not_clean_outputs = check[1].split(" ")
        not_clean_outputs[-1] = not_clean_outputs[-1][:-1]

        outputs.append(not_clean_outputs)
        check = input_data.readline()

    # Part 1
    count = 0
    for i in outputs:
        for j in i:
            if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
                count += 1
    print(f"The number of occurences of the numbers 1, 4, 7 and 8 in the output section is: {count} \n") # 284

    # Part 2
    sum = 0 
    for i in range(len(patterns)):
        configuration = find_configuration(patterns[i]) 
        sum += decrypt_output(outputs[i], configuration) # Adding every output value
    
    print(f"The sum of all output values is: {sum}") # 973499

    input_data.close()




if __name__ == "__main__":
    main()