import json, time, tracemalloc
from VertexCoverDP import addEdge, minSizeVertexCover
from VertexCoverBNB import VC_Size, create_graph, BnB

def load_adjacency_list(filename):
    with open(filename, 'r') as file:
        adj = json.load(file)
    return adj
    

def main():

    # Load the generated tree

    small_tree = load_adjacency_list("dataset/small_tree.json")
    medium_tree = load_adjacency_list("dataset/medium_tree.json")
    large_tree = load_adjacency_list("dataset/large_tree.json")

    # Experiment for Dynamic Programming Algorithm - Running Time

    print("Minimum Size Vertex Cover - Dynamic Programming:\n")

    print("Minimum Size Vertex Cover for Small Tree:")
    start_time = time.time()
    minSizeVertexCover(small_tree, len(small_tree))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Execution time in milliseconds
    print(f"Lama waktu: {execution_time} ms")

    print("Minimum Size Vertex Cover for Medium Tree:")
    start_time = time.time()
    minSizeVertexCover(medium_tree, len(medium_tree))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Execution time in milliseconds
    print(f"Lama waktu: {execution_time} ms")


    print("Minimum Size Vertex Cover for Large Tree:")
    start_time = time.time()
    minSizeVertexCover(large_tree, len(large_tree))
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Execution time in milliseconds
    print(f"Lama waktu: {execution_time} ms")

    # Experiment for Dynamic Programming Algorithm - Memory Allocation

    tracemalloc.start() 
    minSizeVertexCover(small_tree, len(small_tree))
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    print(f"Small Tree DP - Peak Memory Usage: {peak / (1024 ** 2):.2f} MB")  # Convert to MB

    tracemalloc.start()
    minSizeVertexCover(medium_tree, len(medium_tree))
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    print(f"Medium Tree DP - Peak Memory Usage: {peak / (1024 ** 2):.2f} MB")  # Convert to MB

    tracemalloc.start() 
    minSizeVertexCover(large_tree, len(large_tree))
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    print(f"Large Tree DP - Peak Memory Usage: {peak / (1024 ** 2):.2f} MB")  # Convert to MB

    print("==========================================================================\n")

    # Slice the Vertices List

    small_tree = [[v for v in node_list if v <= 100] for node_list in small_tree[:101] if node_list and node_list[0] <= 100]
    medium_tree = [[v for v in node_list if v <= 300] for node_list in medium_tree[:301] if node_list and node_list[0] <= 300]
    large_tree = [[v for v in node_list if v <= 900] for node_list in large_tree[:901] if node_list and node_list[0] <= 900]

    # Experiment for Branch and Bound Algorithm - Running Time

    print("Minimum Size Vertex Cover - Branch and Bound:\n")

    small_tree = create_graph(small_tree)
    print('No of nodes in G:', small_tree.number_of_nodes(), '\nNo of Edges in G:', small_tree.number_of_edges())

    Sol_VC, times = BnB(small_tree, 1200)

    for element in Sol_VC:
        if element[1] == 0:
            Sol_VC.remove(element)

    print('Solution VC:', Sol_VC, VC_Size(Sol_VC))
    print('Times', times * 1000, 'ms') # Execution time in milliseconds

    medium_tree = create_graph(medium_tree)
    print('No of nodes in G:', medium_tree.number_of_nodes(), '\nNo of Edges in G:', medium_tree.number_of_edges())

    Sol_VC, times = BnB(medium_tree, 1200)

    for element in Sol_VC:
        if element[1] == 0:
            Sol_VC.remove(element)

    print('Solution VC:', Sol_VC, VC_Size(Sol_VC))
    print('Times', times * 1000, 'ms') # Execution time in milliseconds

    large_tree = create_graph(large_tree)
    print('No of nodes in G:', large_tree.number_of_nodes(), '\nNo of Edges in G:', large_tree.number_of_edges())

    Sol_VC, times = BnB(large_tree, 1200)

    for element in Sol_VC:
        if element[1] == 0:
            Sol_VC.remove(element)

    print('Solution VC:', Sol_VC, VC_Size(Sol_VC))
    print('Times', times, * 1000, 'ms') # Execution time in milliseconds

    # Experiment for Branch and Bound Algorithm - Memory Allocation

    tracemalloc.start() 
    BnB(small_tree, 1200)
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    print(f"Small Tree BNB - Peak Memory Usage: {peak / (1024 ** 2):.2f} MB")  # Convert to MB

    tracemalloc.start()
    BnB(medium_tree, 1200)
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    print(f"Medium Tree BNB - Peak Memory Usage: {peak / (1024 ** 2):.2f} MB")  # Convert to MB

    tracemalloc.start() 
    BnB(large_tree, 1200)
    current, peak = tracemalloc.get_traced_memory() 
    tracemalloc.stop() 
    print(f"Large Tree BNB - Peak Memory Usage: {peak / (1024 ** 2):.2f} MB")  # Convert to MB
    

if __name__ == "__main__":
    main()
    