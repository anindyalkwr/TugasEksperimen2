import json
import random

from VertexCoverDP import addEdge

def generate_tree(size):
    tree = {i: [] for i in range(1, size + 1)}
    
    for i in range(2, size + 1):
        parent = random.randint(1, i - 1)
        tree[parent].append(i)
    
    return tree

def generate_and_save_tree(size, filename):
    tree = generate_tree(size)
    adj = [[] for i in range(size + 1)]
    for vertex, children in tree.items():
        for child in children:
            addEdge(adj, vertex, child)

    with open(filename, 'w') as file:
        json.dump(adj, file)

    return adj

# Usage
generate_and_save_tree(10**4, 'small_tree.json')
generate_and_save_tree(10**5, 'medium_tree.json')
generate_and_save_tree(10**6, 'large_tree.json')