# num of machine
m_num = 5
# array of works cost
cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4]


def mmsp(num):
    machines = [["MachineIdx: " + str(i), 0, []] for i in range(num)]
    cost.sort(key=lambda x: x)
    for each in cost:
        target = min(machines, key=lambda x: x[1])
        target[1] += each
        target[2].append(each)
    return machines

if __name__ == '__main__':
    ret = mmsp(m_num)
    for i in ret:
        print(i)

