class DayTwoAdvent:
    def __init__(self):
        """
        part1: the lines that are safe according to part 1 specifications
        part2: the lines that are safe according to part 2 specifications
        """
        self.part1 = 0
        self.part2 = 0
    
    def is_level_safe(self, line: list[int]) -> bool:
        """
        Arguments:
            line: a list of integers containing all the values of the given line
        Function:
            calculates the difference between consecutive values in the line and adds it to a set.
            the final set to compared to the acceptable values of differences
        Returns:
            bool - returns if the set of difference is less than or equal to the acceptable given set
        """
        diff_set = set()
        for i in range(len(line) - 1):
            diff_set.add(line[i] - line[i+1])
        return diff_set <= {1, 2, 3} or diff_set <= {-1, -2, -3}

    def get_safe_lines(self, f_obj) -> int:
        for line in f_obj:
            line = line.split()
            int_nums = [ int(x) for x in line ]
            if self.is_level_safe(int_nums):
                #print(is_level_safe(line))
                self.part1 += 1
                self.part2 += 1
            else:
                for i in range(len(int_nums)):
                    if self.is_level_safe(int_nums[:i] + int_nums[i+1:]):
                        self.part2 += 1
                        break

def main():
    file_path = "day2.txt"

    f_obj = open(file_path, 'r')
    d2 = DayTwoAdvent()
    d2.get_safe_lines(f_obj)
    print(d2.part1)
    print(d2.part2)

main()