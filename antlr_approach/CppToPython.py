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

# sys.path.append("/compilation_theory/antlr_approach/dist/")

from antlr4 import *

from dist.FileErrorListener import FileErrorListener
from dist.HelloLexer import HelloLexer
from dist.HelloListener import HelloListener
from dist.HelloParser import HelloParser






def from_file(path, out_path="out.py"):
    input = FileStream(path)
    lexer = HelloLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.program()

    printer = HelloListener(out_path)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    return printer.output


class CppToPython:
    output_string = ""

    def from_string(self, input_string: str, out_path="out.py"):
        lexer = HelloLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = HelloParser(stream)
        parser.addErrorListener(FileErrorListener())
        tree = parser.program()

        printer = HelloListener(out_path)
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        return printer.output

    def from_file(self, path, out_path="out.py"):
        input = FileStream(path)
        lexer = HelloLexer(input)
        stream = CommonTokenStream(lexer)
        parser = HelloParser(stream)
        parser.addErrorListener(FileErrorListener())
        tree = parser.program()

        printer = HelloListener(out_path=out_path)
        walker = ParseTreeWalker()
        walker.walk(printer, tree)


# def from_string(input_string: str):
#     lexer = HelloLexer(InputStream(input_string))
#     stream = CommonTokenStream(lexer)
#     parser = HelloParser(stream)
#     parser.addErrorListener(FileErrorListener())
#
#     tree = parser.program()
#
#     printer = HelloListener("a.py")
#     walker = ParseTreeWalker()
#     walker.walk(printer, tree)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == '-f':
        path = sys.argv[2]
        out = path.removesuffix(".txt") + ".py"
        translator = CppToPython()
        translator.from_file(path, out)
    if len(sys.argv) == 5 and sys.argv[1] == '-f' and sys.argv[3] == '-d':
        translator = CppToPython()
        translator.from_file(sys.argv[2], sys.argv[4])


if __name__ == '__main__':
    main()
