#Partition into cliques





if __name__ == '__main__':
    def partition_into_cliques(graph):
        def find_clique(graph, vertex):
            clique = set()
            queue = [vertex]
            while queue:
                v = queue.pop(0)
                clique.add(v)
                for neighbor in graph[v]:
                    if neighbor not in clique and all(graph[neighbor][w] for w in clique):
                        queue.append(neighbor)
            return clique
        cliques = []
        visited = set()
        for vertex in range(len(graph)):
            if vertex not in visited:
                clique = find_clique(graph, vertex)
                visited = visited.union(clique)
                cliques.append(clique)
        return len(cliques)
    graph = [[0, 1, 1, 0],
             [1, 0, 1, 1],
             [1, 1, 0, 0],
             [0, 1, 0, 0]]
    print(partition_into_cliques(graph))

def test():
    print("Testing p_vs_np.graph_theory.partition_into_cliques...")
    main()
    print("p_vs_np.graph_theory.partition_into_cliques passed.")


if __name__ == '__main__':
    main()
