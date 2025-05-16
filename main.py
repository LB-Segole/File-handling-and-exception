import os

def read_and_write_file(input_filename, output_filename):
    """
    Reads the content of a file, modifies it, and writes it to a new file.

    Args:
        input_filename (str): The name of the file to read.
        output_filename (str): The name of the file to write to.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: File not found - {input_filename}")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper()

    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Successfully wrote modified content to {output_filename}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def get_filename_and_handle_errors():
    """
    Prompts the user for a filename and handles potential errors when reading it.
    """
    filename = input("Enter the name of the file to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"File content:\n{content}")
        return filename  # Return filename if successfully read
    except FileNotFoundError:
        print(f"Error: File not found - {filename}")
        return None  # Return None to indicate failure
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    """
    Main function to run the file read/write and error handling tasks.
    """
    input_file = get_filename_and_handle_errors()
    if input_file:  # Only proceed if a file was successfully read
        output_file = "output.txt"  # You can change this name
        read_and_write_file(input_file, output_file)

if __name__ == "__main__":
    main()
