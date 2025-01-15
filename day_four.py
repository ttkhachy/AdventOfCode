import re

class DayFour:
    def __init__(self):
        self.part1_count = 0

    def check_and_count(self, word):
        if word in {"XMAS", "SAMX"}:
            self.part1_count +=1

    def horizontal_count(self, lines: list[str]):
        for line in lines:
            self.part1_count += len(re.findall("XMAS", line))
            self.part1_count += len(re.findall("SAMX", line))

    
    def diagonal_left_to_right(self, lines: list[str]):
        for row in range(len(lines) - 3):
            for col in range(len(lines[row]) - 3): # 4 or 3
                word = lines[row][col] + lines[row+1][col+1] +lines[row+2][col+2] + lines[row+3][col+3]
                self.check_and_count(word)

        pass
    
    def diagonal_right_to_left(self, lines):
        #either return the int or directly add it to the count
        i = len(lines) - 1
        k = len(lines[i]) - 1
        while i >= 3:
            k = len(lines[i])- 1
            while k >= 3:
                word = lines[i][k] + lines[i-1][k-1] +lines[i-2][k-2] + lines[i-3][k-3]
                self.check_and_count(word)
                k-=1
            i-=1

        pass

    def vertical_count(self, lines: list[str]):
        i = 0
        k = 0
        while i < (len(lines) - 3):
            k = 0
            while k < len(lines[i]) - 1: # when i add the -1 it gets rid of the white lines?
                word = lines[i][k] + lines[i+1][k] + lines[i+2][k] + lines[i+3][k]
                self.check_and_count(word)
                k+=1
            i+=1


def main():
    d4 = DayFour()
    f_obj = open("day4.txt")
    lines = f_obj.readlines()
    d4.vertical_count(lines) 
    d4.diagonal_left_to_right(lines)
    d4.diagonal_right_to_left(lines)
    d4.horizontal_count(lines)
    print(f"final count: {d4.part1_count}")

main()

