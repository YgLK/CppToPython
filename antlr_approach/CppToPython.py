import sys

from antlr4 import *

from dist_tmp.FileErrorListener import FileErrorListener
from dist_tmp.HelloLexer import HelloLexer
from dist_tmp.HelloListener import HelloListener
from dist_tmp.HelloParser import HelloParser


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

