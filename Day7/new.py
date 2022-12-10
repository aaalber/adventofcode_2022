#!/usr/bin/env python3

def main():

    with open("input.txt") as f:
        commands = f.read().splitlines()

    current_path = []
    dirs_just_files = {}

    for c in commands:
        command = c.split(" ")
        if not ("ls" in command or "dir" in command):

            if '$ cd' in command:
                if command[5:] == "..":
                    current_path.pop()
                else:
                    dash = "" if current_path[-1] == "/" else "/"
                    print(dash)
                    current_path.append(command[5:])

            else:
                print(command)
        print(current_path)
#        else:
#            filesize = int(command[0])



if __name__ == '__main__':
   main()