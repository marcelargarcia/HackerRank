# https://www.udemy.com/course/11-essential-coding-interview-questions
# O(N)


def non_repeating(given_string):
    non_repeating = {}
    str_array = list(given_string)
    for i in range(len(str_array)):
        if non_repeating.get(str_array[i], 'Not Found') == 'Not Found':
            non_repeating[str_array[i]] = True
        else:
            non_repeating[str_array[i]] = False
    keys = [k for k, v in non_repeating.items() if v == True]
    if len(keys) == 0:
        keys.append(None)
    return keys[0]


if __name__ == "__main__":
    print(non_repeating("abcab"))  # should return 'c'
    print(non_repeating("abab"))  # should return None
    print(non_repeating("aabbbc"))  # should return 'c'
    print(non_repeating("aabbdbc"))  # should return 'd'
