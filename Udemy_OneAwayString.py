# https://www.udemy.com/course/11-essential-coding-interview-questions/learn/quiz/380026#questions
# O(N)


def is_one_away(s1, s2):
    if len(s1) > len(s2):
        maxList = list(s1)
        minList = list(s2)
    else:
        maxList = list(s2)
        minList = list(s1)

    # Same len
    if len(s1) == len(s2):
        countdiff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                countdiff += 1
            if countdiff > 1:
                return False
        return True

    # Diff len
    elif (len(maxList) - len(minList)) == 1:
        countdiff = 0
        j = 0
        for i in range(len(maxList)):
            if maxList[i] != minList[j]:
                countdiff += 1
            elif maxList[i] == minList[j] and j < len(minList) - 1:
                j += 1
            if countdiff > 1:
                return False
        return True

    else:
        return False


# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcdeeeee", "abcd"))  # should return False
print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("abcde", "abde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
