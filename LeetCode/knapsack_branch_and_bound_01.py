#!/usr/bin/python
# -*- coding: utf-8 -*-

capacity = 30
weights = [10, 10, 10, 10]
values = [13, 11, 15, 20]
result = None
kp_stack = []
kp_tree = []


class TreeNode:
    def __init__(self):
        self.parent = None
        self.remain = 0
        self.bound = 0
        self.id = -1
        self.is_taken = False
        self.room = None


def branch_bound():
    global capacity, weights, values, kp_tree, kp_stack
    items = len(values) - 1
    cur_take = [False] * (items+1)
    root = TreeNode()

    # Get density and sort by it
    value_per_weight = [[each[0][0], each[0][1] / each[1]] for each in zip(enumerate(values), weights)]
    value_per_weight.sort(key=lambda pair: pair[1], reverse=True)

    weights = [weights[element[0]] for element in value_per_weight]
    values = [values[element[0]] for element in value_per_weight]

    # Initial root node
    root.room = capacity
    root.remain = get_bound(items, root, value_per_weight)
    kp_tree.append(root)
    kp_stack.append(root)

    # Still stack not empty
    while kp_stack:
        go_branch(items, value_per_weight)

    node = result
    # back track to root
    while node.parent:
        cur_take[value_per_weight[node.id][0]] = node.is_taken
        print(value_per_weight, node.room, node.bound)
        node = node.parent

    return result.bound, cur_take


def get_bound(items, root, value_per_weight):
    global weights, values
    cur_id = root.id
    cur_bound = root.bound
    cur_room = root.room
    while cur_id < items and 0 <= cur_room - weights[cur_id + 1]:
        cur_bound += values[cur_id + 1]
        cur_room -= weights[cur_id + 1]
        cur_id += 1

    # new bound = min(weights)*p
    if cur_id < items and cur_room > 0:
        cur_bound = cur_bound + value_per_weight[cur_id + 1][1] * min(cur_room - weights[cur_id+1], weights[cur_id + 1])

    return cur_bound


def go_branch(items, value_per_weight):
    global result, kp_tree, kp_stack, values, weights

    if not kp_stack:
        return
    else:
        root = kp_stack.pop()

    if result and root.remain < result.bound:
        return
    elif root.id == items:
        return

    # get
    node = TreeNode()
    node.id = root.id + 1
    node.room = root.room
    if node.room >= 0:
        node.bound = root.bound
        node.is_taken = False
        node.remain = get_bound(items, node, value_per_weight)
        node.parent = root
        kp_stack.append(node)
        if node.bound == node.remain:
            if result and node.bound > result.bound:
                result = node
            elif result is None:
                result = node

    kp_tree.append(node)

    # do not
    node = TreeNode()
    node.id = root.id + 1
    node.room = root.room - weights[node.id]
    if node.room >= 0:
        node.bound = root.bound + values[node.id]
        node.is_taken = True
        node.remain = get_bound(items, node, value_per_weight)
        node.parent = root
        kp_stack.append(node)
        if node.bound == node.remain:
            if result and node.bound > result.bound:
                result = node
            elif result is None:
                result = node

    kp_tree.append(node)


if __name__ == '__main__':
    value, taken = branch_bound()
    print("Max Weight is " + str(value) + "\t And the pack is: ", taken)
