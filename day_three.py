import re

class DayThreeAdvent:
    def find_do_dont(self, f_obj):
        ## could use regex?
        matches = []
        
        for line in f_obj:
            lol = re.findall(r"don't\(\).*?do\(\)", line)
            print(f"lol:\n {lol}")
            
            for match in lol:
                print(match)
                print()
                matches.append(match)
            ##matches.append(re.findall(r"(don't\(\).*do\(\))", line))

        #print(matches)
        write_file = open("d3_do.txt", 'w')
        f_obj.seek(0)
        for line in f_obj:

            #print("hellow")
            for m in matches:
                #print("L")
                #print(f"m = {m}")
                fixed_line = line.replace(m, "")
                write_file.write(fixed_line)
        write_file.close
        return "d3_do.txt"

    def find_ok_mul(self, f_obj):
        ## could use regex?
        matches = []
        for line in f_obj:
            matches.append(re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", line))

        return matches
    
    def calculate_sum(self, matches):
        final_sum = 0
        for l in matches:
            for elem in l:
                #print(elem)
                product = int(elem[0]) * int(elem[1])
                final_sum += product
        
        return final_sum


def main():
    f_obj = open("day3.txt", 'r')
    d3 = DayThreeAdvent()
    matches = d3.find_ok_mul(f_obj)
    part1_sum = d3.calculate_sum(matches)

    f_obj.seek(0)
    new_file = d3.find_do_dont(f_obj)
    p2_f_obj = open(new_file, 'r')
    p2_matches = d3.find_ok_mul(p2_f_obj)
    p2_sum = d3.calculate_sum(p2_matches)
    print(part1_sum)
    print(p2_sum)



main()
