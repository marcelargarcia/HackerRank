# O(n2)

def find3IntegersMulitply(list, mult):
    divisiveis = []
    for m in range(len(list)):
        if mult % list[m] == 0:
            divisiveis.append(list[m])

    left = 0
    right = 2
    for i in range(1,len(divisiveis)):
        while divisiveis[left] * divisiveis[i] * divisiveis[right] != mult and left < i and right <= len(divisiveis):
            if right == len(divisiveis)-1:
                if left < i:
                    left += 1
                    right = i+1
            elif right < len(divisiveis)-1:
                right += 1

        if divisiveis[left] * divisiveis[i] * divisiveis[right] == mult:
            return divisiveis[left], divisiveis[i], divisiveis[right]
    return 0


if __name__ == "__main__":
    print(find3IntegersMulitply([2, 3, 1, 5, -20, -1], -40))
    print(find3IntegersMulitply([], 10))
