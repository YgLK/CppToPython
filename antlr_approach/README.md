<h1 align="center">  Kompilator C++ do Pythona </h1>

## Spis treści

- [Informacje o projekcie](#doc_scube)
- [Spis tokenów](#description)
- [Gramatyka](#instructions)
- [Instrukcja uruchomienia projektu](#servermsg)

    1. [Graficzny interfejs użytkownika](#gui)

    2. [Terminal](#cl)
- [Testy](#tests)
    1. [Prawidłowy kod](#pk)

    2. [Nieprawidłowy kod](#nk)

## Informacje o projekcie <a name="doc_scube"></a>

Autorzy: <br>

* Jakub Szpunar `jszpunar@student.agh.edu.pl`
* Bartosz Fudali `bfudali@student.agh.edu.pl`

Główne cele i założenia projektu: <br>

* Translacja kodu z C++ do Pythona
* Możliwość uruchamiania kodu w Pythonie

Język implementacji: Python <br>
Generator parserów: ANTLR4

## Spis tokenów <a name="description"></a>

```java
WS: [ \t\r\n]+     // znaki białe

PLUS: '+';
MINUS: '-';
DPLUS: '++';
DMINUS: '--';
MUL: '*';
DIV: '/';
MOD: '%';

ESC: '\';
RPARENTH: ')';
LPARENTH: '(';
LSQUARE: '[';
RSQUARE: ']';
LBRACE: '{';
RBRACE: '}';
COLON: ':';
SEMICOLON: ';';
COMMA: ',';
DOT: '.';

GTHAN: '>';
LTHAN: '<';
EQUAL: '=';
DEQUAL: '==';
GREATER_EQUAL: '>=';
LESS_EQUAL: '<=';
NOT_EQUAL: '!=';
LBIT: '<<';
RBIT: '>>';

INT: 'int';
FLOAT: 'float';
CHAR: 'char';
STRING: 'string';
BOOL: 'bool';
VOID: 'void';
WHILE: 'while';
FOR: 'for';
IF: 'if';
ELSE: 'else';
TRUE: 'true';
FALSE: 'false';

CIN: 'cin';
COUT: 'cout';
MAIN: 'main';
USING: 'using';
NAMESPACE: 'namespace';
STD: 'std';
INCLUDE: 'include';
HASH: '#';
RETURN: 'return';
BREAK: 'break';

CONTINUE: 'continue';
DELETE: 'delete';
ENDL: 'endl';

CLASS: 'class';
PUBLIC: 'public';
PRIVATE: 'private';
PROTECTED: 'protected';

FLOATVAR: [0-9]* '.' [0-9]+;
INTVAR: '-'? [0-9]+;

VARNAME: [a-zA-Z_][a-zA-Z0-9_]*;

STRINGVAR: '"' .*? '"';

COMMENTVAR: DIV DIV VARNAME '\n';
```

## Gramatyka  <a name="instructions"></a>

```antlr
program:
	include using_namespace_std block
	| using_namespace_std block;

block: block_part main_func | main_func;

block_part:
	block_part block_part
	| variable_def
	| function
	| class_object;

main_func:
	return_type MAIN LPARENTH RPARENTH LBRACE func_block RBRACE
	| return_type MAIN LPARENTH RPARENTH LBRACE RBRACE;

using_namespace_std: USING NAMESPACE STD SEMICOLON;

class_object:
	CLASS VARNAME LBRACE class_variable class_functions RBRACE SEMICOLON
	| CLASS VARNAME LBRACE class_functions RBRACE SEMICOLON
	| CLASS VARNAME LBRACE class_variable RBRACE SEMICOLON;

class_variable:
	access_modifier COLON variable_def
	| variable_def
	| assign_var
	| class_variable class_variable;

class_functions:
	access_modifier COLON function
	| function
	| class_functions class_functions;

function:
	return_type VARNAME LPARENTH parameters RPARENTH LBRACE func_block RBRACE
	| return_type VARNAME LPARENTH RPARENTH LBRACE func_block RBRACE;

parameters:
	data_type VARNAME
	| data_type VARNAME COMMA parameters;

access_modifier: PUBLIC | PRIVATE | PROTECTED;

statement:
	func_call
	| variable_def
	| if_statement
	| while_statement
	| for_statement
	| print_out
	| cin_in
	| VARNAME EQUAL calculation SEMICOLON
	| assign_var
	| statement statement;

assign_var:
    VARNAME EQUAL VARNAME PLUS VARNAME SEMICOLON
    | VARNAME EQUAL VARNAME PLUS var_value SEMICOLON
    | VARNAME EQUAL var_value PLUS VARNAME SEMICOLON
	| VARNAME EQUAL var_value SEMICOLON
	| VARNAME EQUAL calculation SEMICOLON
	| VARNAME EQUAL VARNAME SEMICOLON;

for_statement:
	FOR LPARENTH INT VARNAME EQUAL INTVAR SEMICOLON VARNAME comparator INTVAR SEMICOLON VARNAME
		math_operator EQUAL INTVAR RPARENTH LBRACE func_block RBRACE
	|FOR LPARENTH INT VARNAME EQUAL INTVAR SEMICOLON VARNAME comparator VARNAME SEMICOLON VARNAME
		math_operator EQUAL INTVAR RPARENTH LBRACE func_block RBRACE
	|FOR LPARENTH VARNAME EQUAL INTVAR SEMICOLON VARNAME comparator VARNAME SEMICOLON VARNAME
		math_operator EQUAL INTVAR RPARENTH LBRACE func_block RBRACE
	| FOR LPARENTH SEMICOLON SEMICOLON RPARENTH LBRACE func_block RBRACE;

while_statement:
	WHILE LPARENTH condition RPARENTH LBRACE func_block RBRACE;

if_statement:
	IF LPARENTH condition RPARENTH LBRACE func_block RBRACE else_block
	| IF LPARENTH condition RPARENTH LBRACE func_block RBRACE;

else_block: ELSE LBRACE func_block RBRACE;

func_block:
	statement
	| statement return_statement
	| return_statement;

return_statement:
	RETURN var_value SEMICOLON
	| RETURN VARNAME SEMICOLON
	| RETURN SEMICOLON;

condition:
	var_value comparator var_value
	| VARNAME comparator VARNAME
	| VARNAME comparator var_value
	| var_value comparator VARNAME;

variable_def: declare_var | declare_assign_var;

declare_var: data_type VARNAME SEMICOLON;

declare_assign_var:
    data_type VARNAME EQUAL VARNAME math_operator VARNAME SEMICOLON
	|data_type VARNAME EQUAL var_value SEMICOLON
	| data_type VARNAME EQUAL calculation SEMICOLON;

print_out: COUT cout_expression_string SEMICOLON;

cout_expression_string:
	cout_expression cout_expression_string
	| cout_expression;

func_call:
    VARNAME LPARENTH func_call_parameters RPARENTH SEMICOLON
    | VARNAME LPARENTH RPARENTH SEMICOLON;

func_call_parameters:
    VARNAME COMMA func_call_parameters
    | VARNAME;

cout_expression: LBIT printable;

printable: var_value | VARNAME | ENDL | STRINGVAR;

calculation: number math_operator number;

include: HASH INCLUDE LTHAN VARNAME GTHAN;

cin_in: CIN RBIT VARNAME SEMICOLON;

number: INTVAR | FLOATVAR;

return_type: data_type | VOID;

data_type: INT | FLOAT | CHAR | STRING | BOOL;

math_operator: PLUS | MINUS | MUL | DIV | MOD;

comparator:
	GTHAN
	| LTHAN
	| LESS_EQUAL
	| DEQUAL
	| GREATER_EQUAL
	| NOT_EQUAL;

var_value: INTVAR | FLOATVAR | STRINGVAR | bool_value;

bool_value: TRUE | FALSE;
```

## Instrukcja uruchomienia projektu <a name="servermsg"></a>

1. Installation: <br>
   ANTLR4 install command:<br>
   `pip install antlr4-python3-runtime==4.7.2`<br>
   Warning! Only 4.7.2 version works with this project.
2. Build project:<br>
   `antlr4 -Dlanguage=Python3 Hello.g4 -o dist` <br>
   with the visitor created:<br>
   `antlr4 -Dlanguage=Python3 -visitor Hello.g4`

<br>

1. How to check project grammar in Pycharm:
    1. Go to Hello.g4 file.
    2. Right-click on the 'program' production
    3. CLick 'Test rule program'
    4. Provide input and test if rule works fine.<br>
       or <br>

There are two ways to run translate a <code>C++</code> to a <code> Python </code>.

1. [Graphical User Interface](#gui)
2. [Command Line](#cl)

### Graphical User Interface <a name = "gui"></a>

In order to run the project via GUI the additional Python <code>Kivy</code> package is needed.

If you use Anaconda, you can install Kivy with its package manager Conda using:

`conda install kivy -c conda-forge`

For further information go to <a href=https://kivy.org/doc/stable/gettingstarted/installation.html> Kivy
documentation</a>.

To run the application simply run the [CppToPythonGui.py](#CppToPythonGui.py)

### Command Line <a name = "cl"></a>

You can run the application from the command line as well.

Go to *compilation_theory/antlr_approach* and open a command
line. Enter `py .\CppToPython.py -f [PathToCppFile.txt] -d [PathToPythonFile.py]`.

Argument `-f` specifies the file to be translated. The default output path is the same as the input file, name of the
output file is created as follows: `[filename.txt]` `[filename.py]`

Argument `-d` is **optional**, specifies the output file path. It is required to output file path ends with `.py`
extension.


## Testy  <a name="tests"></a>
### Prawidłowy kod <a name="pk"></a><br>
Testy zawierające prawidłowo napisany kod w C++. Translacja przebiega pomyślnie.

* [HelloWorld.txt](https://github.com/YgLK/compilation_theory/blob/main/antlr_approach/tests/final_correct/Classes.txt)

Prosty plik `HelloWorld` zawierający deklarację zmiennych oraz przypisywanie im wartości. Znajduje się tam też kod wyświetlanie na wyjście oraz przypisywania wartości na wejściu do zmiennych.
```cpp
#include<iostream>
using namespace std;

int main(){

    string a = "test string";
    int b = 4;
    int c = 3*12;
    string test = "Test string";
    cout << test;
    cout << "Enter text:";
    cin >> a;
    cout << a;

    string waitForInput;
    cin >> waitForInput;

    return 0;
};
```
Kod wynikowy z pliku `HelloWorld.txt` po translacji do języka **Python**:
```py
if __name__ == '__main__':
    a = "test string"
    b = 4
    c = 3*12
    test = "Test string"
    print(test)
    print("Enter text:")
    a = input()
    print(a)
    waitForInput = ""
    waitForInput = input()

```

* [Loops.txt](https://github.com/YgLK/compilation_theory/blob/main/antlr_approach/tests/final_correct/Loops.txt)

Plik `Loops` zawierający definiowanie własnych metod oraz ich wywołanie wraz z obsługą pętli `for` i `while` oraz instrukcją warunkową `if`. 
```cpp
#include<iostream>
using namespace std;

int main(){

    string a = "test string";
    int b = 4;
    int c = 3*12;
    string test = "Test string";
    cout << test;
    cout << "Enter text:";
    cin >> a;
    cout << a;

    string waitForInput;
    cin >> waitForInput;

    return 0;
};
```
Kod wynikowy z pliku `Loops.txt` po translacji do języka **Python**:
```py
def method1():
    print("First method")
    i = 0
    while i < 15:
        print(i)
        i += 1
    return i


def method2():
    print("Second method")
    k = 0
    while k < 3:
        print("Hi")
        k = 1 + k


if __name__ == '__main__':
    method1()
    method2()
    print("For loop")
    j = 1
    while j < 5:
        print(j)
        if j == 3:
            print("j is 3")
        else:
            print("j is smaller than 5")
        j += 1
    waitForInput = ""
    waitForInput = input()
```

* [Classes.txt](https://github.com/YgLK/compilation_theory/blob/main/antlr_approach/tests/final_correct/Classes.txt)

Przykładowy kod zawierający zdefiniowane klasy. Każda z klas może posiadać metody oraz atrybuty wraz z określonym modyfikatorem dostępnu (`public`, `protected`, `private`).
```cpp
using namespace std;

class Car{
    int year = 2019;
    private:
        int speed = 120;
    private:
        int gear = 3;
    public:
        string name = "Carl";
    protected:
        bool isSafe = true;
};

class Giraffe{
    private:
        int length = 3;
    public:
        int height = 13;

    public:
        int getHeight(){
            return height;
        }
    protected:
        int getHeight(){
            return height;
        }
    private:
        int getLength(){
            return length;
        }
};

int main(){
cout << "Classes";
};
```
Kod wynikowy z pliku `Classes.txt` po translacji do języka **Python**:
```py
class Car:
    year = 2019
    __speed = 120
    __gear = 3
    name = "Carl"
    _isSafe = True


class Giraffe:
    __length = 3
    height = 13

    def getHeight(self):
        return height

    def _getHeight(self):
        return height

    def __getLength(self):
        return length


if __name__ == '__main__':
    print("Classes")
```

### Nieprawidłowy kod <a name="nk"></a><br>
Testy zawierające nieprawidłowo napisany kod w C++. Podczas translacji wyświetlane są zdefiniowane błędy.

* [IncorrectCoutUse.txt](https://github.com/YgLK/compilation_theory/blob/main/antlr_approach/tests/final_error/IncorrectCoutUse.txt)<br>
W poniższym kodzie nieprawidłowo użyty został `cout`. Translator rozpoznaje błąd oraz informuje o nim użytkownika.
```cpp
using namespace std;

int main(){
    int a;
    cout >> "Hello world";	// prawidłowo powinno być `cout <<` zamiast `cout >>` 
    cin >> a;
    return 0;
};
```

* [InvalidCharacter.txt](https://github.com/YgLK/compilation_theory/blob/main/antlr_approach/tests/final_error/InvalidCharacter.txt)<br>
W poniższym kodzie występuje niedozwolony znak `$`. Translator rozpoznaje błąd oraz informuje użytkownika o typie błędu oraz miejscu jego wystąpienia.
```cpp
#include <iostream>
using namespace std;

int main()
{
    int a = 5;
    int b = 10;
    int temp;$		// nieprawidłowy znak `$`

    return 0;
};
```

* [MissingCurlyBrace.txt](https://github.com/YgLK/compilation_theory/blob/main/antlr_approach/tests/final_error/MissingCurlyBrace.txt)<br>
W poniższym kodzie brakuje nawiasu otwierającego `{` przy funkcji `main`. Podobnie jak w poprzednich przypadkach wyświetlany jest komumnikat o błędzie.
```cpp
using namespace std;

int main()		// brakuje `{`
    cout << "Hello World";
    int a;
    cin >> a;
    return 0;
};
```
