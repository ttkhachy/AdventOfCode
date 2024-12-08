'''
def is_inc_level_safe(line: list[int]) -> bool:
    ## 1 4 8 5 10
    #print(line)
    i = 1
    bad_level_allowance = 0

    while i < (len(line)):
        diff = line[i] - line[i-1]
        #print(diff)
        print(f"line: {line} bla: {bad_level_allowance}")
        if diff < 1 or diff > 3:
            for i in range(len(line)):
                if is_inc_level_safe(line[i:] + line[i+1:]):
                    return True
                
            return False
        i+=1
    return True
'''

def is_level_safe(line: list[int]) -> bool:
    #print(f"line {line}")
    diff_set = set()
    for i in range(len(line) - 1):
        #print(f"diff = {line[i] - line[i+1]}")
        #print(f"line[i]: {line[i]} line[i+1]: {line[i+1]}")
        diff_set.add(line[i] - line[i+1])
    #print(diff_set)
    #print(diff_set <= {1, 2, 3})
    #print(diff_set <= {-1, -2, -3})
    #print(diff_set <= {1, 2, 3} or diff_set <= {-1, -2, -3})
    return diff_set <= {1, 2, 3} or diff_set <= {-1, -2, -3}

def get_safe_lines(f_obj) -> int:
    safe_lines=0
    for line in f_obj:
        line = line.split()
        int_nums = [ int(x) for x in line ]
        if is_level_safe(int_nums):
            #print(is_level_safe(line))
            safe_lines += 1
        else:
            for i in range(len(int_nums)):
                if is_level_safe(int_nums[:i] + int_nums[i+1:]):
                    safe_lines +=1
                    break
    return safe_lines

    ## it is correct bu it cant differentiate between 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    # so need to maybe have a decreasing checker and increasing check to account for this?


def main():
    file_path = "day2.txt"

    f_obj = open(file_path, 'r')
    safe_lines = get_safe_lines(f_obj)
    print(safe_lines)

main()
