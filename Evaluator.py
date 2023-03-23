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
        return ":\t"
    def rb(self, args):
        return "\n"
    def NUMBER(self, args):
        return float(args)
    def exp(self, args):
        return str(args)
    
test = "function test (int) { 1 }"
grammar = Parser.grammar()
parser = Parser.parser(grammar, "start")
tree = Parser.tree_generator(parser, test)
print(tree)
print(Evaluator().transform(tree)[1:-1])