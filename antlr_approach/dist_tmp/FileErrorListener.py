from antlr4.error.ErrorListener import ErrorListener


class FileErrorListener(ErrorListener):
    __path = "dist_tmp/diag.txt"
    __errors = ""

    def __init__(self):
        super().__init__()
        open(self.__path, 'w').close()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.__errors += "line " + str(line) + ":" + str(column) + " " + msg + "\n"
        self.write()


    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        # self.__errors += "reportAmbiguity " + str(ambigAlts) + ":" + str(
        #     configs) + ", input=" + self.parser.getTokenStream().getText(interval)
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        # self.__errors += "reportAttemptingFullContext decision=" + str(dfa.decision) + ":" + str(
        #     configs) + ", input=" + self.parser.getTokenStream().getText(interval)
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        # self.__error += "reportContextSensitivity decision=" + str(dfa.decision) + ":" + str(
        #     configs) + ", input=" + self.parser.getTokenStream().getText(interval)
        pass

    def write(self):
        with open(self.__path, 'w') as file:
            file.writelines(self.__errors)