
if __name__ == '__main__':
    from .largest_common_subgraph import *
    from .directed_hamiltonian_circuit import *
    from .graph_homomorphism import *
    from .hamiltonian_circuit import *
    from .planar_subgraph import *
    from .induced_path import *
    from .graph_grundy_numbering import *
    from .partition_into_hamiltonian_subgraphs import *
    from .elimination_degree_sequence import *
    from .partition_into_perfect_matchings import *
    from .weighted_diameter import *
    from .threshold_number import *
    from .achromatic_number import *
    from .covering_by_complete_bipartite_subgraphs import *
    from .path_with_forbidden_pairs import *
    from .kernel import *
    from .graph_contractibility import *
    from .clique import *
    from .metric_dimension import *
    from .hamiltonian_completion import *
    from .feedback_vertex_set import *
    from .graph_k_colourability_chromatic_number import *
    from .transitive_subgraph import *
    from .interval_graph_completion import *
    from .nesetril_rodl_dimension import *
    from .covering_by_cliques import *
    from .partition_into_triangles import *
    from .degree_bounded_connected_subgraph import *
    from .hamiltonian_path import *
    from .domatic_number import *
    from .partition_into_cliques import *
    from .monochromatic_triangle import *
    from .path_distinguishers import *
    from .bipartite_subgraph import *
    from .dominating_set import *
    from .partial_feedback_edge_set import *
    from .intersection_graph_basis import *
    from .bandwidth import *
    from .subgraph_isomorphism import *
    from .partition_into_isomorphic_subgraphs import *
    from .partition_into_forests import *
    from .minimum_k_connected_subgraph import *
    from .induced_connected_subgraph_with_property_pi import *
    from .minimum_equivalent_digraph import *
    from .feedback_arc_set import *
    from .edge_subgraph import *
    from .path_graph_completion import *
    from .minimum_maximal_matching import *
    from .rooted_tree_arrangement import *
    from .induced_subgraph_with_property_pi import *
    from .optimal_linear_arrangement import *
    from .digraph_d_morphism import *
    from .directed_bandwidth import *
    from .directed_optimal_linear_arrangement import *
    from .balanced_complete_bipartite_subgraph import *
    from .directed_elimination_ordering import *
    from .multiple_choice_matching import *
    from .unconnected_subgraph import *
    from .vertex_cover import *
    from .oriented_diameter import *
    from .maximum_subgraph_matching import *
    from .k_closure import *
    from .cubic_subgraph import *
    from .independent_set import *
    from .minimum_cut_linear_arrangement import *

def test():
    print("Testing p_vs_np.graph_theory.__init__...")
    main()
    print("p_vs_np.graph_theory.__init__ passed.")


if __name__ == '__main__':
    main()
