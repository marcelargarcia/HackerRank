#https://leetcode.com/problems/daily-temperatures/
import collections
import operator

def dailyTemperatures(temperatures):
    stack = []
    resp = [0] * len(temperatures)
    for i in range(len(temperatures)):
        t = temperatures[i]
        while stack and temperatures[stack[-1]] < t:
            cur = stack.pop()
            resp[cur] = i-cur
        stack.append(i)
    return resp

def dailyTemperatures_1(temperatures): #Run Time
    resp = [0] * len(temperatures)
    for i in reversed(range(len(temperatures))):
        act = temperatures[i]
        if i == len(temperatures)-1:
            continue
        else:
            for j in range(i+1,len(temperatures)):
                next = temperatures[j]
                if next > act:
                    resp[i] = j-i
                    break
    return resp


def dailyTemperatures_2(temperatures): #wrong
    temp_hmap = {}
    for i in range(len(temperatures)):
        temp = temperatures[i]
        temp_hmap[i] = temp

    #Sort hash map by values
    temp_sort = collections.OrderedDict(sorted(temp_hmap.items(), key=operator.itemgetter(1)))
    resp = [0] * len(temperatures)

    for t in range(len(temperatures)):
        temp = temperatures[t]
        if t == len(temperatures)-1:
            resp[t] = 0
        else:
            if temperatures[t+1] > temp:
                resp[t] = 1
            else:
                for k,v in temp_sort.items():
                    if v > temp and k>t:
                        resp[t] = k - t
                        break;
    return resp


#print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))
