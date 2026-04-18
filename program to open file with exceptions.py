

def open_file():
    filename = input("Enter the file name: ")

    try:
       
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile opened successfully!")
            print("File content:\n")
            print(content)

    except FileNotFoundError:
        print("Error: The file does not exist.")

    except PermissionError:
        print("Error: You do not have permission to read this file.")


open_file()