max_value = 0
cur_weight = 0
cur_value = 0
max_back = []

w = [20, 22, 61]
v = [60, 32, 51]
n = len(w)
l = 10


def backtrack(i):
    global max_value, cur_weight, cur_value, cur_back, max_back
    if i >= n:
        if max_value < cur_value:
            max_value = cur_value
            max_back = cur_back[:]
    else:
        if cur_weight + w[i] <= l:
            cur_back[i] = 1
            cur_weight += w[i]
            cur_value += v[i]

            backtrack(i + 1)

            cur_weight -= w[i]
            cur_value -= v[i]

        cur_back[i] = 0
        backtrack(i + 1)


cur_back = [0 for i in range(n)]
backtrack(0)
print(max_value)
print(max_back)
