# Implement alpha_beta pruning function to get the value of root node
import math


# TODO: Implement your alpha beta pruning function here

def max_val(a, b):
    return a if a > b else b


def min_val(a, b):
    return a if a < b else b


def ab_prune(alpha, beta, values, depth, index, maxx):
    num_children = 2
    if depth == 3:
        return values[index]
    if maxx:
        c_val = alpha
        for i in range(num_children):
            c_val = max_val(c_val, ab_prune(alpha, beta, values, depth + 1, index * 2 + 1, False))
            alpha = max_val(alpha, c_val)
            if alpha >= beta:
                break
        return c_val
    else:
        c_val = beta
        for i in range(num_children):
            c_val = min_val(c_val, ab_prune(alpha, beta, values, depth + 1, index * 2 + 1, True))
            beta = min_val(beta, c_val)

            if beta <= alpha:
                break
        return c_val


leaf_node_values = [6, 8, 9, 12, 4, 5, 3, 2]
alpha = -999
beta = 999
root_node_value = ab_prune(alpha, beta, leaf_node_values, 0, 0, True)
print("value of node is: ", root_node_value)
