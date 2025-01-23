import re

class DayFour:
    def __init__(self):
        self.part1_count = 0

    def check_and_count(self, word):
        if word in {"XMAS", "SAMX"}:
            self.part1_count +=1

    def horizontal_count(self, lines: list[str]):
        """Count occurrences of target words horizontally."""
        for line in lines:
            self.part1_count += len(re.findall("XMAS", line))
            self.part1_count += len(re.findall("SAMX", line))

    
    def diagonal_left_to_right(self, lines: list[str]):
        """Count occurrences of target words horizontally from top left to bottom right."""
        for row in range(len(lines) - 3):
            for col in range(len(lines[row]) - 3): # 4 or 3
                word = lines[row][col] + lines[row+1][col+1] +lines[row+2][col+2] + lines[row+3][col+3]
                self.check_and_count(word)

        pass
    
    def diagonal_right_to_left(self, lines):
        """Count occurrences of target words diagonally from top right to bottom left."""
        for row in range(len(lines) - 3):
            for col in range(3, len(lines[row])):  # Start from the 4th column
                word = (
                    lines[row][col]
                    + lines[row + 1][col - 1]
                    + lines[row + 2][col - 2]
                    + lines[row + 3][col - 3]
                )
                self.check_and_count(word)

    def vertical_count(self, lines: list[str]):
        """Count occurrences of target words vertically."""
        for col in range(len(lines[0])):  # Loop through columns
            for row in range(len(lines) - 3):  # Ensure there are enough rows
                word = (
                    lines[row][col]
                    + lines[row + 1][col]
                    + lines[row + 2][col]
                    + lines[row + 3][col]
                )
                self.check_and_count(word)


def main():
    d4 = DayFour()
    try:
        f_obj = open("day4.txt")
        lines = f_obj.readlines()
        d4.vertical_count(lines) 
        d4.diagonal_left_to_right(lines)
        d4.diagonal_right_to_left(lines)
        d4.horizontal_count(lines)
        print(f"final count: {d4.part1_count}")
    except FileNotFoundError:
        print("Error, the file \"day4.txt\" was not found.")

main()

