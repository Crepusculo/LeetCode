n = 5
color = [1, 2, 3, 4]
point = [0 for i in range(n)]
matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 0],
]

ret = []


def backtrack(ptr):
    global n, ret
    # if 直到完成都没有冲突
    if ptr >= n:
        conflict = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1 and point[j] == point[i]:
                    conflict += 1
        # if 着色不冲突
        if conflict == 0:
            ret = point[:]
    else:
        for i in color:
            # recursion
            point[ptr] = color.index(i)
            backtrack(ptr + 1)


def main():
    backtrack(0)

    print("And the solution is", ret)


if __name__ == '__main__':
    main()
