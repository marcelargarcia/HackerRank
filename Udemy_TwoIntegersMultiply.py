# https://www.udemy.com/course/11-essential-coding-interview-questions
# O(n)

def find2Integers(list, mult):
    #list.sort() # O(N log N) [-1, 1, 2, 4, 5, 15, 40]
    visited = set()
    i = 0
    while i < len(list):
        k = list[i]
        div = mult / k
        if div in visited:
            return k, div
        else:
            visited.add(k)
            i+= 1



if __name__ == "__main__":
    print(find2Integers([2,4,1,6,5,40,-1], 30))