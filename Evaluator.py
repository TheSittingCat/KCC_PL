from lark import Transformer
import Parser
# Transformer is a class that can be used to evaluate the tree
class Evaluator(Transformer):
    # The following methods are called when the corresponding rule is found
    def start(self, args):
        return str(args)
    def fun(self, args):
        return "def"
    def name(self, args):
        arg_list = []
        for arg in args:
            arg_list.append(str(arg))
        args = "".join(arg_list)
        return args
    def lp(self, args):
        return "("
    def rp (self, args):
        return ")"
    def int_rule(self, args):
        return "int"
    def str_rule(self, args):
        return "str"
    def float_rule(self, args):
        return "float"
    def shape_rule(self, args):
        return "shape"
    def lb(self, args):
        return ": \n \t"
    def rb(self, args):
        return "\n"
    def NUMBER(self, args):
        return float(args)
    # Expression paths, the order of the methods is important. Returns the number of expression is a number, recursively calls the next expression if it is not a number.
    def exp(self, args):
        if len(args) == 1:
            return args[0]
        else :
            arg_list = []
            for arg in args:
                arg_list.append(str(arg))
            args = " ".join(arg_list)
            return args
    def exp1(self, args):
        if len(args) == 1:
            return args[0]
        else :
            arg_list = []
            for arg in args:
                arg_list.append(str(arg))
            args = " ".join(arg_list)
            return args
    def exp2(self, args):
        if len(args) == 1:
            return args[0]
        else :
            arg_list = []
            for arg in args:
                arg_list.append(str(arg))
            args = " ".join(arg_list)
            return args
    def exp3(self, args):
        if len(args) == 1:
            return args[0]
        else :
            arg_list = []
            for arg in args:
                arg_list.append(str(arg))
            args = " ".join(arg_list)
            return args
    def equals(self, args):
        return "="
    def plus(self, args):
        return "+"
    def minus(self, args):  
        return "-"
    def multiply(self, args):
        return "*"
    def divide(self, args):
        return "/"
    def modulus(self, args):
        return "%"
    def power(self, args):
        return "**"
    def STRING(self, args):
        return str(args)
    def expstr(self, args):
        if len(args) == 1:
            return args[0]
        else :
            arg_list = []
            for arg in args:
                arg_list.append(str(arg))
            args = " ".join(arg_list)
            return args
    def end(self, args):
        return ";"
test = r'''function test (int) {
Hello = "Hello World";
Christina = 5;
Camille = 6;
 }'''

def transform_result(entry):
    grammar = Parser.grammar()
    parser = Parser.parser(grammar, "start")
    tree = Parser.tree_generator(parser, entry)
    print(tree.pretty())
    return Evaluator().transform(tree)[1:-1]
transform_result(test)