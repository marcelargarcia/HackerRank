# https://leetcode.com/problems/keys-and-rooms
from collections import deque
def canVisitAllRooms(rooms):
    tocheck = deque([0])
    visited = set()
    while tocheck:
        i = tocheck.pop()
        key_list = rooms[i]
        j = 0
        for j in range(len(key_list)):
            roomNumber = key_list[j]
            if roomNumber not in visited and roomNumber not in tocheck:
                tocheck.append(roomNumber)
        visited.add(i)

    if len(visited) == len(rooms):
        return True
    return False

print(canVisitAllRooms([[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]]))
print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))
print(canVisitAllRooms([[1],[2],[3],[]]))