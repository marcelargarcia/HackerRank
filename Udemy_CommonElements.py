# https://www.udemy.com/course/11-essential-coding-interview-questions/learn/lecture/7450632#overview
# O(min(len(array1), len(array2))

def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return sorted(set1.intersection(set2))

if __name__ == "__main__":
    print(common_elements([1,3,4,6,7,9],[1,2,4,5,9,10]))

    list_b1 = [1, 2, 9, 10, 11, 12]
    list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
    print(common_elements(list_b1, list_b2))

    list_c1 = [0, 1, 2, 3, 4, 5]
    list_c2 = [6, 7, 8, 9, 10, 11]
    common_elements(list_b1, list_b2) # should return [] (an empty list).