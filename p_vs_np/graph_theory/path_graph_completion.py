#Path Graph Completion






if __name__ == '__main__':
    from itertools import combinations
    def path_graph_completion(graph):
        for edges in combinations(graph.edges(), graph.number_of_edges()):
            subgraph = graph.subgraph(edges)
            if nx.is_path(subgraph):
                return subgraph
        return None
    graph = nx.Graph()
    graph.add_edges_from([(0, 1), (1, 2)])
    subgraph = path_graph_completion(graph)
    print(subgraph.edges())

def test():
    print("Testing p_vs_np.graph_theory.path_graph_completion...")
    main()
    print("p_vs_np.graph_theory.path_graph_completion passed.")


if __name__ == '__main__':
    main()
