from tree import Tree


if __name__ == '__main__':
    growing_tree = Tree()
    while True:
        user_input = input("""
        type:
        'water' - to water the tree
        'q' to quit
        """)

        if user_input == "water":
            growing_tree.water()
        elif user_input == "q":
            break
