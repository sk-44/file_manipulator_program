import sys
import os


def reverse_file(input_file: str, output_file: str):
    content = ""
    with open(input_file, "r", encoding="utf-8") as infile:
        content = infile.read()[::-1]
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(content)
    return True


def copy_file(input_file: str, output_file: str):
    content = ""
    with open(input_file, "r", encoding="utf-8") as infile:
        content = infile.read()
    with open(output_file, "w", encoding="utf-8") as outfile:
        outfile.write(content)
    return True


def duplicate_contents(input_file: str, n: int):
    if int(n) < 1:
        print("Error: The number of duplicates must be at least 1.")
        return False

    content = ""
    with open(input_file, "r+", encoding="utf-8") as infile:
        content = infile.read()
        infile.write(content * int(n))
    return True


def replace_string(input_file: str, needle: str, newstring: str):
    content = ""
    with open(input_file, "r", encoding="utf-8") as infile:
        content = infile.read()
    with open(input_file, "w", encoding="utf-8") as outfile:
        replaced_content = content.replace(needle, newstring)
        outfile.write(replaced_content)
    return True


def main():
    if len(sys.argv) < 2:
        print("Error: No command provided.")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if len(args) == 0:
        print("Error: No input file specified.")
        sys.exit(1)

    if not os.path.isfile(args[0]):
        print(f"Error: file {args[0]} does not exist.")
        sys.exit(1)

    if command == "reverse":
        if len(args) == 2:
            reverse_file(args[0], args[1])
        else:
            print("Usage: python3 file_manipulator_program.py reverse <input_path> <output_path>")
            sys.exit(1)
    elif command == "copy":
        if len(args) == 2:
            copy_file(args[0], args[1])
        else:
            print("Usage: python3 file_manipulator_program.py copy <input_path> <output_path>")
            sys.exit(1)
    elif command == "duplicate-contents":
        if len(args) == 2:
            duplicate_contents(args[0], args[1])
        else:
            print("Usage: python3 file_manipulator_program.py duplicate-contents <input_path> <number_of_duplicates>")
            sys.exit(1)
    elif command == "replace-string":
        if len(args) == 3:
            replace_string(args[0], args[1], args[2])
        else:
            print("Usage: python3 file_manipulator_program.py replace-string <input_path> <target_string> <replace_string>")
            sys.exit(1)
    else:
        print("Error: Invalid command or incorrect arguments.")
        sys.exit(1)


if __name__ == "__main__":
    main()