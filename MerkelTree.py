import hashlib


def hash(val):
    return hashlib.sha256(val.encode('utf-8')).hexdigest()
# hash('a')


ls = ['1', '2', '3', '4', '5']


def merkel_tree_without_hash(ls):
    temp = ls.copy()
    tree = {}
    last = ""
    if len(temp) % 2 == 1:  # if there are odd terms in the list
        last = temp.pop()
    while(len(temp) > 1):
        temp2 = []
        for i in range(0, len(temp), 2):
            left, right = temp[i], temp[i+1]
            node = left+right
            temp2.append(node)
            tree[node] = [left, right]
        # after one iteration through list set temp = temp2
        temp = temp2

    # print(tree)
    if last == "":  # if last is empty string then original list had even terms
        return node, tree  # return node (merkel root) and tree (dictionary)

    # if  if there are odd terms in the list then last will have some value
    root = node+last
    tree[root] = [node, last]
    return root, tree


merkel_tree_without_hash(ls)


def merkel_tree(ls):
    temp = ls.copy()
    tree = {}
    last = ""
    if len(temp) % 2 == 1:  # if there are odd terms in the list
        last = temp.pop()
    while(len(temp) > 1):
        temp2 = []
        for i in range(0, len(temp), 2):
            left, right = temp[i], temp[i+1]
            node = hash(left+right)
            temp2.append(node)
            tree[node] = [left, right]
        # after one iteration through list set temp = temp2
        temp = temp2

    # print(tree)
    if last == "":  # if last is empty string then original list had even terms
        return node, tree  # return node (merkel root) and tree (dictionary)

    # if  if there are odd terms in the list then last will have some value
    root = hash(node+last)
    tree[root] = [node, last]
    return root, tree


m_root, m_tree = merkel_tree(ls)

print("merkel root: ", m_root)

for node, children in m_tree.items():
    print(node, ":")
    print("L -> ", children[0])
    print("R -> ", children[1])
    print('\n')
