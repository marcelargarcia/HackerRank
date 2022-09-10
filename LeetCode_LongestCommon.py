# https://leetcode.com/problems/longest-common-prefix/

#O(S) S = soma de todos os caracteres de todas as strings
def longestPrefix(strings):
    if not strings:
        return ""
    prefixo = strings[0]
    for i in range(1, len(strings)):
        newPrefixo = ""
        for ch in range(0, len(prefixo)):
            if ch == len(strings[i]):
                break;
            elif prefixo[ch] == strings[i][ch]:
                newPrefixo = newPrefixo + prefixo[ch]
            else:
                break;
        if prefixo != newPrefixo:
            prefixo = newPrefixo
        if newPrefixo == "":
            break;

    return prefixo

if __name__ == '__main__':
    print(longestPrefix(['flor', 'floreio','fluor']))
    print(longestPrefix(['flor', 'mae', 'pai']))
    print(longestPrefix(['flor', 'floreio', 'florentino']))
    print(longestPrefix(['flor', 'flor', 'flor']))
    print(longestPrefix(['']))
    print(longestPrefix([]))
    print(longestPrefix(['flower', 'flow', 'flight']))
