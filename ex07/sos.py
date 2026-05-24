import sys


def morse_converter(val):
    """Converts string to Morse code."""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    morse = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--..",
        "-----", ".----", "..---", "...--", "....-", ".....",
        "-....", "--...", "---..", "----."
    ]
    NESTED_MORSE = {c: m for c, m in zip(chars, morse)}
    NESTED_MORSE[" "] = "/"
    ret = " ".join([NESTED_MORSE[x] for x in val])
    return ret


def ctrl_argv(val):
    """Validates that string contains only alphanumeric and spaces."""
    for c in val:
        if not c.isalpha() and not c.isspace() and not c.isdigit():
            return False
    return True


def main():
    """Main function - converts input to Morse code."""
    try:
        if (len(sys.argv) != 2):
            raise AssertionError("the arguments are bad")
        if not ctrl_argv(sys.argv[1]):
            raise AssertionError("the arguments are bad")
        print(morse_converter(sys.argv[1].upper()))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
