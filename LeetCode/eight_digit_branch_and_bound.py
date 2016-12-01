import copy

ugly = []

raw = [0, 3, 4,
       5, 2, 7,
       8, 1, 6]

target = [5, 3, 4,
          0, 7, 6,
          8, 1, 2]


def ebb():
    global raw, target
    '''
    !IMPORTANT
    如果助教要验证正确性请务必按照下列注释改变state中的参数
    '''
    # move_times, matrix, zero_position, diff_zone, route
    state = [
        0,  # move_times
        copy.deepcopy(raw),  # matrix
        0,  # zero_position
        cmp([0, raw]),  # diff_zone
        []  # route
    ]

    queue = [state]
    while len(queue):
        qstate = queue.pop(0)
        if target == qstate[1]:
            return qstate
        for xstate in [move_up(qstate), move_down(qstate), move_right(qstate), move_left(qstate)]:
            if xstate[1] != qstate[1] and xstate[1] not in ugly:
                    ugly.append(xstate[1])
                    queue.append(xstate)
                    print(xstate, "\n\n")
    pass


def move_up(prestate):
    state = copy.deepcopy(prestate)
    # 0 at p 0,1,2
    if state[2] < 3:
        return state
    # 0 at p 3,4,5,6,7,8
    else:
        state[0] += 1
        state[1][state[2]], state[1][state[2] - 3] = state[1][state[2] - 3], state[1][state[2]]
        state[2] -= 3
        state[3] = cmp(state)
        state[4].append("Move Up")

        return state
    pass


def move_down(prestate):
    state = copy.deepcopy(prestate)
    # 0 at p 6,7,8
    if state[2] > 5:
        return state
    # 0 at p 0,1,2,3,4,5
    else:
        state[0] += 1
        state[1][state[2]], state[1][state[2] + 3] = state[1][state[2] + 3], state[1][state[2]]
        state[2] += 3
        state[3] = cmp(state)
        state[4].append("Move Down")
        return state
    pass


def move_right(prestate):
    state = copy.deepcopy(prestate)
    # 0 at p 0,3,6
    if state[2] % 3 == 2:
        return state
    # 0 at p 1,2, 4,5 7,8
    else:
        state[0] += 1
        state[1][state[2]], state[1][state[2] + 1] = state[1][state[2] + 1], state[1][state[2]]
        state[2] += 1
        state[3] = cmp(state)
        state[4].append("Move Right")
        return state
    pass


def move_left(prestate):
    state = copy.deepcopy(prestate)
    # 0 at p 2,5,8
    if state[2] % 3 == 0:
        return state
    # 0 at p 0,1, 3,4, 6,7,
    else:
        state[0] += 1
        state[1][state[2]], state[1][state[2] - 1] = state[1][state[2] - 1], state[1][state[2]]
        state[2] -= 1
        state[3] = cmp(state)
        state[4].append("Move Left")
        return state
    pass


def cmp(state1):
    cnt = 0
    for inx, each1 in enumerate(state1[1]):
        if each1 != target[inx]:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print("Ret:", ebb())
