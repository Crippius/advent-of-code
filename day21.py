
# https://adventofcode.com/2021/day/21

memo = {}

def dirac_dice_game(player1_pos, player2_pos, player1_score=0, player2_score=0):
    
    global memo

    if player1_score >= 21: # Base cases, if a player has won
        return (1, 0)
    if player2_score >= 21: # Or the current positions+scores have been already calculated
        return (0, 1)
    if (player1_pos, player2_pos, player1_score, player2_score) in memo:
        return memo[(player1_pos, player2_pos, player1_score, player2_score)]
    
    # Default case
    results = (0, 0)
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4): # Rolling three 3d dices and finding new position + score of player 1
                new_player1_pos = (player1_pos+d1+d2+d3)%10
                new_player1_score = player1_score+new_player1_pos+1 # For all 12 combinations of rolls check winner
                win_results = dirac_dice_game(player2_pos, new_player1_pos, player2_score, new_player1_score) # <- Alternating players                       
                results = (results[0]+win_results[1], results[1]+win_results[0]) # Updating win results

    memo[(player1_pos, player2_pos, player1_score, player2_score)] = results 
    return results # Before returning results add it to the dict
                    

def main():
    
    input_data = open("day21_input.txt", "r")

    # Part 1  
    player1_pos = int(input_data.readline()[-2])-1 # Getting initial position of the two players
    player2_pos = int(input_data.readline()[-2])-1 # Subtracting by one to make it compatible with the modulo operator

    player1_score, player2_score = 0, 0
    
    die, times = 0, 0
    while player1_score < 1000 and player2_score < 1000: # While a winner hasn't been found
        
        if times%2 == 0: # Since the 'times' variable increases by three every iteration, when it's divisible by 2 it's the first player turn
            for _ in range(3): # 'Rolling' the deterministic die and moving it in the board three times
                die = die+1 if die != 100 else 1 
                player1_pos = (player1_pos+(die%10))%10
            player1_score += player1_pos+1 # Increasing the player's score by its position (+1 removed by the modulo %) 
        
        else: # Otherwise it's player two's turn
            for _ in range(3):
                die = die+1 if die != 100 else 1 
                player2_pos = (player2_pos+(die%10))%10
            player2_score += player2_pos+1
        
        times += 3


    print("The product of the # of times the die was rolled and the loser's score is: ", end="")
    print(times*player2_score if player1_score >= 1000 else times*player1_score) # 893700
    print()
    
    # Part 2
    input_data.seek(0) # Resetting positions
    player1_pos = int(input_data.readline()[-2])-1
    player2_pos = int(input_data.readline()[-2])-1

    results = dirac_dice_game(player1_pos, player2_pos) # Completing new game
    print(f"The # of times the player that has won in more universes has beaten its rival is: ", end="") 
    print(results[0] if results[0] >= results[1] else results[1]) # 568867175661958
    

    
if __name__ ==  "__main__":
    main()