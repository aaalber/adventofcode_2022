#!/usr/bin/env python3

def main():

    with open("small.txt") as f:
        moves = f.read().splitlines()

    for move in moves:
        move = move.split(' ')

        direction = move[0]
        num = move[1]
        

        print(move)

    print(moves)


if __name__ == '__main__':
    main()