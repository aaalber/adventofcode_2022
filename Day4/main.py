#!/usr/bin/env python3

def main():

    with open("input.txt") as f:
        all_elves = f.read().splitlines()

    new_list = [ elf.split(',') for elf in all_elves]

    count_1 = 0
    count_2 = 0
    for elf in new_list:
        elf1 = elf[0].split("-")
        elf2 = elf[1].split("-")
        
        range1 = list(range(int(elf1[0]), int(elf1[1]) + 1))
        range2 = list(range(int(elf2[0]), int(elf2[1]) + 1))

        """ Part 1 """
        if (all(item in range1 for item in range2) or
            all(item in range2 for item in range1)):
            count_1 = count_1 + 1

        """ Part 2 """
        if any(item in range1 for item in range2): # or
            count_2 = count_2 + 1

    print(f'Total Count: {count_1}')
    print(f'Total Count: {count_2}')


if __name__ == '__main__':
   main()