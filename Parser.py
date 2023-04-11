# The purpose of this file is to generate the parser and the tree from the text. The parser is generated from the grammar and the tree is generated from the text.
from lark import Lark
#Grammar for the parser
def grammar() : 
    grammar = r'''
    start: fun name lp ([type] | name equals (exp | expstr))* rp lb (exp | funcall)+ return (exp | expstr)? rb (start)* | fun name lp [type] rp lb (expstr | funcall)+ return (exp | expstr)? rb (start)*
    fun: "function"
    lp: "("
    type: int_rule | str_rule | float_rule | shape_rule
    int_rule: "int"
    str_rule: "str"
    float_rule: "float"
    shape_rule: "shape"
    rp: ")"
    lb: "{"
    rb: "}"
    return: "return"
    equals: "="
    plus: "+"
    minus: "-"
    multiply: "*"
    divide: "/"
    modulus: "%"
    power: "^"
    end: ";"
    comma: ","
    %import common.ESCAPED_STRING -> STRING
    %import common.SIGNED_NUMBER -> NUMBER
    name: /[a-zA-Z0-9]+/
    %import common.WS
    %ignore WS
    return: returnstr (exp | name | NUMBER)
    expstr: STRING | name equals STRING end | exp
    exp: NUMBER | exp1 | name equals exp1 end | expstr
    exp1: exp1 plus exp1 | exp1 minus exp1 | exp1 multiply exp2 | exp1 divide exp2 | exp1 modulus exp2 | exp2
    exp2: exp2 multiply exp2 | exp2 divide exp2 | exp2 modulus exp2 | exp2 power exp3 | exp3 
    exp3: exp3 power exp3 | exp
    funcall: name lp (name | name equals exp | name equals expstr | exp | name comma | name equals exp comma | name equals expstr comma | exp comma)* rp end
    '''
    return grammar
def parser(grammar, starter) :
    #Generates the parser from the grammar
    parser = Lark(grammar, start = starter)
    return parser
def tree_generator(parser, text) : 
    #Generates the tree from the text
    tree = parser.parse(text)
    return tree
def tree_printer(tree) :
    #Outputs the tree in the pretty format
    print(tree.pretty())