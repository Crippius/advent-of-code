
# https://adventofcode.com/2021/day/14

from math import ceil # Function used to round up the values that are inserted

def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" else 0



def poly_insertion(pairs, rules): # Inserts in dictionary all new combinations in this generation
    
    new_gen = {} # Dictionary where the new formations are going to be stored

    for i in pairs.keys(): # For every pair

        if i in rules: # If between the pair, a new element needs to be inserted 

            pair1 = i[0]+rules[i] # First pair, with first letter
            if pair1 not in new_gen:
                new_gen[pair1] = 0
            new_gen[pair1] += pairs[i] # Added in the new dictionary

            pair2 = rules[i]+i[1] # Same thing for the second pair, completed with the second letter
            if pair2 not in new_gen:
                new_gen[pair2] = 0
            new_gen[pair2] += pairs[i]

    return new_gen # Return the dictionary with all new insertions



def num_letters(pairs): # Counts the number of letters in the dictionary

    letters = {} # Dict where the keys are the characters and the values are the number of times they are present in the polymer

    for i in pairs.keys(): # For every pair

        if i[0] not in letters: # Adding the first letter to the dict and inserting the number of times this pair was found
            letters[i[0]] = 0
        letters[i[0]] += pairs[i]
        
        if i[1] not in letters: # Same thing with the second letter
            letters[i[1]] = 0
        letters[i[1]] += pairs[i]
    
    for i in letters.keys(): # Since all letters but the extreme ones are counted twice, divide by two and find the ceiling value
        letters[i] = ceil(letters[i]/2)
    
    return letters # Return the dict



def main():

    input_data = open("day14_input.txt", "r")

    template = input_data.readline() # Reading first line (starting polymer)
    
    pairs = {} # Adding to 'pairs' dict the first pairs of the starting polymer
    for i in range(len(template)-2): # Key: A pair (ex. NB) | Value: The number of times the pair is present in the template (ex. 2)
        if template[i]+template[i+1] not in pairs.keys():
            pairs[template[i]+template[i+1]] = 0
        pairs[template[i]+template[i+1]] += 1
    
    input_data.readline() # Skipping empty line

    insertion_rules = {} # Key: The needed pair to insert an element (ex. NB)
                         # Value: The element that needs to be inserted (ex. H)
    
    check = input_data.readline() 
    while EOF_check(check): # Adding all rules for the insertion of elements
        insertion_rules[check[:2]] = check[-2]
        check = input_data.readline()

    for gen in range(10): # Part 1, doing it ten times
        pairs = poly_insertion(pairs, insertion_rules) # Adding new polymers
    
    letters = num_letters(pairs) # Finding the number of letters
    print("The difference between the most common letter and the least common one after 10 generations is: ", end="") 
    print(max(letters.values()) - min(letters.values())) # 3247
    print() # Adding newline

    for gen in range(30): # Part 2, doing it 40 times (starting from the tenth generation)
        pairs = poly_insertion(pairs, insertion_rules)  
    
    letters = num_letters(pairs)
    print("The difference between the most common letter and the least common one after 40 generations is: ", end="")
    print(max(letters.values()) - min(letters.values())) # 4110568157153

# My first solution, worked perfectly with the first part, struggled a lot with the second one,
# since the string becomes more and more big as time goes on, the time it takes to work through the insertions grows exponentially
# |
# v
# template = string (ex. NNCB)
# for gen in range(10):
#     tmp = template[0]
#     for i in range(len(template)-1):
#         if template[i]+template[i+1] in insertion_rules.keys():
#             tmp += insertion_rules[template[i]+template[i+1]]
#         tmp += template[i+1]
#     template = tmp
    


if __name__ == "__main__":
    main()