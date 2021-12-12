
# https://adventofcode.com/2021/day/12
                                                                                                          
# P.S: This is the first day in which I couldn't find my own solution, 
# The solution that I consulted to help me find my own answer is:
# https://www.reddit.com/r/adventofcode/comments/rehj2r/comment/hoa72no/?utm_source=share&utm_medium=web2x&context=3
# My first strategy can be seen at the end of the file


def EOF_check(input): # Small function to check if the program reached the EOF
    return 1 if input != "" else 0

def traverse_paths(branches, path=["start"], not_revisited=True): # Parameters: 
                                                                  # -'branches': see line 40
                                                                  # -'path': a list where the current path is stored
    curr = path[-1] # Current cave                                  -'revisited': For part 2, gives option to reenter cave a second time                                         

    if curr == "end": # Base case: 
        return [path] # If a path has found its way to the end, return its path
    
    # Default case:
    new_paths = []
    for i in branches[curr]: # For every possible branch

        if i == 'start': # If condition to avoid edge case in which the program returns to start
            continue
        
        if not (i.islower() and i in path): # If its a big cave / if its a cave that has never been visited before
            new_paths += traverse_paths(branches, path+[i], not_revisited) # add all possible new paths
        else:
            if not_revisited: # For part 2, if a small cave has not been visited twice in current path
                new_paths += traverse_paths(branches, path+[i], False) # add all possible new paths (removing option to re-enter)
            
    return new_paths # Return all paths
    


def main():
    input_data = open("day12_input.txt", "r") # Getting inputs and inserting them into the 'branches' dict

    branches = {} # Has all the caves as keys, their adjacents stored in a list as values 
    # ex: {'start': ['XR', 'vl', 'zw'], 'zi': ['XR', 'end', 'zk', 'ws'], 'XR': ['start', 'vl', 'zk', 'ws', 'zi', 'zw']}

    check = input_data.readline() 
    while EOF_check(check): # Cleaning values

        check = check.split("-") # Dividing data

        if check[0] not in branches: 
            branches[check[0]] = []
        branches[check[0]].append(check[1][:-1])
                                                 # Inserting them into the list
        if check[1][:-1] not in branches: 
            branches[check[1][:-1]] = []
        branches[check[1][:-1]].append(check[0])

        check = input_data.readline()
    
    result = len(traverse_paths(branches, ["start"], False))
    print(f"The number of paths in the cave system is : {result}\n") 
    result = len(traverse_paths(branches, ["start"], True))
    print(f"The number of paths in the cave system (entering one small cave twice) is : {result}") 

# My first approach to the problem:
# Really similar to the end product, it used a blacklist as a parameter instead of looking at it path
# My only problem was how the information was returned, the final result was a giant list of lists of lists of... and so on
# |
# v
# def traverse_paths(branches, curr="start", paths=[], blacklist=[]):

#     if curr == "end":
#         paths.append(curr)
#         return paths
    
#     new_paths = []
#     for i in branches[curr]:
#         if i not in blacklist:
#             new_paths.append(paths+[i])
#             if i.islower() and i != "end":
#                blacklist.append(i)
#             new_paths += traverse_paths(branches, i, new_paths, blacklist)
#     return new_paths

if __name__ == "__main__":
    main()