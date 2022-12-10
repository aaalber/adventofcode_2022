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
    print(rows)
    """
    # rows  {1: ['2', '4', '0', '4', '3', '2'], 2: ['2', '3', '3', '3', '5', '3']
    # cols  {1: ['2', '2', '2', '2', '4', '3'], 2: ['4', '3', '0', '1', '0', '2']
      240432
      233353
      202133
      214241
      404043
      321431 
    """
    total_count = 0 
    for row_num,values in rows.items():

        col_index = 0
        row_index = 0
        col_num = 0
        for value in values:

            #print(values) 
            #top = 0 if row_num == 1 else cols[col_index - 1][col_num + 1]
            #bottom = -1 if row_num == len(rows) else cols[col_index + 1][col_num + 1]
            #print(f'RowNum {row_num}, ColNum {col_num}, ColIndex {col_index}')
            if row_num == 1:
                top = -1
            else:
                top = cols[col_index + 1][row_num - 2]
            
            if row_num == len(rows):
                bottom = -1
            else:             
                bottom = cols[col_index + 1][col_num + 1]
            
            value, bottom, top = int(value), int(bottom), int(top)

            print(value, top, bottom)

            

            if row_index == 0:
                # First Number
                if value > int(values[row_index + 1]) and value > bottom and value > top:
                    total_count = total_count + 1
                #if value > int(values[row_index + 1]) and value > bottom:
                #    total_count = total_count + 1

            elif row_index == len(values) - 1:
                # Last Number
                print(row_num)
                if (value > int(values[row_index - 1]) and 
                    value > bottom and value > top):
                    total_count = total_count + 1        
                #if value > int(values[row_index - 1]) and value > bottom:
                #    print("yes last:1")

            else:
                # check left and right
                if (value > int(values[row_index - 1]) and 
                    value > int(values[row_index + 1]) and
                    value > bottom and value > top):
                    total_count = total_count + 1
            #col_num += 1    
            row_index += 1
            col_index += 1
            #col_num += 1
            

    print(total_count)




if __name__ == '__main__':
   main()