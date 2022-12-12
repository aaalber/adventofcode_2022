#!/usr/bin/env python3

from re import I


def main():

    folders = {}

    with open("input.txt") as f:
        commands = f.read().splitlines()

    current_path = []

    all_files = {}
    sub_dirs = {}

    for command in commands:
        if '$ cd' in command:
            if command[5:] == "..":
                current_path.pop()
            else:
                current_path.append(command[5:])            
        else:  
            ls = command.split(" ")

            if ls[0].isnumeric():
                this_file = '/'.join(current_path) + "/" + ls[1]
                all_files[this_file[1:]] = int(ls[0])

            elif ls[0] == "dir":
                if current_path == ["/"]:
                    this_path = ''.join(current_path)
                else:
                    this_path = '/'.join(current_path)[1:]
                
                if this_path not in sub_dirs.keys():
                    sub_dirs[this_path] = []
                
                if this_path == "/":
                    sub_dirs[this_path].append(this_path + ls[1])
                else:
                    sub_dirs[this_path].append(this_path + "/" + ls[1])
    
    all_folders = {}
    for folder,subfolders in sub_dirs.items():
        folder_size = 0
        for file,size in all_files.items():
            if file.startswith(folder):                
                folder_size = folder_size + size

        all_folders[folder] = folder_size
        

        for subfolder in subfolders:

            folder_size = 0
            for file,size in all_files.items():
                if file.startswith(subfolder):
                    folder_size = folder_size + size
                all_folders[subfolder] = folder_size
    
    dir_to_del = []
    total_space = 70000000
    space_free = total_space - all_folders["/"]
    space_needed = 30000000 - space_free
    for k,v in all_folders.items():
        if v > space_needed:
            dir_to_del.append(v)

    print(f'Part 2: {min(dir_to_del)}')
    
    total = 0 
    for k,v in all_folders.items():
        if v <= 100000:
            total = total + v

    print(f'Part 1 Total: {total}')
if __name__ == '__main__':
    main()