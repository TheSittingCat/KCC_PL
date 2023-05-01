# The purpose of this file is to generate the parser and the tree from the text. The parser is generated from the grammar and the tree is generated from the text.
from lark import Lark
#Grammar for the parser
def grammar() : 
    grammar = r'''
    start: fun name lp ([type] | name equals (exp | expstr) | name equals (exp | expstr) comma)* rp lb (exp | funcall)* [returnstatement] rb (start)* 
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
    returnstr: "return"
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
    %import common.WS
    %ignore WS
    expfun: (name comma name)+ equals funcall | name equals funcall | exp | expstr | expname
    expstr: STRING end | name equals STRING end | exp | expfun | expname
    exp: NUMBER | exp1 | name equals exp1 end | expstr | expfun | expname
    exp1: exp1 plus exp1 | exp1 minus exp1 | exp1 multiply exp2 | exp1 divide exp2 | exp1 modulus exp2 | exp2
    exp2: exp2 multiply exp2 | exp2 divide exp2 | exp2 modulus exp2 | exp2 power exp3 | exp3 
    exp3: exp3 power exp3 | exp | name
    expname: name equals name end | exp | expstr | expfun
    funcall: name lp (name | name equals exp | name equals expstr | exp | name comma | name equals exp comma | name equals expstr comma | exp comma | STRING | funfuncall | name equals name)* rp end
    funfuncall: name lp (name | name equals exp | name equals expstr | exp | name comma | name equals exp comma | name equals expstr comma | exp comma | STRING | funfuncall)* rp
    returnstatement: returnstr (exp | expstr | funcall | name) end
    name: /[a-zA-Z0-9_]+/
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