# The purpose of this file is to read the text from the Evaluator module and generate the python file from the text.
import Evaluator
import sys
import re
def read_file(file_name):
    # The with statement is used to open a file and close it automatically after the code block is executed.
    # The file is opened in read mode.
    # Read the KCC code from the file and return it.
    with open(file_name, "r") as file:
        return file.read()
def parse_kcc_code(code) : 
    # Parse the KCC code and return the unstructured python string.
    return Evaluator.transform_result(code)
def get_arguments():
    # Get the file name from the command line arguments.
    # If the file name is not given, exit the program.
    if len(sys.argv) == 2:
        return sys.argv[1]
    else:
        print("Error: No file name given")
        exit()
def write_file(file_name, code):
    # The with statement is used to open a file and close it automatically after the code block is executed.
    # The file is opened in write mode.
    # Write the python code to the file.
    # Changes .txt to .py
    # Replace the actual new line and tab characters with the escape sequences.
    code = code.replace(r'\t', "\t")
    code = code.replace(r'\n', "\n")
    code = code.replace(r'"[', "")
    code = code.replace(r']"', "")
    code = re.sub(r"\\", "", code)
    file_name = re.sub(r"\.KCC$", ".py", file_name)
    with open(file_name, "w", encoding= "ascii") as file:
        code = code + "main()"
        file.write(code)
    return file_name, code
def py_list_to_string(py_list):
    # Convert the python list to a string.
    # The list is converted to a string by joining the elements of the list.
    py_list = [i for i in py_list if i != "None"]
    #remove quotes from strings
    #Convert double backslashes to single backslashes
    for i in range(len(py_list)):
        py_list[i] = re.sub(r"\'", "", py_list[i])
    return "".join(py_list)
def main() : 
    #Call the functions in the correct order.

    path = get_arguments()
    code = read_file(path)
    code = parse_kcc_code(code)
    code = py_list_to_string(code)
    file_name, code = write_file(path, code)
    print(code)
    print("File created: " + file_name)
main()