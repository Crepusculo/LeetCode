w = [1, 2, 3, 4, 5, 6, 10]
v = [2, 3, 6, 28, 40, 3, 10]
n = len(w)
limit = 10


def greedy(limit):
    global w, v, n
    mark = -1
    cur_v = 0
    cur_w = 0
    max_v = 0
    cur_back = [0 for i in range(n)]

    # get p list
    p = []
    for i in range(n):
        p.append(v[i] / w[i])

    status = True
    while status:
        for i in p:
            if i == max(p):
                idx = p.index(i)
                cur_w += w[idx]
                cur_v += v[idx]
                if cur_w <= limit:
                    cur_back[idx] = 1
                    max_v = cur_v
                    p[idx] = mark
                    # print('Max Value is ', cur_v, "\t And the solution is", cur_back)
                else:
                    status = False

    print('Max Value is ', max_v, "\t And the solution is", cur_back)


greedy(limit)
