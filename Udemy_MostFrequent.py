#https://www.udemy.com/course/11-essential-coding-interview-questions/learn/lecture/7450632#overview

import sys

def most_frequent(array):
    hash_frequency = {}
    freq = -sys.maxsize - 1
    freq_numb = None

    for i in range(len(array)):
        key = array[i]
        if hash_frequency.get(key, 'Not Found') == 'Not Found':
            hash_frequency[array[i]] = 1
        else:
            hash_frequency[array[i]] = hash_frequency[array[i]] + 1
        if hash_frequency[array[i]] > freq:
            freq = hash_frequency[array[i]]
            freq_numb = array[i]

    return freq_numb

if __name__ == "__main__":
    array = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
    print(most_frequent(array))