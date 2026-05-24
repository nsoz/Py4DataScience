import sys


def cal(value):
    """This function is calculates the character types in the string."""
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0
    total = 0
    for char in value:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            punctuation_count += 1
        total += 1
    dic = {
            "uperCase": upper_count,
            "lowerCase": lower_count,
            "spaceCase": space_count,
            "digitCase": digit_count,
            "puncCase": punctuation_count,
            "totalCase": total
        }
    return (dic)


def main():
    """Main function - processes user input or command line arguments."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if (len(sys.argv) == 1):
            user_data = input("What is the text to count?\n")
            user_data += '\n'
        else:
            user_data = sys.argv[1]
        ret_dict = cal(user_data)
        print(f"The text contains {ret_dict['totalCase']} characters")
        print(f"{ret_dict['uperCase']} upper letters")
        print(f"{ret_dict['lowerCase']} lower letters")
        print(f"{ret_dict['puncCase']} punctuation marks")
        print(f"{ret_dict['spaceCase']} spaces")
        print(f"{ret_dict['digitCase']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
