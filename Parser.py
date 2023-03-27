from lark import Lark
#Grammar for the parser
def grammar() : 
    grammar = r'''
    start: fun name lp ([type] | name "=" (exp | expstr))* rp lb (exp | funcall)+ rb | fun name lp [type] rp lb (expstr | funcall)+ rb | fun name lp [type] rp lb (exp | funcall)+ rb start | fun name lp [type] rp lb (expstr | funcall)+ rb start
    fun: "function"
    name: (/.+?(?<!\\)/)*
    lp: "("
    ?type: int_rule | str_rule | float_rule | shape_rule
    int_rule: "int"
    str_rule: "str"
    float_rule: "float"
    shape_rule: "shape"
    rp: ")"
    lb: "{"
    rb: "}"
    exp: NUMBER | exp1 | name equals exp1 end
    exp1: exp1 plus exp1 | exp1 minus exp1 | exp1 multiply exp2 | exp1 divide exp2 | exp1 modulus exp2 | exp2
    exp2: exp2 multiply exp2 | exp2 divide exp2 | exp2 modulus exp2 | exp2 power exp3 | exp3 
    exp3: exp3 power exp3 | exp
    expstr: STRING | name equals STRING
    equals: "="
    plus: "+"
    minus: "-"
    multiply: "*"
    divide: "/"
    modulus: "%"
    power: "^"
    end: ";"
    funcall: name lp (name | name "=" exp | name "=" expstr)* rp
    %import common.ESCAPED_STRING -> STRING
    %import common.SIGNED_NUMBER -> NUMBER
    %import common.WS
    %ignore WS

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