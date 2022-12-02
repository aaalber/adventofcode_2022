
def main():
    f = open("input.txt", "r")

    all_elves = f.read().split('\n')
    # ['6669', '6434', '', '6160'

    this_elf = 0 
    cal_count = 0
    totals = []

    for cal in all_elves:
        if cal:
            cal_count = cal_count + int(cal)
        else:
            print(f'Elf {this_elf} = {cal_count}')
            totals.append(cal_count)
            this_elf = this_elf + 1
            cal_count = 0 

    # Part 1
    print(max(totals))

    # Part 2
    sorted_totals = sorted(totals, reverse=True)[0:3]
    print(sum(sorted_totals))

if __name__ == "__main__":
   main()