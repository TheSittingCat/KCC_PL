from lark import Lark
grammar = r'''
start: fun name lp [type] rp lb (exp | funcall)+ rb | fun name lp [type] rp lb (expstr | funcall)+ rb | fun name lp [type] rp lb (exp | funcall)+ rb start | fun name lp [type] rp lb (expstr | funcall)+ rb start
fun: "function"
name: /.+?(?<!\\)/ name | /.+?(?<!\\)/
lp: "("
type: "int" | "str" | "float" | "shape"
rp: ")"
lb: "{"
rb: "}"
exp: NUMBER | exp1 | name "=" exp1
exp1: exp1 "+" exp1 | exp1 "-" exp1 | exp1 "*" exp2 | exp1 "/" exp2 | exp1 "%" exp2 | exp2
exp2: exp2 "*" exp2 | exp2 "/" exp2 | exp2 "%" exp2 | exp2 "^" exp3 | exp3 
exp3: exp3 "^" exp3 | exp
expstr: STRING | name "=" STRING
funcall: name lp (name | name "=" exp | name "=" expstr)* rp
%import common.ESCAPED_STRING -> STRING
%import common.SIGNED_NUMBER -> NUMBER
%import common.WS
%ignore WS

'''
def parser(grammar, starter) :
    parser = Lark(grammar, start = starter)
    return parser
def tree_generator(parser, text) : 
    tree = parser.parse(text)
    return tree

parser = parser(grammar, starter = 'start')
test = """
function kaveh(int) {
randomfunction(Hello = "shayesteh")
}
"""
tree = tree_generator(parser, test) 
print(tree.pretty())