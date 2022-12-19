import hashlib
from binarytree import Node


def hash(val):
    return hashlib.sha256(val.encode('utf-8')).hexdigest()


def build_tree(tree, r):
    root = Node(r)

    if tree[r][0] != None:
        root.left = build_tree(tree, tree[r][0])

    if tree[r][1] != None:
        root.right = build_tree(tree, tree[r][1])

    return root


def without_hash(input_string):
    tree = {}
    tree_list = []
    for i in input_string:
        tree[i] = (None, None)
    # print(tree)

    temp1 = input_string.copy()

    if len(input_string) % 2 == 1:  # odd
        last = temp1.pop(-1)
    while len(temp1) > 1:
        temp2 = []
        for i in range(0, len(temp1), 2):
            left = temp1[i]
            right = temp1[i+1]
            h = left+right
            temp2.append(h)

            tree[h] = (left, right)

        tree_list.append(temp1)
        temp1 = temp2.copy()

       # if last is a null string

    tree_list.append(temp1)

    # print(tree)

    if last != '':
        tree_list.append([last])
        odd = tree_list[-2][0]+tree_list[-1][0]
        merkel_root = odd

    else:
        merkel_root = temp1

    tree[merkel_root] = (tree_list[-2][0], tree_list[-1][0])
    tree_list.append([merkel_root])

    # print(tree)
    return merkel_root, tree


def merkel_tree(input_string):
    tree = {}
    tree_list = []
    for i in input_string:
        tree[i] = (None, None)
    # print(tree)

    temp1 = input_string.copy()

    if len(input_string) % 2 == 1:  # odd
        last = temp1.pop(-1)
    while len(temp1) > 1:
        temp2 = []
        for i in range(0, len(temp1), 2):
            left = temp1[i]
            right = temp1[i+1]
            h = hash(left+right)
            temp2.append(h)

            tree[h] = (left, right)

        tree_list.append(temp1)
        temp1 = temp2.copy()

       # if last is a null string

    tree_list.append(temp1)

    # print(tree)

    if last != '':
        tree_list.append([last])
        odd = hash(tree_list[-2][0]+tree_list[-1][0])
        merkel_root = odd

    else:
        merkel_root = temp1

    tree[merkel_root] = (tree_list[-2][0], tree_list[-1][0])
    tree_list.append([merkel_root])

    # print(tree)
    return merkel_root, tree


merkelroot, merkeltree = merkel_tree(['1', '2', '3', '4', '5'])
merkeltree
