class DayFive:
    def __init__(self):
        self.part_one_sum = 0
        self.ordering_rules = []
        self.page_nums = []

    def get_ordering_rules(self, f_obj):
        for line in f_obj:
            if '|' in line:
                line = line.strip("\n").split('|')
                self.ordering_rules.append([int(line[0]), int(line[1])])
            if ',' in line:
                page = [int(i) for i in line.split(',')]
                self.page_nums.append(page)

    def check_valid_line(self, line: list[int]):
        # line = [1, 5, 6, 2]
        # ordering rules = [ [2, 4], [6, 7], [8, 9]]
        for i in range(len(self.ordering_rules) - 1):
            if self.ordering_rules[i][0] in line and self.ordering_rules[i][1] in line:
                index1 = line.index(self.ordering_rules[i][0])
                index2 = line.index(self.ordering_rules[i][1]) 
                ## index1 must be < index2
                if index1 < index2:
                    middle_index = (len(line) - 1) / 2
                    self.part_one_sum + line[middle_index]


    def main(self):
        f_obj = open("day5.txt")
        self.get_ordering_rules(f_obj)



if __name__ == "__main__":
    d5 = DayFive()
    d5.main()
