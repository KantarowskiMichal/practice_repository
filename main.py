from tree import Tree


if __name__ == '__main__':
    growing_tree = Tree()
    while True:
        user_input = input("""
        type:
        'water' - to water the tree
        'chop' - to chop the tree down
        'q' to quit
        """)

        if user_input == "water":
            growing_tree.water()
        elif user_input == "chop":
            growing_tree.chop()
        elif user_input == "q":
            break
