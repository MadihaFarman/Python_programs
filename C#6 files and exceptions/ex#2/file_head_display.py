def main():
    filename = input("Enter the name of the file: ")
    try:
        with open(filename, 'r') as file:
             lines = (file.readlines())
             #print(len(lines))
             if len(lines) < 5:
                print("The file contains less than five lines. Displaying entire contents:")
                print("".join(lines)) #combines a list of strings into a single string .'lines' is a list of strings, where each string is a line from the file."\n".join(lines) would combine the lines with newline characters in between, effectively reconstructing the original file content.
             else:                    #since each line in lines already ends with a newline character, using "".join(lines) without any delimiter will correctly display the content without adding extra newlines.
                print("Displaying the first five lines:")
                print("".join(lines[:5]))
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()