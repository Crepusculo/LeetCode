#!/usr/bin/python
# -*- coding: utf-8 -*-

capacity = 30
weights = [20, 10, 15]
values = [10, 20, 30]
BB_solution = None
BB_stack = []
BB_tree = []


class BTreeNode():
    """Structure to represent  a binary tree node in branch and bound method"""

    def __init__(self):
        self.ParentNode = None
        self.Relaxation = 0
        self.Objective = 0
        self.ObjectID = -1
        self.Taken = None
        self.Room = None


def branch_bound():
    global capacity, weights, values
    # array indicating whether an
    # element has been taken or not.
    global BB_tree, BB_stack

    # Get number of items
    items = len(values)

    # Allocate memory for taken
    taken = [0] * items

    # Create a list containing (index, value/weight)
    value_per_weight = [(elem[0][0], elem[0][1] / elem[1]) for elem in zip(enumerate(values), weights)]

    # Sort the list in descending order
    value_per_weight.sort(key=lambda pair: pair[1], reverse=True)

    # Reorder values and weights
    weights = [weights[element[0]] for element in value_per_weight]
    values = [values[element[0]] for element in value_per_weight]

    # Create root node
    Root = BTreeNode()
    # Root.Relaxation = sum(values)
    Root.Room = capacity
    Root.Objective = 0
    Root.ObjectID = -1
    Root.Relaxation = get_bound(items - 1, Root.ObjectID, Root.Room, Root.Objective, weights, values, value_per_weight)

    # Add root node to the tree
    BB_tree.append(Root)
    BB_stack.append(Root)

    # Branch while stack is not empty
    while BB_stack:
        Branch(items - 1, values, weights, value_per_weight)

    # Retrace which items were taken and which ignored
    Node = BB_solution

    while Node.ParentNode:
        taken[value_per_weight[Node.ObjectID][0]] = Node.Taken
        Node = Node.ParentNode

    return (BB_solution.Objective, taken)


def Branch(items, values, weights, value_per_weight):
    global BB_solution, BB_tree, BB_stack

    if not BB_stack:
        return
    else:
        Root = BB_stack.pop()

    if BB_solution and Root.Relaxation < BB_solution.Objective:
        return
    elif Root.ObjectID == items:
        return

    Node = BTreeNode()
    Node.ObjectID = Root.ObjectID + 1
    Node.Room = Root.Room
    if Node.Room >= 0:
        Node.Objective = Root.Objective
        Node.Taken = 0
        # Node.Relaxation = Root.Relaxation - values[Node.ObjectID]
        Node.Relaxation = get_bound(items, Node.ObjectID, Node.Room, Node.Objective, weights, values, value_per_weight)
        Node.ParentNode = Root
        # Root.RightNode = Node
        BB_stack.append(Node)
        if Node.Objective == Node.Relaxation:
            if BB_solution and Node.Objective > BB_solution.Objective:
                BB_solution = Node
            elif BB_solution is None:
                BB_solution = Node

    BB_tree.append(Node)

    Node = BTreeNode()
    Node.ObjectID = Root.ObjectID + 1
    Node.Room = Root.Room - weights[Node.ObjectID]
    if Node.Room >= 0:
        Node.Objective = Root.Objective + values[Node.ObjectID]
        Node.Taken = 1
        # Node.Relaxation = Root.Relaxation
        Node.Relaxation = get_bound(items, Node.ObjectID, Node.Room, Node.Objective, weights, values, value_per_weight)
        Node.ParentNode = Root
        # Root.LeftNode = Node
        BB_stack.append(Node)
        if Node.Objective == Node.Relaxation:
            if BB_solution and Node.Objective > BB_solution.Objective:
                BB_solution = Node
            elif BB_solution is None:
                BB_solution = Node

    BB_tree.append(Node)


def get_bound(items, rootid, root_room, root_objective, weights, values, value_per_weight):
    while rootid < items and root_room - weights[rootid + 1] >= 0:
        root_objective = root_objective + values[rootid + 1]
        root_room = root_room - weights[rootid + 1]
        rootid = rootid + 1

    if rootid < items and root_room > 0:
        root_objective = root_objective + min(root_room, weights[rootid + 1]) * value_per_weight[rootid + 1][1]

    return root_objective


import sys

if __name__ == '__main__':
    value, taken = branch_bound()
    # value, taken = BB_solver_lm(capacity, weights, values)

    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    print(outputData)
