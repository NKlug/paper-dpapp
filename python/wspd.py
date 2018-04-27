from python.split_tree import tree_to_list
import numpy as np


def compute_wspd(T, S, s):
    inner_nodes = [node for node in tree_to_list(T) if is_inner_node(node)]
    for node in inner_nodes:
        v = node.left
        w = node.right
        find_pairs(v, w, S, s)


def find_pairs(v, w, S, s):
    if is_well_separated(v, w, S, s):
        # Store in v, w that they form a pair of a WSPD
        v.b_nodes.append(w)
        w.a_nodes.append(v)
    else:
        i, j = v.interval
        k, l1 = w.interval
        if S[j] - S[i] <= S[l1] - S[k]:
            w1 = w.left
            w2 = w.right
            find_pairs(v, w1, S, s)
            find_pairs(v, w2, S, s)
        else:
            v1 = v.left
            v2 = v.right
            find_pairs(v1, w, S, s)
            find_pairs(v2, w, S, s)


def is_well_separated(v, w, S, s):
    i, j = v.interval
    k, l1 = w.interval
    R = np.maximum(S[j] - S[i], S[l1] - S[k])
    return S[k] - S[j] >= R * s or S[i] - S[l1] >= R * s


def is_inner_node(node):
    return node.left is not None or node.right is not None


def print_wspd(node):
    node.print_wspd()
    if node.left is not None:
        print_wspd(node.left)
    if node.right is not None:
        print_wspd(node.right)