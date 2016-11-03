w = [1, 2, 3, 4, 5, 6, 10]
v = [2, 4, 6, 8, 10, 3, 10]
n = len(w)

def greedy():
    global w, v, n
    p = []
    for i in range(n):
        p.append(w[i] / v[i])

    print(p)

greedy()