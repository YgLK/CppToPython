# TOKENS
TOK_INT = "TOK_INT"
# separate letter
TOK_CHAR = "TOK_CHAR"
TOK_PLUS = "TOK_PLUS"
TOK_MINUS = "TOK_MINUS"
# multiplication  '*'
TOK_MUL = "TOK_MUL"
# division token  '/'
TOK_DIV = "TOK_DIV"
# escape token '\'
TOK_ESC = "TOK_ESC"
# (
TOK_RPARENTH = "TOK_RPARENTH"
# )
TOK_LPARENTH = "TOK_LPARENTH"
# [ - left square bracket
TOK_LSQUARE = "TOK_LSQUARE"
# ] - right square bracket
TOK_RSQUARE = "TOK_RSQUARE"
# end of file
TOK_EOF = "TOK_EOF"
# "
TOK_QUOTE = "TOK_QUOTE"
# >
TOK_GTHAN = "TOK_GTHAN"
# <
TOK_LTHAN = "TOK_LTHAN"
# variable name token (it's not in keywords list)
# e.g. a, b, int_variable etc.
TOK_VAR = "TOK_VAR"
# {
TOK_LBRACE = "TOK_LBRACE"
# }
TOK_RBRACE = "TOK_RBRACE"
# ;
TOK_SEMICOLON = "TOK_SEMICOLON"

# ------- KEYWORDS -------
# while
TOK_WHILE = "TOK_WHILE"
# for
TOK_FOR = "TOK_FOR"
# if
TOK_IF = "TOK_IF"
# else
TOK_ELSE = "TOK_ELSE"
# cin
TOK_CIN = "TOK_CIN"
# cout
TOK_COUT = "TOK_COUT"
# main
TOK_MAIN = "TOK_MAIN"
# using
TOK_USING = "TOK_USING"
# namespace
TOK_NAMESPACE = "TOK_NAMESPACE"
# return
TOK_RETURN = "TOK_RETURN"
# break
TOK_BREAK = "TOK_BREAK"
# class
TOK_CLASS = "TOK_CLASS"
# continue
TOK_CONTINUE = "TOK_CONTINUE"
# delete
TOK_DELETE = "TOK_DELETE"
# void
TOK_VOID = "TOK_VOID"
# endl
TOK_ENDL = "TOK_ENDL"


# ACCESS MODIFIERS
# private
TOK_PRIVATE = "TOK_PRIVATE"
# protected
TOK_PROTECTED = "TOK_PROTECTED"
# public
TOK_PUBLIC = "TOK_PUBLIC"


# DATA TYPES
# int
TOK_INTEGER = "TOK_INTEGER"
# double
TOK_DOUBLE = "TOK_DOUBLE"
# float
TOK_FLOAT = "TOK_FLOAT"
# string
TOK_STRING = "TOK_STRING"
# char
TOK_CHARACTER = "TOK_CHARACTER"
# long
TOK_LONG = "TOK_LONG"


# TODO:
# - przesunięcia są niepoprawnie przez co niektóre tokeny są omijane
# - ++ -- << >> etc. recognition
# - html colouring (idk czy trzeba - jak będą tokeny to już w sumie dużo roboty nie ma tbh)
# - omit characters between two quotes as it can be custom string etc. a = "124s asdac czx e124135"


class Token:
    def __init__(self, code_, value_):
        self.code = code_
        self.value = value_

    def __str__(self):
        return "({0}: {1})".format(self.code, self.value)


def scanner(filepath):
    # open .txt file
    with open(filepath) as file:
        lines = file.read().rstrip()
    # list containing tokens
    tokens_list = []
    # current position
    curr_pos = 0
    # current read character
    curr_char = ""
    while True:
        # move further
        # curr_pos += 1

        # assign None to current character when EOF is met
        if len(lines) == curr_pos:
            tokens_list.append(Token(TOK_EOF, "EOF"))
            return tokens_list
        else:
            curr_char = lines[curr_pos]
        # omit whitespaces
        if curr_char in " \t\n":
            curr_pos += 1
            continue

        # create instance of the appropriate token
        if curr_char in "0123456789":
            # check if number has more than 1 digit
            number = curr_char
            curr_pos += 1
            # read multi digit number
            while True:
                if len(lines) == curr_pos:
                    # add number token
                    tokens_list.append(Token(TOK_INT, number))
                    # add end of file token
                    tokens_list.append(Token(TOK_EOF, "EOF"))
                    return tokens_list
                elif lines[curr_pos] in "0123456789":
                    number += lines[curr_pos]
                    # move the cursor
                    curr_pos += 1
                elif lines[curr_pos].lower() in "abcdefghijklmnopqrstuvwxyz":
                    # letters cannot occur after digits
                    tokens_list.append(
                        "ERROR", f"Invalid token at the position: {curr_pos}"
                    )
                    return
                # set current position to the position of last read number
                else:
                    tokens_list.append(Token(TOK_INT, number))
                    break
        # read token starting with
        elif (
            curr_char
            in "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
        ):
            characters = curr_char
            curr_pos += 1
            while True:
                if len(lines) == curr_pos:
                    # add character token
                    tokens_list.append(Token(TOK_CHAR, characters))
                    # add end of file token
                    tokens_list.append(Token(TOK_EOF, "EOF"))
                    return tokens_list
                elif (
                    lines[curr_pos] in "0123456789"
                    or lines[curr_pos].lower() in "abcdefghijklmnopqrstuvwxyz"
                ):
                    characters += lines[curr_pos]
                    # move the cursor
                    curr_pos += 1
                # set current position to the position of last read number
                else:
                    token = keyword_detect(characters)
                    tokens_list.append(Token(token, characters))
                    break
        elif curr_char == '"':
            tokens_list.append(Token(TOK_QUOTE, curr_char))
            curr_pos += 1
        elif curr_char == ";":
            tokens_list.append(Token(TOK_SEMICOLON, curr_char))
            curr_pos += 1
        elif curr_char == "{":
            tokens_list.append(Token(TOK_LBRACE, curr_char))
            curr_pos += 1
        elif curr_char == "}":
            tokens_list.append(Token(TOK_RBRACE, curr_char))
            curr_pos += 1
        elif curr_char == "[":
            tokens_list.append(Token(TOK_LSQUARE, curr_char))
            curr_pos += 1
        elif curr_char == "]":
            tokens_list.append(Token(TOK_RSQUARE, curr_char))
            curr_pos += 1
        elif curr_char == ">":
            tokens_list.append(Token(TOK_GTHAN, curr_char))
            curr_pos += 1
        elif curr_char == "<":
            tokens_list.append(Token(TOK_LTHAN, curr_char))
            curr_pos += 1
        elif curr_char == "+":
            tokens_list.append(Token(TOK_PLUS, curr_char))
            curr_pos += 1
        elif curr_char == "+":
            tokens_list.append(Token(TOK_PLUS, curr_char))
            curr_pos += 1
        elif curr_char == "-":
            tokens_list.append(Token(TOK_MINUS, curr_char))
            curr_pos += 1
        elif curr_char == "*":
            tokens_list.append(Token(TOK_MUL, curr_char))
            curr_pos += 1
        elif curr_char == "/":
            tokens_list.append(Token(TOK_DIV, curr_char))
            curr_pos += 1
        elif curr_char == "(":
            tokens_list.append(Token(TOK_LPARENTH, curr_char))
            curr_pos += 1
        elif curr_char == ")":
            tokens_list.append(Token(TOK_RPARENTH, curr_char))
            curr_pos += 1
        elif curr_char == "\\":
            tokens_list.append(Token(TOK_RPARENTH, curr_char))
            curr_pos += 1
        else:
            raise ValueError(
                "Incorrect character "
                + '"'
                + str(curr_char)
                + '"'
                + " at the index "
                + str(curr_pos)
            )


def keyword_detect(word):
    if word == "while":
        return TOK_WHILE
    elif word == "for":
        return TOK_FOR
    elif word == "if":
        return TOK_IF
    elif word == "else":
        return TOK_ELSE
    elif word == "cin":
        return TOK_CIN
    elif word == "cout":
        return TOK_COUT
    elif word == "main":
        return TOK_MAIN
    elif word == "using":
        return TOK_USING
    elif word == "namespace":
        return TOK_NAMESPACE
    elif word == "return":
        return TOK_RETURN
    elif word == "break":
        return TOK_BREAK
    elif word == "class":
        return TOK_CONTINUE
    elif word == "continue":
        return TOK_CONTINUE
    elif word == "delete":
        return TOK_DELETE
    elif word == "void":
        return TOK_VOID
    elif word == "private":
        return TOK_PRIVATE
    elif word == "protected":
        return TOK_PROTECTED
    elif word == "public":
        return TOK_PUBLIC
    elif word == "int":
        return TOK_INTEGER
    elif word == "char":
        return TOK_CHARACTER
    elif word == "str":
        return TOK_STRING
    elif word == "long":
        return TOK_LONG
    elif word == "endl":
        return TOK_ENDL
    # if no keyword is detected return variable token
    else:
        return TOK_VAR


if __name__ == "__main__":
    filepath = "data/cpp_code.txt"
    tokens = scanner(filepath)
    for token in tokens:
        print(token)
