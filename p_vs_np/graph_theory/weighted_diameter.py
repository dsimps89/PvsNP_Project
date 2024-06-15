#Weighted Diameter


# Define the weighted graph

# Add edges and nodes to the graph

# Initialize the diameter

# Iterate over all nodes in the graph
    # Use the Dijkstra's algorithm to find the shortest path from the current node
    # Find the longest simple path
    # Update the weighted diameter if needed

# Print the result

if __name__ == '__main__':
    import heapq
    G = nx.Graph()
    G.add_edges_from([(1,2,3), (2,3,2), (3,4,1)])
    weighted_diameter = 0
    for node in G.nodes():
        dist, pred = nx.single_source_dijkstra(G, node)
        diameter = max(dist.values())
        if diameter > weighted_diameter:
            weighted_diameter = diameter
    print("The weighted diameter of the graph is: ", weighted_diameter)

def test():
    print("Testing p_vs_np.graph_theory.weighted_diameter...")
    main()
    print("p_vs_np.graph_theory.weighted_diameter passed.")


if __name__ == '__main__':
    main()
