arrays = [1, 2, 41, -22, -54, 5, 34, 6, 2, -34, 3, 25, 13, 22, -41, 28, 25, -7, 1, 20, 22, -70, 24, -6, 3, 20, 5, 18, 2]


def exr(arr):
    start = [arr[0], "Loc: 0"]
    ret = [-0xfffff, -1, start]
    last = [-0xfffff, -1, start]
    last = [-0xfffff, -1, start]
    flag = False
    for idx, val in enumerate(arr):

        old = last[0]
        last = [max(0, last[0]) + val, "Loc: " + str(idx), start]
        if flag is True:
            start = [last[0], last[1]]
            flag = False
        if last[0] < old and last[0] < last[2][0]:
            flag = True
        ret = max(ret, last, key=lambda x: x[0])
    return ret


if __name__ == '__main__':
    ret = exr([2, -3, 5, -4, 5, -4, 6, -3, -30, -3, 3, -2, 3, 3, 3, 3, 3, 3, 3, 3, 3])
    print("From", ret[2][1], "to", ret[1])
    print("Range sum is", ret[0])
