#!/usr/bin/env python3

def main():

    with open("input.txt") as f:
        signal = list(f.read())

    index = 0 
    count = 4
    count_2 = 14

    for s in signal:
        next_four = signal[index:count]
        next_fourteen = signal[index:count_2]

        if len(set(next_four)) == 4:
            print(f'Marker at {index + 4}')
        
        if len(set(next_fourteen)) == 14:
            print(f'Message at {index + 14}')

        count_2 = count_2 + 1
        count = count + 1
        index = index + 1


if __name__ == '__main__':
   main()