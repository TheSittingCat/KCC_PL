# The purpose of this file is to read the text from the Evaluator module and generate the python file from the text.
import Evaluator
def read_file(file_name):
    # The with statement is used to open a file and close it automatically after the code block is executed.
    # The file is opened in read mode.
    # Read the KCC code from the file and return it.
    with open(file_name, "r") as file:
        return file.read()
def parse_kcc_code(code) : 
    # Parse the KCC code and return the unstructured python string.
    return Evaluator.transform_result(code)
code = read_file("C:/Users/keskandarimiandoab/Desktop/test.txt")