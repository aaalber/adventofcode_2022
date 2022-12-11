#!/usr/bin/env python3

def main():

    folders = {}

    rows = {}
    cols = {}

    with open("input.txt") as f:
        grid = f.read().splitlines()
    
    count = 1
    col_count = 0
    for line in grid:
        rows[count] = [*line]
        cols[count] = [ col[col_count] for col in grid ]
        count += 1
        col_count += 1
    
    total_count = 0 
    
    for row_num,values in rows.items():

        row_index = 0
        col_index = 0
        col_num = 0

        for value in values:

            if row_num == 1 or row_num == len(rows):
                total_count += 1
            
            else:
                if row_index == 0 or row_index == len(values) - 1:
                    if not row_num == 1 or not row_num == len(rows):
                        total_count += 1
            
                    value = int(value)
                else:
                    right = values[row_index:][1:]
                    left = values[:row_index]
                    bottom = cols[col_index + 1][row_num:]
                    top = cols[col_index + 1][:row_num - 1]
                    
                    right = [i for i in right if i >= value]
                    left = [i for i in left if i >= value]
                    top = [i for i in top if i >= value]
                    bottom = [i for i in bottom if i >= value]
                    
                    if not right or not left or not top or not bottom:
                        total_count += 1

            row_index += 1
            col_index += 1

    """ PART 1 """            
    print(total_count)





if __name__ == '__main__':
   main()