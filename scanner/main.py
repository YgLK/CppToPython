# TOKENS
TOK_INT = "TOK_INT"
TOK_PLUS = "TOK_PLUS"
TOK_MINUS = "TOK_MINUS"
# multiplication token  '*'
TOK_MUL = "TOK_MUL"
# division token  '/'
TOK_DIV = "TOK_DIV"
# parentheses tokens
TOK_RPARENTH = "TOK_RPARENTH"
TOK_LPARENTH = "TOK_LPARENTH"
# end of file
TOK_EOF = "TOK_EOF"

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
                else:
                    break
            # set current position to the position of last read number
            curr_pos = curr_pos - 1
            tokens_list.append(Token(TOK_INT, number))
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
        else:
            raise ValueError("Incorrect character " + "\"" + str(curr_char) + "\"" + " at the index " + str(curr_pos))


if __name__ == '__main__':
    filepath = "data/to_scan.txt"
    tokens = scanner(filepath)
    for token in tokens:
        print(token)