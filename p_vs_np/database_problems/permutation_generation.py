#Permutation Generation



# Example usage



if __name__ == '__main__':
    from itertools import permutations
    def generate_permutations(elements):
        return list(permutations(elements))
    elements = [1, 2, 3]
    permutations = generate_permutations(elements)
    print("Permutations:")
    for perm in permutations:
        print(perm)

def test():
    print("Testing p_vs_np.database_problems.permutation_generation...")
    main()
    print("p_vs_np.database_problems.permutation_generation passed.")


if __name__ == '__main__':
    main()
