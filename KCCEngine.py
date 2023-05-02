# The purpose of this file is to read the text from the Evaluator module and generate the python file from the text.
import Evaluator
import sys
import re
import os
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
    code_new = code.replace(r'"[', "")
    code_new = code_new.replace(r']"', "")
    if code_new == code:
        code = code.replace(r'[',"", 1)
        code = code.replace(r']',"", 1)
        del code_new
    else:
        code = code_new
        del code_new
    sumnum = sum(1 for _ in re.finditer(r'\b%s\b'% re.escape('def'), code))
    if sumnum > 2: 
        # sumnum - 2 because we already remove the initial brackets. For 3 functions, we do a single deletion. For 4 functions, we do 2 deletions and so on.
        for i in range(sumnum - 2) : 
            code = code.replace(r'[',"", 1)
            code = code.replace(r']',"", 1)
    code = re.sub(r"\\", "", code)
    file_name = re.sub(r"\.KCC$", ".py", file_name)
    current_folder_path = os.path.abspath(os.getcwd())
    file_name = current_folder_path + "\\" + file_name
    with open(file_name, "w", encoding= "ascii") as file:
        code = 'from Graph_Equations import * \n' + code + "main()"
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
def isolate_python_code(code):
    # Isolate the python code from the KCC code.
    # The python code is surrounded by the following tags:
    # <python>
    # </python>
    # The python code is extracted using regular expressions.
    # The regular expression is compiled.
    # The regular expression is used to find the python code.
    # The python code is returned and the KCC code is modified to remove the python code.
    # Returns the python code and the modified KCC code, as well as the index of the python code.
    # The index is used to insert the python code back into the KCC code.
    regex = re.compile(r"<python>(.*)</python>", re.DOTALL)
    python_code = regex.findall(code)
    #add tabs to the start of each code.
    import copy
    new_python_code = copy.deepcopy(python_code)
    for i in range(len(new_python_code)):
        new_python_code[i] = new_python_code[i].replace("\n","", 1)
        new_python_code[i] = new_python_code[i].replace("\t", "\t \t")
        new_python_code[i] = new_python_code[i].replace('   ', "\t \t")
        new_python_code[i] = new_python_code[i][:-1]
        new_python_code[i] = new_python_code[i] + "\n \t"
    # Replace the python code with the new python code.
        code = re.sub(python_code[i], new_python_code[i], code)
    # Find the indexes of the python code.
    matches = re.finditer(regex, code)
    indexes = [m.start() for m in matches] # There is a bug here. The indexes are not correct as the number of characters change. TODO: Replace with list version.
    # Remove the python code from the KCC code.
    code = regex.sub("", code)
    return new_python_code, code, indexes
def add_back_python_code(code, python_code, indexes):
    # Add the python code back into the compiled python code.
    # Use indexes to insert the python code back into the KCC code.
    for i in range(len(indexes)):
        code = code[:indexes[i]+ 1] + "\n \t" + python_code[i] + code[indexes[i] + 1:]
    return code
def run_python_code(path) : 
    # Run a python file.
    # The python file is run using the subprocess module.
    # The python file is run in the same directory as the project.
    import subprocess
    file_name = os.path.basename(path)
    subprocess.call(["python", file_name], shell=True)
def delete_python_file(path) :
    # Delete the python file.
    # The python file is deleted using the os module.
    # The python file is deleted in the same directory as the project.
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")
def main() : 
    #Call the functions in the correct order.
    import time
    start_time = time.time()
    path = get_arguments()
    file_name = os.path.basename(path)
    code = read_file(path)
    python_code, code, indexes = isolate_python_code(code)
    code = parse_kcc_code(code)
    code = py_list_to_string(code)
    code = add_back_python_code(code, python_code, indexes)
    file_name, code = write_file(file_name, code)
    run_python_code(file_name)
    delete_python_file(file_name)
    print("--- %s seconds ---" % (time.time() - start_time))
main()