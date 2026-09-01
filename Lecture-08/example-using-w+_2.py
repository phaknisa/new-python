def example_w_plus_mode():
    # Example code for using the 'w+' mode in file handling
    with open('example_w+.txt', 'a+') as file:
        file.seek(0)

        content = file.read()
        print("Current content of the file:")
        print(content)

        file.write("Appending a new line at the end\n")

        file.seek(0)
        updated_content = file.read()
        print("\nUpdated content of the file:")
        print(updated_content)

example_w_plus_mode()