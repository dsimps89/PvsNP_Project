#Boyce-Codd Normal Form Violation





# Example usage


if __name__ == '__main__':
    def is_bcnf_violation(F, R):
        for X, Y in F:
            closure = compute_closure(X, F)
            if not closure.issubset(R):
                return True
        return False
    def compute_closure(X, F):
        closure = set(X)
        updated = True
        while updated:
            updated = False
            for B, C in F:
                if B.issubset(closure) and not C.issubset(closure):
                    closure.update(C)
                    updated = True
        return closure
    R = ['A', 'B', 'C', 'D']
    F = [({'A'}, {'B'}), ({'B', 'C'}, {'D'})]
    result = is_bcnf_violation(F, R)
    if result:
        print("BCNF violation detected.")
    else:
        print("No BCNF violation.")

def test():
    print("Testing p_vs_np.database_problems.boyce_codd_normal_form_violation...")
    main()
    print("p_vs_np.database_problems.boyce_codd_normal_form_violation passed.")


if __name__ == '__main__':
    main()
