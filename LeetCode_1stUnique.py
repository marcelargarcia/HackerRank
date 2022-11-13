#https://leetcode.com/problems/first-unique-character-in-a-string

def firstUniqChar(s):
    mapChars = {}
    for i in range(len(s)):
        key = s[i]
        if key not in mapChars:
            value = s.count(key)
            if value == 1:
                return i
            mapChars[key] = value
    return -1

def firstUniqChar_2(s):
    setChars = set()
    for i in range(len(s)):
        key = s[i]
        if key not in setChars:
            value = s.count(key)
            if value == 1:
                return i
            setChars.add(key)
    return -1

print(firstUniqChar('leetcode'))
print(firstUniqChar('loveleetcode'))
print(firstUniqChar('aabb'))

####################################################################
#Input = 1 string
#Output = 1 integer (index of the 1st non-repeating char)
#Strategies, complexity and edge cases
#1
    #1 Strategy
        #For i ... loop (each char of the string)
            #countChar = list.count(char)
            #if countChar == 1:
                #return i
    #1 Cons
        #Time Complexity O(n2) worst case - quadratic time
        #aaaaaaaxxxxxxxxxxxxxaaaae
    #1 Pros
        #Space Complexity O(1) - no new data structure

#2
    #2 Strategy
        # Create a new Hash Map
        # For loop (each char of the string)
            #Add char in the hash map -> add +1 in the value (frequency)
        # For i loop (each char of the string)
            #Get the value of the hash map
            #If value == 1:
                #return i
    #2 Cons
        #Space Complexity O(N) - new data structure (hash map)
        #Time Complexity O(N) - best case - linear time
        #abcdefghijklmnopq

    #2 Pros
        #Time Complexity O(N) worst case - linear time
        #aaaaaaaxxxxxxxxxxxxxaaaae

#3
    #3 Strategy
        #Create a New Map
        #For i loop (each char of the string)
            #if char is not in hash map
                #list.count(char)
                #hashmap.add(char) -> value (count of the char)
            #If value == 1:
                #return i
    #3 Cons
        #Space Complexity O(N) - new data structure (hash map)
    #3 Pros
        #Time Complexity O(N) - best case
        #abcdefghijklmnopq
        #Time Complexity O(N) - worst case
        #aaaaaaaxxxxxxxxxxxxxaaaae
