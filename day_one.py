def get_similarity_score(list1: list[int], list2: list[int]):
    score = 0
    for i in range(len(list1)):
        v1 = int(list1[i])
        v1_count = list2.count(v1)
        score += (v1 * v1_count)

    return score

def get_difference(list1: list[int], list2: list[int]) -> int:
    diff = 0
    for i in range(len(list1)):
        v1 = int(list1[i])
        v2 = int(list2[i]) 
        diff += abs(v1 - v2)


    return diff

def get_list_by_index(f_obj, index: int):
    ret_list = []
    for line in f_obj:
        line = line.split()
        ret_list.append(int(line[index]))
    ret_list.sort()
    return ret_list


def main():
    file_path = "input.txt"
    f_obj = open(file_path)

    list1 = get_list_by_index(f_obj, 0) ## returns sorted list
    f_obj.seek(0)
    list2 = get_list_by_index(f_obj, 1)

    final_dif = get_difference(list1, list2)

    print(final_dif)

    sim_score = get_similarity_score(list1, list2)
    print(sim_score)


main()



