import markdown
import os, sys


def convert_markdown(input_file: str, output_file: str):
    with open(input_file, "r", encoding="utf-8") as infile:
        context = infile.read()
    with open(output_file, "w", encoding="utf-8") as outfile:
        md = markdown.Markdown(extensions=["extra", "tables"])
        tohtml = md.convert(context)
        outfile.write(tohtml)


def main():
    if len(sys.argv) != 4:
        print("Usage: file-converter.py markdown <iputfile_path> <outputfile_path>")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if not os.path.isfile(args[0]):
        print(f"Error: file {args[0]} does not exist.")
        sys.exit(1)

    if command == "markdown":
        convert_markdown(args[0], args[1])
    else:
        print("Error: Invalid command.")
        sys.exit(1)


if __name__ == "__main__":
    main()
