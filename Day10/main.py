#!/usr/bin/env python3

def main():

    with open("small.txt") as f:
        signals = f.read().splitlines()

    register = 1
    cycle = 1
    row = []
    
    sprite = 1

    for signal in signals:

        if 'noop' in signal:        
            cycle += 1
            print(f'Cycle {cycle} - Register {register} - Strength {cycle * register}')

        else:
            cycle += 1
            print(f'Cycle {cycle} - Register {register} - Strength {cycle * register}')
            counter = int(signal.split(" ")[1])
            register += counter
            sprite += counter
            print(sprite)
            cycle += 1
            print(f'Cycle {cycle} - Register {register} - Strength {cycle * register}')
        
        # 20   340
        # 60   1260
        # 100  2100
        # 140  2940
        # 180  3780
        # 220  4840


if __name__ == '__main__':
    main()