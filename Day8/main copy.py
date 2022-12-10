#!/usr/bin/env python3

def main():

    folders = {}

    rows = {}
    cols = {}

    with open("small.txt") as f:
        grid = f.read().splitlines()
    
    count = 1
    col_count = 0
    for line in grid:
        rows[count] = [*line]
        cols[count] = [ col[col_count] for col in grid ]
        count += 1
        col_count += 1

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
    row_index = 0
    col_index = 0
    col_num = 0  
    
    for row_num,values in rows.items():

        if row_num == 1:
            # First Row

            for value in values:
                #print(values) 
                #top = 0 if row_num = 1 else top = cols[col_index - 1][col_num + 1]
                bottom = 0 if row_num == len(rows) else cols[col_index + 1][col_num + 1]

                if row_index == 0:
                    # First Number
                    if value > values[row_index + 1] and value > bottom:
                        print("Yes 1:1")

                elif row_index == len(values) - 1:
                    # Last Number
                    if value > values[row_index - 1] and value > bottom:
                        print("yes last:1")

                else:
                    # check left and right
                    if (value > values[row_index - 1] and 
                        value > values[row_index + 1] and
                        value > bottom):
                        print("yes")
                
                row_index += 1
                col_index += 1

        elif row_num == len(rows):
            # Last row
            pass





        else:
            # all middle rows
            pass

        row_index = 0 

        """    
        if row_index == 0:
            # Edge tree
            this_play = values[row_index:2]
        elif row_index
        """

        





if __name__ == '__main__':
   main()