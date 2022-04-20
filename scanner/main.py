# TOKENS
TOK_INT = "TOK_INT"
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
# character
TOK_CHAR = "TOK_CHAR"
# {
TOK_LBRACE = "TOK_LBRACE"
# }
TOK_RBRACE = "TOK_RBRACE"
# ;
TOK_SEMICOLON = "TOK_SEMICOLON"

# ------- KEYWORDS -------
# while
# for
# if
# else
# cin
# cout
# main
# using
# namespace
# break
# class
# continue
# delete
# void


# ACCESS MODIFIERS
# private
# protected
# public


# DATA TYPES
# int
# double
# float
# string
# char
# long


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
        return '({0}: {1})'.format(self.code, self.value)


def scanner(filepath):
    # open .txt file
    with open(filepath) as file:
        lines = file.read().rstrip()
    # list containing tokens
    tokens_list = []
    # current position
    curr_pos = -1
    # current read character
    curr_char = ""
    while True:
        # move further
        curr_pos += 1

        # assign None to current character when EOF is met
        if len(lines) == curr_pos:
            tokens_list.append(Token(TOK_EOF, "EOF"))
            return tokens_list
        else:
            curr_char = lines[curr_pos]

        # omit whitespaces
        if curr_char in " \t\n":
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
                    tokens_list.append("ERROR", f"Invalid token at the position: {curr_pos}")
                    return
                # set current position to the position of last read number
                else:
                    tokens_list.append(Token(TOK_INT, number))
                    break
        # read token starting with
        elif curr_char in "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper():
            characters = curr_char
            curr_pos += 1
            while True:
                if len(lines) == curr_pos:
                    # add character token
                    tokens_list.append(Token(TOK_CHAR, characters))
                    # add end of file token
                    tokens_list.append(Token(TOK_EOF, "EOF"))
                    return tokens_list
                elif lines[curr_pos] in "0123456789" or lines[curr_pos].lower() in "abcdefghijklmnopqrstuvwxyz":
                    characters += lines[curr_pos]
                    # move the cursor
                    curr_pos += 1
                # set current position to the position of last read number
                else:
                    tokens_list.append(Token(TOK_VAR, characters))
                    break
        elif curr_char == "\"":
            tokens_list.append(Token(TOK_QUOTE, curr_char))
        elif curr_char == ";":
            tokens_list.append(Token(TOK_SEMICOLON, curr_char))
        elif curr_char == "{":
            tokens_list.append(Token(TOK_LBRACE, curr_char))
        elif curr_char == "}":
            tokens_list.append(Token(TOK_RBRACE, curr_char))
        elif curr_char == "[":
            tokens_list.append(Token(TOK_LSQUARE, curr_char))
        elif curr_char == "]":
            tokens_list.append(Token(TOK_RSQUARE, curr_char))
        elif curr_char == ">":
            tokens_list.append(Token(TOK_GTHAN, curr_char))
        elif curr_char == "<":
            tokens_list.append(Token(TOK_LTHAN, curr_char))
        elif curr_char == "+":
            tokens_list.append(Token(TOK_PLUS, curr_char))
        elif curr_char == "+":
            tokens_list.append(Token(TOK_PLUS, curr_char))
        elif curr_char == "-":
            tokens_list.append(Token(TOK_MINUS, curr_char))
        elif curr_char == "*":
            tokens_list.append(Token(TOK_MUL, curr_char))
        elif curr_char == "/":
            tokens_list.append(Token(TOK_DIV, curr_char))
        elif curr_char == "(":
            tokens_list.append(Token(TOK_LPARENTH, curr_char))
        elif curr_char == ")":
            tokens_list.append(Token(TOK_RPARENTH, curr_char))
        elif curr_char == "\\":
            tokens_list.append(Token(TOK_RPARENTH, curr_char))
        else:
            raise ValueError("Incorrect character " + "\"" + str(curr_char) + "\"" + " at the index " + str(curr_pos))



if __name__ == '__main__':
    filepath = "data/cpp_code.txt"
    tokens = scanner(filepath)
    for token in tokens:
        print(token)