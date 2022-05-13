#https://www.udemy.com/course/11-essential-coding-interview-questions/learn/lecture/7450632#overview

def common_elements(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    return set1.intersection(set2)
    # set1 & set2

if __name__ == "__main__":
    print(common_elements([1,3,4,6,7,9],[1,2,4,5,9,10]))