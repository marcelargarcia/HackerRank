# https://www.udemy.com/course/11-essential-coding-interview-questions/learn/quiz/380026#questions
# O(N)


def is_one_away(s1, s2):
    arrs1 = list(s1)
    arrs2 = list(s2)

    # Same len
    if len(s1) == len(s2):
        countdiff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                countdiff +=1
        if countdiff <= 1:
            return True
        else:
            return False

    # Diff len
    elif len(s1) == len(s2) +1:
        countdiff = 0
        j = 0
        for i in range(len(s1)):
            if s1[i] != s2[j]:
                countdiff +=1
            elif s1[i] == s2[j] and j < len(s2) -1:
                j += 1
        if countdiff <= 1:
            return True
        else:
            return False
    elif len(s2) == len(s1) +1:
        countdiff = 0
        j = 0
        for i in range(len(s2)):
            if s2[i] != s1[j]:
                countdiff += 1
            elif s2[i] == s1[j] and j < len(s1) -1:
                j += 1
        if countdiff <= 1:
            return True
        else:
            return False

    else:
        return False

# NOTE: The following input values will be used for testing your solution.
print(is_one_away("abcdeeeee", "abcd")) # should return False
print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde")) # should return True
print(is_one_away("abcde", "abde"))  # should return True
print(is_one_away("a", "a")) # should return True
print(is_one_away("abcdef", "abqdef")) # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False
