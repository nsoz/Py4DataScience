import sys


def isInt(value):
    """Checks if value can be converted to integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False


def main():
    """Main function for even/odd checker."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            assert isInt(sys.argv[1]), "argument is not an integer"
            val = int(sys.argv[1])
            if val % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
