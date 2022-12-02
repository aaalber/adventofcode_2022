
def main():
    
    shape_score = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    ties = [['B','Y'],['A','X'],['C','Z']] 
    wins = [['C','X'],['A','Y'],['B','Z']]
    """
    Opponent:  A for Rock, B for Paper, and C for Scissors
    Me:        X for Rock, Y for Paper, and Z for Scissors
    -------
    Scores: 
    0 if you lost, 3 if the round was a draw, and 6 if you won
    1 for Rock, 2 for Paper, and 3 for Scissors
    """
    f = open("input.txt", "r")

    # Convert input file to something we can compare
    raw_matches = f.read().split('\n')
    all_matches = []

    for score in raw_matches:
        all_matches.append(score.split(" "))
    
    """ PART 1 """
    total_score = 0
    for match in all_matches:
        this_score = 0
        this_score = this_score + shape_score[match[1]]
        
        if match in ties:
            this_score = this_score + 3
        elif match in wins:
            this_score = this_score + 6
        
        total_score = total_score + this_score

    print(f'Part 1: {total_score}')

    """ PART 2 """
    # X = LOSE , Y = DRAW , Z = WIN
    total_score = 0 
    for match in all_matches:
        this_score = 0 

        if match[1] == "Z":
            # Need to Win
            if match[0] == "A":
                this_score = 2            
            elif match[0] == "B":
                this_score = 3
            else:
                this_score = 1
            this_score = this_score + 6
        elif match[1] == "Y":
            # Need to Tie
            this_score = this_score + shape_score[match[0]] + 3
        else: 
            # Need to Lose
            if match[0] == "A":
                this_score = 3
            elif match[0] == "B":
                this_score = 1
            else:
                this_score = 2

        total_score = total_score + this_score

    print(f'Part 2: {total_score}')






if __name__ == "__main__":
   main()