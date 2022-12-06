#!/usr/bin/env python3

def main():

    stacks = {
        1: ['S','L','W'],
        2: ['J','T','N','Q'],
        3: ['S','C','H','F','J'],
        4: ['T','R','M','W','N','G','B'],
        5: ['T','R','L','S','D','H','Q','B'],
        6: ['M','J','B','V','F','H','R','L'],
        7: ['D','W','R','N','J','M'],
        8: ['B','Z','T','F','H','N','D','J'],
        9: ['H','L','Q','N','B','F','T']
    }
    
    with open("input.txt") as f:
        moves = f.read().splitlines()

    for move in moves:
        # Pull numbers out of input
        numbers = [int(i) for i in move.split() if i.isdigit()]
        num = numbers[0]
        frm = numbers[1]
        to = numbers[2]

        # Save the crates we are removing, then del
        crates = stacks[frm][-num:]
        del stacks[frm][-num:]

        # Part 1 
        # stacks[to].extend(list(reversed(crates)))
        # Part 2
        stacks[to].extend(list(crates))

    for k,v in stacks.items():
        print(k,v)




if __name__ == '__main__':
   main()






