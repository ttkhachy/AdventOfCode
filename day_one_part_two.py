def get_list_by_index(f_obj, index: int):
    ret_list = []
    for line in f_obj:
        print(line)
        line = line.split()
        ret_list.append(int(line[index]))
        print(f"int = {int(line[index])}")
    print(f"ret_list = {ret_list}")
    ret_list.sort()
    return ret_list


def main():
    file_path = "input.txt"
    f_obj = open(file_path)

    list1 = get_list_by_index(f_obj, 0) ## returns sorted list
    print(f"list1 = {list1}")
    f_obj.seek(0)
    list2 = get_list_by_index(f_obj, 1)
    print(f"list2 = {list2}")