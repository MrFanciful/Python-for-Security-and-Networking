import argparse

if __name__ == "__main__":
    description = """
    Use cases:
    
    + Basic scan:
        - target 127.0.0.1
    + Specific port:
        - target 127.0.0.1 -port 21
    + Port list:
        - target 127.0.0.1 -port 21,22
    + Only show open ports:
        - target 127.0.0.1 --open True
    """

    parser = argparse.ArgumentParser(description='Port scanning', epilog=description,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-target', metavar='TARGET', dest='target', help='target to scan', required=True )
    parser.add_argument('-ports', dest='ports', help='')