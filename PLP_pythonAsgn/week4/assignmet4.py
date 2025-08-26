def modify_content(content: str) -> str:
    lines = content.splitlines()
    return "\n".join(f"{i+1}: {line}" for i, line in enumerate(lines))

def main():
    try:
        filename = input("Enter the file name: ").strip()
        with open(filename, "r") as infile:
            content = infile.read()

        modified = modify_content(content)
        new_filename = "modified_" + filename

        with open(new_filename, "w") as outfile:
            outfile.write(modified)

        print(f"Modified file saved as {new_filename}")

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
