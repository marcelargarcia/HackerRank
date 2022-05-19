# https://www.udemy.com/course/11-essential-coding-interview-questions
# No Duplicates


def isARotation_1(list1, list2):  # O(n)
    if len(list1) != len(list2):
        return False

    i = 0
    if list1[i] not in list2:
        return False

    for key_i in range(len(list2)):
        if list1[i] == list2[key_i]:
            break
    for i in range(len(list1)):
        j = (key_i + i) % len(list1)
        if list1[i] != list2[j]:
            return False

    return True

def isARotation(list1, list2):  # O(n)
    if len(list1) != len(list2):
        return False

    i = 0
    if list1[i] not in list2:
        return False

    for key_i in range(len(list2)):
        if list1[i] == list2[key_i]:
            break
    j = key_i -1
    for i in range(len(list1)):
        j += 1
        if j == len(list2):
            j = 0
        if list1[i] != list2[j]:
            return False

    return True

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2a = [4, 5, 6, 7, 8, 1, 2, 3]
    print(isARotation(list1, list2a))

    list2a = [4, 5, 6, 7, 1, 2, 3]
    print(isARotation(list1, list2a))

    list2a = [4, 5, 6, 9, 1, 2, 3]
    print(isARotation(list1, list2a))

    list2a = [4, 6, 5, 7, 1, 2, 3]
    print(isARotation(list1, list2a))

    list2a = [4, 5, 6, 7, 0, 2, 3]
    print(isARotation(list1, list2a))

    list2a = [1, 2, 3, 4, 5, 6, 7]
    print(isARotation(list1, list2a))

    list2a = [7, 1, 2, 3, 4, 5, 6]
    print(isARotation(list1, list2a))
