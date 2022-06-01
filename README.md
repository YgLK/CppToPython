# compilation_theory

| Token         |   Kod   |
| ------------- | :---------: |
| PLUS          |     `+`     |
| MINUS         |     `-`     |
| DPLUS         |    `++`     |
| DMINUS        |    `--`     |
| MUL           |     `*`     |
| DIV           |     `/`     |
| MOD           |     `%`     |
| ESC           |     `\`     |
| RPARENTH      |     `)`     |
| LPARENTH      |     `(`     |
| LSQUARE       |     `[`     |
| RSQUARE       |     `]`     |
| LBRACE        |     `{`     |
| RBRACE        |     `}`     |
| COLON         |     `:`     |
| SEMICOLON     |     `;`     |
| COMMA         |     `,`     |
| QUOTE         |     `"`     |
| APOSTROPHE    |     `'`     |
| DOT           |     `.`     |
| GTHAN         |     `>`     |
| LTHAN         |     `<`     |
| NOT           |     `!`     |
| EQUAL         |     `=`     |
| DEQUAL        |    `==`     |
| GREATER_EQUAL |    `>=`     |
| LESS_EQUAL    |    `<=`     |
| NOT_EQUAL     |    `!=`     |
| LBIT          |    `<<`     |
| RBIT          |    `>>`     |
| INT           |    `int`    |
| FLOAT         |   `float`   |
| CHAR          |   `char`    |
| STRING        |  `string`   |
| BOOL          |   `bool`    |
| VOID          |   `void`    |
| WHILE         |   `while`   |
| FOR           |    `for`    |
| IF            |    `if`     |
| ELSE          |   `else`    |
| CIN           |    `cin`    |
| COUT          |   `cout`    |
| MAIN          |   `main`    |
| USING         |   `using`   |
| NAMESPACE     | `namespace` |
| STD           |    `std`    |
| INCLUDE       |  `include`  |
| HASH          |     `#`     |
| RETURN        |  `return`   |
| BREAK         |   `break`   |
| CONTINUE      | `continue`  |
| DELETE        |  `delete`   |
| ENDL          |   `endl`    |
| SPACE         |     ` `     |
| BREAKLINE     |    `\n`     |
| TAB           |    `\t`     |
| CLASS         |      `class`         |
| PUBLIC        |      `public`        |
| PRIVATE       |      `private`       |
| PROTECTED     |      `protected`     | 
<!-- 
| AND           |    `&&`     |
| OR            |      `      |  | ` |
| CLASS         |      `class`         |
| PUBLIC        |      `public`        |
| PRIVATE       |      `private`       |
| PROTECTED     |      `protected`     | 
 CONST         |      `const`         |
| STATIC        |      `static`        |
| VIRTUAL       |      `virtual`       | 
-->

| Token      |           Regexp            |
| ---------- | :-------------------------: |
| VARNAME    | `^[a-zA-Z$][a-zA-Z_$0-9]*$` |
| FLOATVAR   |     `^-?\d*\.{0,1}\d+$`     |
| INTVAR     |          `^-?\d+$`          |
| STRINGVAR  |          `^".*"$`           |
| COMMENTVAR |          `^\/\/.*`          |
