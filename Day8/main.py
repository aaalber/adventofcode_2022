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
    tree_num = []

    for row_num,values in rows.items():

        tree_n = 1
        row_index = 0
        col_index = 0
        col_num = 0

        for value in values:

            value = int(value)
            
            if row_num == 1 or row_num == len(rows):
                total_count += 1
            
            else:
                if row_index == 0 or row_index == len(values) - 1:
                    if not row_num == 1 or not row_num == len(rows):
                        total_count += 1
            
                else:
                    right = values[row_index:][1:]
                    left = values[:row_index]
                    bottom = cols[col_index + 1][row_num:]
                    top = cols[col_index + 1][:row_num - 1]
                    
                    right_1 = [i for i in right if int(i) >= value]
                    left_1 = [i for i in left if int(i) >= value]
                    top_1 = [i for i in top if int(i) >= value]
                    bottom_1 = [i for i in bottom if int(i) >= value]
                    
                    if not right_1 or not left_1 or not top_1 or not bottom_1:
                        total_count += 1
                    

                    right = values[row_index:][1:]
                    left = values[:row_index]
                    bottom = cols[col_index + 1][row_num:]
                    top = cols[col_index + 1][:row_num - 1]
                    
                    lcount = 0 
                    rcount = 0
                    tcount = 0
                    bcount = 0

                    for x in right:
                        x = int(x)
                        if value > x:
                            rcount += 1
                        else:
                            rcount +=1
                            break
                    
                    for x in left[::-1]:
                        x = int(x)
                        if value > x:
                            lcount += 1
                        else:
                            lcount +=1
                            break

                    for x in top[::-1]:
                        x = int(x)
                        if value > x:
                            tcount += 1
                        else:
                            tcount +=1
                            break

                    for x in bottom:
                        x = int(x)
                        if value > x:
                            bcount += 1
                        else:
                            bcount +=1
                            break

                    tree_num.append(lcount * rcount * tcount * bcount)


            row_index += 1
            col_index += 1

    """ PART 1 """            
    print(f'Part 1 Total: {total_count}')

    """ PART 2 """
    print(f'Part 2 Total: {max(tree_num)}')




if __name__ == '__main__':
   main()