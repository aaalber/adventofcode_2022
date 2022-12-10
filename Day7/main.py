#!/usr/bin/env python3

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
    #for k,v in all_files.items():
    #    print(k,v)
    for folder,subfolders in sub_dirs.items():
        print(len(subfolders))
        folder_size = 0
        for file,size in all_files.items():
            if file.startswith(folder):
                folder_size = folder_size + size

        for file,size in all_files.items():
            for subfolder in subfolders:
                if file.startswith(subfolder):
                    folder_size = folder_size + size
        
        all_folders[folder] = folder_size
                    

    #for k,v in all_folders.items():
    #    print(k,v)

    y = dict(sorted(all_folders.items(), key=lambda item: item[1]))
    total = 0 
    for k,v in y.items():
        print(k,v)
        if v <= 100000:
            total = total + v

    print(f'Part 1 Total: {total}')

        #print(folder, subfolder)
    """ 
    all_folders = {}
    for file,space in all_files.items():
        for folder,subfolder in sub_dirs.items():
            print('/'.split(folder))
            print('/'.split(file))
            if folder in file:
                if folder in all_folders.keys():
                    all_folders[folder] = all_folders[folder] + space
                else:
                    all_folders[folder] = space
                print("yes")
    print(all_folders)
    """
    """
    temp_dict = {}
    for k,v in all_files.items():
        #print(k,v)
        if not k:
            k = "/est"
        split_me = k.split('/')
        directory = split_me[-2:-1][0]
        #print(directory)
        if k not in temp_dict.keys():
            temp_dict[directory] = int(v)
        else: 
            temp_dict[directory] = temp_dict[directory] + int(v)


    y = dict(sorted(temp_dict.items(), key=lambda item: item[1]))
    total = 0 
    for k,v in y.items():
        if v <= 100000:
            total = total + v

    print(f'Part 1 Total: {total}')

    
    total_sizes = {} 
    for k,v in dirs_just_files.items():
        total_size = v

        for x in sub_dirs[k]:
            total_size = total_size + dirs_just_files[x]

        total_sizes[k] = total_size
    
    y = dict(sorted(total_sizes.items(), key=lambda item: item[1]))
    total = 0 
    for k,v in y.items():
        if v <= 100000:
            total = total + v

    print(f'Part 1 Total: {total}')
    
    """
if __name__ == '__main__':
   main()