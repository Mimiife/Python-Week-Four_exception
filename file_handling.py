def read_and_write_file():
    try:
        # User input 
        input_file = input("Enter the name of the file to read: ")
        
        # Open and read the input file
        with open(input_file, 'r') as file:
            content = file.read()

        # modify the content
        modified_content = content.upper()
        
        # Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as file:
                file.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. Unable to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")