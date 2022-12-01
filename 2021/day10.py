
# https://adventofcode.com/2021/day/10

def EOF_check(input): # Small function to check if the program reached the EOF
    return 0 if input == "" or input == "\n" else 1

# Used for both parts
def is_corrupt(string, return_stack=False): # Parameters: 'string' -> the string that contains all brackets
                                            #       'return_stack' -> returns with the eventual exception the pile of brackets not closed

    brackets = {"(":")", "[":"]", "{":"}", "<":">"}  # List where every opening bracket is coupled with their closing bracket

    stack = []
    for i in string:
        
        if i in brackets.keys(): # If the character is an opening bracket
            stack.append(i)      # Add it to the pile
        
        else: # If it's a closing bracket

            if brackets[stack[-1]] == i: # If it is paired with the last number of the pile
                stack.pop(-1) # It's not corrupt, pair is found and the last opening bracket can be removed from the pile

            elif i != "\n": # An if condition to avoid edge cases

                if return_stack == False: # If the user doesn't want to get the stack
                    return i              # Only return the exception
                else:                     # Otherwise return the stack too (even if it is not going to be used)
                    return i, stack
    
    # No corrupution found
    if return_stack: # Return stack too if the user wants it
        return 0, stack
    return 0

# Used for part 2
def is_missing(stack): # Parameter: 'stack' -> The list of brackets that still need their pair

    # Since the instructions doesn't explicitly say it, this function only returns the points that the string would get
    # it doesn't complete it with the missing closing brackets

    point_dict = {"(":1, "[":2, "{":3, "<":4}
    
    total  = 0
    for i in reversed(stack): # Iterating every bracket starting from the top of the pile 
        total = total*5 + point_dict[i] # Add corresponding points

    return total # Return score
        

def main():

    # Part 1
    input_data = open("day10_input.txt", "r") # Opening inputs

    point_dict = {")":3, "]":57, "}":1197, ">":25137} # Score for all brackets

    total = 0 # Variable that will store the result for the first part

    check = input_data.readline() # While loop that reads every line until the EOF (without wasting space containg all lines in a list)
    while EOF_check(check): 
        if is_corrupt(check): # If a misplaced bracket has been found
            total += point_dict[is_corrupt(check)] # Check the score for that bracket
        check = input_data.readline() # Read next line
    
    print(f"The total syntax error score is: {total}\n") # 344193

    # Part 2
    input_data.seek(0) # Returning to the start of the file
    
    total  = [] # Now all scores (found in 'is_missing') are stored since we want to find the median value

    check = input_data.readline() # Similar while loop until the EOF 
    while EOF_check(check):

        corrupt, stack = is_corrupt(check, True) # Using other parameter to get from function the pile of missing brackets
        
        if corrupt == 0: # If not corrupt
            total.append(is_missing(stack)) # Append the value from 'is_missing' to list

        check = input_data.readline()

    total.sort() # Sort list and find the median
    print(f"The median score is: {total[len(total)//2]}") # 3241238967



if __name__ == "__main__":
    main()