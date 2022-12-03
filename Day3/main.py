#!/usr/bin/env python3
from string import ascii_lowercase, ascii_uppercase

def main():
    """ All sacks have two compartments """
    with open("input.txt") as f:
        all_sacks = f.read().splitlines() 

    # Store priority scores in dict
    count = 1
    priority = {}
    for lower_letter in ascii_lowercase:
        priority[lower_letter] = count
        count = count + 1

    for upper_letter in ascii_uppercase:
        priority[upper_letter] = count
        count = count + 1

    """ Part 1 """
    all_split_sacks = list()

    for sack in all_sacks:
        c1 = sack[:len(sack)//2]
        c2 = sack[len(sack)//2:]
        all_split_sacks.append([c1,c2])

    total_priority = 0 
    for split_sack in all_split_sacks:
        for letter in split_sack[0]:
            if letter in split_sack[1]:
                total_priority = total_priority + priority[letter]
                break

    print(total_priority)

    """ Part 2 """
    # Groups of 3
    groups = [all_sacks[i:i+3] for i in range(0, len(all_sacks), 3)]

    total_priority = 0 
    for group in groups:
        for l in group[0]:
            if l in group[1] and l in group[2]:
                total_priority = total_priority + priority[l]
                break
    
    print(total_priority)

if __name__ == '__main__':
   main()