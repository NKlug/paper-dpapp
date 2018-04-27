from python.Nodes import TreeNode


def compute_split_tree(S, i, j):
    if i == j:
        return TreeNode(interval=(i, j), name=S[i])
    else:
        z = (S[i] + S[j]) / 2
        k = get_k_index(S, z)
        v = compute_split_tree(S, i, k)
        w = compute_split_tree(S, k + 1, j)
        return TreeNode(left=v, right=w, interval=(i, j))


def get_k_index(S, z):
    # TODO: Use binary search
    k = 0
    while z >= S[k+1]:
        k += 1
    return k


def tree_to_list(T):
    tree_list = []
    recursive_tree_to_list(T, tree_list)
    return tree_list


def recursive_tree_to_list(node, tree_list):
    tree_list.append(node)
    if node.left is not None:
        recursive_tree_to_list(node.left, tree_list)
    if node.right is not None:
        recursive_tree_to_list(node.right, tree_list)
