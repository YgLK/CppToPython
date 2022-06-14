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
import io
import sys

import antlr4.tree.Tree
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


def from_file(path, out_path="out.py"):
    input = FileStream(path)
    lexer = HelloLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.program()

    printer = HelloListener(out_path=out_path)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


def from_string(input_string: str):
    lexer = HelloLexer(InputStream(input_string))
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.program()

    printer = HelloListener("a.py")
    walker = ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '-f':
        out = sys.argv[2].removesuffix(".txt") + ".py"
        from_file(sys.argv[2], out)
    if len(sys.argv) == 5 and sys.argv[1] == '-f' and sys.argv[3] == '-d':
        from_file(sys.argv[2], sys.argv[4])

    # from_file("cpp_code_sample.txt", )
