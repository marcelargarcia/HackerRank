# https://www.hackerrank.com/interview/interview-preparation-kit

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the freqQuery function below.
def freqQuery(queries):
    freqNumb = {}
    freq_freqNumb = {}
    result = []

    for i in range(len(queries)):
        operation = queries[i][0]
        value = queries[i][1]
        freq = 0
        prev_freq = 0

        # If I never added or deleted this value. Create KEY value with 0.
        if operation in (range(1, 3)) and freqNumb.get(value, 'None') == 'None':
            freqNumb[value] = 0

        # If I want to ADD this value
        if operation == 1:
            freqNumb[value] = freqNumb[value] + 1  # freq += 1 of this value
            freq = freqNumb[value]  # New freq of the value
            prev_freq = freqNumb[value] - 1  # Previous freq of the value

            # If this is the 1st time we have a frequency like that
            if freq_freqNumb.get(freq, 'None') == 'None':
                freq_freqNumb[freq] = 1  # Update frequency number (frequency = 1)
            # If this frequency is not new at all
            else:
                freq_freqNumb[freq] = freq_freqNumb[freq] + 1  # Update frequency number

            if freq > 1:  # I don't want to count 0's frequencies
                freq_freqNumb[prev_freq] = freq_freqNumb[prev_freq] - 1  # Update previous frequency


        # If I want to DELETE this value
        elif operation == 2:
            if freqNumb[value] > 0:  # Deleting a value that has a frequency > 0

                freqNumb[value] = freqNumb[value] - 1  # freq -= 1 of this value
                freq = freqNumb[value]  # new freq of this value
                prev_freq = freqNumb[value] + 1  # Previous freq of the value

                freq_freqNumb[prev_freq] = freq_freqNumb[prev_freq] - 1  # Update previous frequency

                if freq > 0:
                    freq_freqNumb[freq] = freq_freqNumb[freq] + 1  # Update frequency number

        # OPERATION == 3
        else:
            if freq_freqNumb.get(value, 'None') == 'None' or freq_freqNumb.get(value) == 0:
                result.append('0')
            else:
                result.append('1')

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
