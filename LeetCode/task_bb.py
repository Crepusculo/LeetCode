matrix = [[90, 75, 75, 80],
          [35, 85, 55, 65],
          [125, 95, 90, 105],
          [45, 110, 95, 115]]
queue = []
'''
!IMPORTANT
如果助教要验证正确性请务必按照下列注释改变state中的参数
'''
# min_value, ret_array, now_value
status = [sum([min(x) for x in matrix]), [], 0]


def task():
    queue.append(status)
    total = sum([sum(x) for x in matrix])
    best = [total, [], total]
    while len(queue):
        xstatus = queue.pop()
        if xstatus[0] > best[2]:
            break
        if len(xstatus[1]) == len(matrix[0]):
            if xstatus[2] < best[2]:
                best = xstatus
        else:
            for inx, n in enumerate(matrix):
                if inx not in xstatus[1]:
                    qstatus = [
                        xstatus[2] + matrix[len(xstatus[1])][inx] + sum([min(x) for x in matrix[len(xstatus[1]) + 1:]]),
                        xstatus[1] + [inx],
                        xstatus[2] + matrix[len(xstatus[1])][inx]
                    ]
                    queue.append(qstatus)
    return best


if __name__ == "__main__":
    print("Ret:", task())
