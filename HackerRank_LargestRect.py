# https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

# [1,3,3,4,5]
# [3,2,3]
# [2,3,2]
def largestRectangle(h):
    left = 0
    center = h[0]
    right = 0
    area = h[0]
    limit = h[0]
    for i in range(1, len(h)):
        left = center
        center = h[i]
        if i < len(h) - 1:
            right = h[i + 1]
        else:
            right = 0

        if center > limit:
            if area + limit +


def largestRectangle_incomplete(h):
    area = h[0]
    limitH = area
    lastH = area
    for i in range(1, len(h)):
        if h[i] > limitH:
            if area + limitH < h[i]:
                area = h[i]
                limitH = h[i]
            elif lastH > limitH:
                if h[i] == lastH:
                    area = h[i] + lastH
                    limitH = h[i]
                elif h[i] > lastH:
                    area = lastH * 2
                    limitH = lastH

                area = h[i] + lastH
            else:
                area = area + limitH
        elif h[i] == limitH:
            area = area + limitH
        else:
            print('teste')
    return area


if __name__ == '__main__':
    print(largestRectangle([1, 2, 3, 4, 5]))
