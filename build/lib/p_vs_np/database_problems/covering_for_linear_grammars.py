#Covering for Linear Grammars

    # Initialize an empty set of non-terminals

    # Compute the set of strings generated by the grammar

    # Find the minimum set of non-terminals that cover all strings

        # Find the string with maximum coverage

        # Remove the string from the set and remove the covering non-terminals

    # Return the minimum set of non-terminals that cover all strings


# Example usage



if __name__ == '__main__':
    def find_linear_grammar_cover(grammar):
        non_terminals = set(grammar.keys())
        strings = set()
        for productions in grammar.values():
            for production in productions:
                strings.add(production)
        while strings:
            max_coverage = set()
            max_string = None
            for string in strings:
                coverage = set()
                for non_terminal, productions in grammar.items():
                    if string in productions:
                        coverage.add(non_terminal)
                if len(coverage) > len(max_coverage):
                    max_coverage = coverage
                    max_string = string
            strings.remove(max_string)
            non_terminals -= max_coverage
        return non_terminals
    grammar = {
        'S': ['aA', 'bB', ''],
        'A': ['aA', 'a'],
        'B': ['bB', 'b']
    }
    linear_grammar_cover = find_linear_grammar_cover(grammar)
    print(f"Linear Grammar Cover: {linear_grammar_cover}")
