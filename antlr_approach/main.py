# import sys
# from antlr4 import *
# from dist.HelloLexer import HelloLexer
# from dist.HelloParser import HelloParser
# from dist.HelloVisitor import HelloVisitor
#
#
# def get_username():
#     from pwd import getpwuid
#     from os import getuid
#
#     return getpwuid(getuid())[0]
#
#
# class MyVisitor(HelloVisitor):
#     def visitNumberExpr(self, ctx):
#         value = ctx.getText()
#         return int(value)
#
#     def visitParenExpr(self, ctx):
#         return self.visit(ctx.expr())
#
#     def visitInfixExpr(self, ctx):
#         l = self.visit(ctx.left)
#         r = self.visit(ctx.right)
#
#         op = ctx.op.text
#         operation = {
#             "+": lambda: l + r,
#             "-": lambda: l - r,
#             "*": lambda: l * r,
#             "/": lambda: l / r,
#         }
#         return operation.get(op, lambda: None)()
#
#     def visitByeExpr(self, ctx):
#         print("goodbye {0}".format(get_username()))
#         sys.exit(0)
#
#     def visitHelloExpr(self, ctx):
#         return "{0} {1}".format(ctx.getText(), get_username())
#
#
# if __name__ == "__main__":
#     while 1:
#         data = InputStream(input(">>> "))
#         # lexer
#         lexer = MyGrammerLexer(data)
#         stream = CommonTokenStream(lexer)
#         # parser
#         parser = MyGrammerParser(stream)
#         tree = parser.expr()
#         # evaluator
#         visitor = MyVisitor()
#         output = visitor.visit(tree)
#         print(output)

import sys
from antlr4 import *
# from Python3Lexer import Python3Lexer
# from Python3Parser import Python3Parser
# from Python3Listener import Python3Listener
from dist.HelloListener import HelloListener
from dist.HelloLexer import HelloLexer
from dist.HelloParser import HelloParser


class FuncPrinter(HelloListener):
    def enterFuncdef(self, ctx):
        print("Oh, a func")


def main():
    contents = 'cpp_code_sample.txt'
    input = FileStream(contents)
    lexer = HelloLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    # tree = parser.funcdef()
    tree = parser.program()

    printer = HelloListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()
