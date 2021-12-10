
# https://adventofcode.com/2021/day/4

def clean_data(input): # There were some problems while getting the inputs,
    clean_input = []   # This function cleans garbage data from them
    for i in input.split(" "):
        if i != "":
            clean_input.append(i)
    return clean_input


def check_table(table): # This functions checks if the following table had a win condition
    
    bingo = 0 # Pessimistic start, if a row has five -1 (a number that was found) found then it becomes 1
    for row in table: 
        if row.count(-1) == 5:
            bingo = 1
    if bingo == 1: # Checking if there was a bingo (done before checking the columns to optimize)
        return 1
    
    for i in range(0, 5):
        bingo = 1 # Optimistic start, if a column doesn't have five -1 then it become 0
        for j in range(0, 5):
            if table[j] != -1:
                bingo = 0
        if bingo == 1:
            return 1
    
    return 0


def main():

    # Part 1
    input_data = open("day04_input.txt", "r") # Opening the input file on read mode

    nums = [int(i) for i in input_data.readline().split(",")] # Numbers that are picked one at a time

    tables = [] # (Will) contain all tables

    input_data.readline() # Skipping a line without data
    for i in range(100):
        tmp = [] # (Will) contain a table
        for j in range(5):
            tmp.append([int(z) for z in clean_data(input_data.readline())]) # Inserting row and cleaning it in 'tmp'

        tables.append(tmp) # Inserting table in 'tables' 
        input_data.readline() # Skipping a line without data
        
    ok = 0 # If a winner has been found
    winning_table = [] # Placeholder for the winning table
    last_num = 0 # Last number used before finding the winner

    for num in nums:
        for table in tables:
            found = 0 # If the number is found, 'found' = 1
            for row in table:     
                for i in range(len(row)): # WOW! 4 for loops!
                    if num == row[i]:
                        row[i] = -1 # Turns found element into -1 placeholder
                        found = 1
            if found:
                if check_table(table) == 1: # If there was a BINGO
                    ok = 1
                    winning_table = table
            if ok:
                break  # Breaking the loops since the winner was found
        if ok:
            last_num = num
            nums = nums[nums.index(num):] # Instruction to optimize Part 2, when the numbers will be looped,
            break                         #  it will start from where it was finished

    sum = 0 # Finding the sum of the remaining values
    for row in winning_table:
        for i in row:
            if i != -1: # (Not counting the placeholders)
                sum += i

    solution = sum*last_num
    print(f"The final score of the winning board is: {solution}\n") # 51034

    # Part 2

    losing_tables = tables # The remaining losing tables
    last_num = 0 # Last number before finding the last winner

    for num in nums:
        tmp = [] # Used to insert the losers of x round
        for table in losing_tables:
            for row in table:     # WOW! 4 for loops! Again!
                for i in range(len(row)):
                    if num == row[i]:
                        row[i] = -1
                        found = 1

            if check_table(table) == 0: # If the table didn't won this round
                tmp.append(table) # The table is added with the other losers
        
        if len(tmp) == 0: # If the last table finally won
            last_num = num
            losing_tables = losing_tables[0] # The table is stored for the later results
            break
        else:
            losing_tables = tmp # Continue with the remaining boards
     
    sum = 0  # Same operation as last time
    for row in losing_tables:
        for i in row:
            if i != -1:
                sum += i
    
    solution = last_num*sum
    print(f"The final score of the last board is {solution}") # 5434

    input_data.close()



if __name__ == "__main__":
    main()