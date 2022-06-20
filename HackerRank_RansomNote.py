# https://www.hackerrank.com/challenges/ctci-ransom-note/problem


# O(max(N,M))
def checkMagazine(magazine, note):
    magazine_dict = {}
    note_dict = {}
    resp = True

    for i in range(len(note)):
        if note_dict.get(note[i], 'Not Found') == 'Not Found':
            note_dict[note[i]] = 1
        else:
            freq = note_dict.get(note[i])
            note_dict[note[i]] = freq+1

    for j in range(len(magazine)):
        if magazine_dict.get(magazine[j], 'Not Found') == 'Not Found':
            magazine_dict[magazine[j]] = 1
        else:
            freq = magazine_dict.get(magazine[j])
            magazine_dict[magazine[j]] = freq+1

    for word_node, freq_note in note_dict.items():
        if magazine_dict.get(word_node, 'Not Found') != 'Not Found':
            freq_mag = magazine_dict.get(word_node)
            if freq_mag < freq_note:
                resp = False
                break
        else:
            resp = False
            break

    if resp:
        print('Yes')
    else:
        print('No')


#O(n2)
def checkMagazine_2 (magazine, note):
    for i in range(len(note)):
        if note.count(note[i]) > magazine.count(note[i]):
            print('No')
            return

    print('Yes')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)




