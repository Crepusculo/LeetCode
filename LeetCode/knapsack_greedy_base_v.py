w = [1, 2, 3, 4, 5, 6, 10]
v = [4, 4, 4, 8, 10, 3, 10]
n = len(w)
limit = 15


def greedy(limit):
    global w, v, n
    cur_w = 0
    cur_v = 0
    l = [[x, y] for x, y in zip(w, v)]
    l.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(l)
    for i in l:
        print(i[0], i[1])
        if cur_w + i[0] <= limit:
            cur_w += i[0]
            cur_v += i[1]
            print("pick! v:", cur_v, "w:", cur_w)

    print(cur_v, cur_w)
    return cur_v, cur_w


print(greedy(limit))
