
def tournament_points(matchup):

    shape_points = {"Rock":1, "Paper":2, "Scissors":3}
    result_points = {"Win":6, "Draw":3, "Lose":0}

    who_wins = {"Rock":"Paper", "Paper":"Scissors", "Scissors":"Rock"}

    total_points = 0
    for i in matchup:
        rival, me = i
        round_points = result_points["Draw"]
        if who_wins[rival] == me:
            round_points = result_points["Win"]
        elif who_wins[me] == rival:
            round_points = result_points["Lose"]
        round_points += shape_points[me]

        total_points += round_points
    
    return total_points


if __name__ == "__main__":

    fp = open("day02_input.txt", "r")

    line = fp.readline()

    matchup = []
    while line != "":
        matchup.append(tuple(line.split()))
        line = fp.readline()
    

    their_strat = {"A":"Rock", "B":"Paper", "C":"Scissors"}

    my_strat = {"X":"Rock", "Y":"Paper", "Z":"Scissors"}

    first_matchup = []
    for match in matchup:
        first_matchup.append((their_strat[match[0]], my_strat[match[1]]))
        
    print(f"The number of points made in the tournament using the first strategy is: {tournament_points(first_matchup)} points")

    aux_dict = {"Rock":0, "Paper":1, "Scissors":2, 
                0:"Rock", 1:"Paper", 2:"Scissors"}

    my_new_strat = {"X":-1, "Y":0, "Z":+1}

    second_matchup = []
    for match in matchup:
        second_matchup.append((their_strat[match[0]], aux_dict[(aux_dict[their_strat[match[0]]]+my_new_strat[match[1]])%3]))
    
    print(f"The number of points made in the tournament using the second strategy is: {tournament_points(second_matchup)} points")

