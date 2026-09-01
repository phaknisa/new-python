def example_w_plus_mode():
    # Example code for using the 'w+' mode in file handling
    with open('example_w+.txt', 'w+') as file:
        # Write some data to the file
        file.write("This is the first line in the file.\n")
        file.write("This is the second line in file.\n")
        # Move the cursor to the beginning of the file
        file.seek(0)

        # Read the data back from the file
        content = file.read()
        print("Content of the file:")
        print(content)

example_w_plus_mode()