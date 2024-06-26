
if __name__ == '__main__':
    from .chinese_postman_for_mixed_graphs import *
    from .rural_postman import *
    from .bounded_component_spanning_tree import *
    from .network_survivability import *
    from .network_reliability import *
    from .shortest_weight_constrained_path import *
    from .degree_constrained_spanning_tree import *
    from .graph_partition import *
    from .maximum_leaf_spanning_tree import *
    from .strong_connectivity_augmentation import *
    from .biconnectivity_augmentation import *
    from .longest_path import *
    from .kth_shortest_path import *
    from .multiple_choice_branching import *
    from .bottleneck_travelling_salesman import *
    from .bounded_diameter_spanning_tree import *
    from .isomorphic_spanning_tree import *
    from .geometric_capacitated_spanning_tree import *
    from .kth_best_spanning_tree import *
    from .shortest_total_path_length_spanning_tree import *
    from .stacker_crane import *
    from .optimum_communication_spanning_tree import *
    from .acyclic_partition import *
    from .geometric_steiner_tree import *
    from .steiner_tree_in_graphs import *
    from .longest_circuit import *
    from .max_cut import *
    from .capacitated_spanning_tree import *
    from .minimum_cut_into_bounded_sets import *

def test():
    print("Testing p_vs_np.network_design.__init__...")
    main()
    print("p_vs_np.network_design.__init__ passed.")


if __name__ == '__main__':
    main()
