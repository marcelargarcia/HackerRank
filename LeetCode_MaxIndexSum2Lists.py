#https://leetcode.com/problems/minimum-index-sum-of-two-lists
import sys
def findRestaurant(list1, list2):
    min_index = sys.maxsize
    list_result = []
    mapRest = {}
    for i in range(len(list1)):
        mapRest[list1[i]]= i
    for j in range(len(list2)):
        key = list2[j]
        if key in mapRest.keys():
            soma = mapRest.get(key) + j
            if soma == min_index:
                list_result.append(key)
            elif soma < min_index:
                min_index = soma
                list_result.clear()
                list_result.append(key)
    return list_result

print(findRestaurant(["happy","sad","good"],["sad","happy","good"]))
print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))
print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))