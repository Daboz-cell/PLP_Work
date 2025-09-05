import os

def process_file():
    try:
        # Get input filename from user
        input_filename = input("Enter the input filename: ")
        
        # Check if file exists
        if not os.path.exists(input_filename):
            raise FileNotFoundError(f"The file '{input_filename}' does not exist.")
        
        # Check if file is readable
        if not os.access(input_filename, os.R_OK):
            raise PermissionError(f"No permission to read '{input_filename}'.")
        
        # Read the input file
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            content = input_file.read()
        
        # Modify the content (example: convert to uppercase and add line numbers)
        lines = content.splitlines()
        modified_content = []
        for i, line in enumerate(lines, 1):
            modified_content.append(f"Line {i}: {line.upper()}")
        
        # Create output filename
        output_filename = f"modified_{input_filename}"
        
        # Check if output file already exists
        if os.path.exists(output_filename):
            overwrite = input(f"'{output_filename}' already exists. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                raise FileExistsError("Operation cancelled to avoid overwriting existing file.")
        
        # Write to output file
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write('\n'.join(modified_content))
        
        print(f"File successfully processed and saved as '{output_filename}'")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except FileExistsError as e:
        print(f"Error: {e}")
    except UnicodeDecodeError:
        print("Error: Unable to decode the file. Please ensure it's a valid text file.")
    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    process_file()