# num of machine
m_num = 5
# array of works cost
cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]


def mmsp(num):
    machines = [[i, 0, []] for i in range(num)]
    cost.sort(key=lambda x: x)
    for each in cost:
        target = min(machines, key=lambda x: x[1])
        target[1] += each
        target[2].append(each)
    return machines

if __name__ == '__main__':
    print(mmsp(m_num))
