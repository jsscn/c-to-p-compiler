## Compilers: A C-to-P-Compiler

A compiler for a subset of C. _Project for the [Compilers](https://www.uantwerpen.be/popup/opleidingsonderdeel.aspx?catalognr=1001WETTEL&taal=en&aj=2015) course at the University of Antwerp._

### Requirements

*   Python 3

### Usage (from src/)

*   **build.sh** or **build.bat**  
    Generates a lexer and a parser we used to build an AST
*   **test.sh** or **test.bat**  
    Runs the unit tests in src/tests/  
    Tests can also be ran from src/tests/ with "python3 main.py".  
    If not all necessary files generated by antlr are present, this script will first run the build script.
*   **python3 c2p.py [-h] [-save-ast] [-save-symbol-table] [-t] [-q] [-o O] filename**  
    This will take a C file _filename_, and try to compile it.  
    If there are no errors, a .p file will be generated which can be ran using the P machine in resources/Pmachine. If any syntactic or semantical errors are recognized in the C file, they will be printed.
    Information about the flags can be found with **python3 c2p.py -h**
*   **visualize filename**  
    Shows the parse tree generated for _filename_

### Compilation Steps

After the parsing of a C file, an AST gets built using a listener.  
Visitors are used for the decoration of the AST, the filling of a symbol table, and for typechecking and code generation.  
In the first pass, The AST is decorated to make working with it easier.  
In the next pass, the symbol table is filled. This table is used for scoping and type checking.  
Then, another pass is done to check if all functions and variables are declared before use. If a variable or a function is used in a scope where it doesn't exist, an error is displayed.  
The compiler does not stop when it encounters an error, instead it marks the node in the AST which generated an error and skips this node in future passes.  
In the fourth pass over the AST, type checking is performed.  
Finally, in the fifth pass, if there were no errors, the P machine code generation is done.  
If there were errors and/or warnings, they will be displayed at this point. Go to the 'Errors and Warnings' section to get an idea of which messages can be given.

The order of precedence of operators and associativity is respected by the [grammar](src/C.g4).

### Optional Features

*   [multi-dimensional arrays](src/tests/programs/matrixMultiplication.c)
*   [multiple error output, instead of stopping after 1 error](src/tests/variable-declarations/char-arrays-pointers.txt)
*   [warnings](src/tests/function-declarations/22.txt)
*   extensive collection of errors
*   [array aggregate initialization](src/tests/misc/multidimensional-arrays.c)
*   [initializer lists for multi dimensional arrays](src/tests/misc/multidimensional-arrays.c)
*   [nested arrays and pointer types](src/tests/variable-declarations/multi-arrays-pointers.c)
*   [pointer arithmetic](src/tests/binary-operators/pointer-arithmetic.c)
*   [explicit type conversion](src/tests/programs/areaCirclePointer.c)
*   [const correctness](src/tests/const/10.c)
*   [break, continue](src/tests/misc/for-and-while.c)
*   [for loops](src/tests/misc/for-and-while.c)
*   [comma operator](src/tests/misc/global-var.c)
*   [variables get 'int' type by default if no type is specified at initialization](src/tests/function-declarations/23.c)
*   [binary operators <=, >=](src/tests/binary-operators/correct-literals.c)
*   [unary operators ++, --, [ ]](src/tests/unary-operators/5.c)
*   [do while loops](src/tests/misc/flow-control.c)
*   [multi-line comments](src/tests/programs/primsAlgorithm.c)
*   [initialization with strange bracket use](src/tests/variable-declarations/strange-brackets.c)

### Errors and Warnings

#### Errors

**symbol table checking**

*   variable '{0}' undeclared
*   function '{0}' undeclared
*   redefinition of function '{0}'
*   function: undefined reference to '{0}'
*   'break' statement not in loop statement
*   'continue' statement not in loop statement
*   identifier '{0}' already taken by variable
*   identifier '{0}' already taken by function
*   conflicting types for function declaration
*   function definition parameters don't match with previous declaration
*   parameter name omitted
*   'void' must be the only parameter
*   parameter '{0}' has incomplete type
*   function declaration parameters don't match previous definition
*   function declaration parameters don't match previous declaration

**type checking**

*   incompatible conversion returning '{0}' from a function with return type '{1}'
*   array size missing in '{0}'
*   array type has incomplete element type in '{0}'
*   expected integer literal as array length for '{0}'
*   invalid initializer
*   empty scalar initializer
*   incompatible types when initializing type '{0}' using type '{1}'
*   argument 1 of function '{0}' should be a string literal
*   format '{0}' expects argument of type '{1}', but argument {2} has type '{3}'
*   parameter {2} of '{3}' expected '{0}' but got '{1}'
*   number of arguments to function '{0}' does not match definition (have {1}, need {2})
*   invalid first operand to ternary '?:' (have '{0}', need 'int')
*   invalid operands to ternary '?:', alternatives should be of equal type (have '{0}' and '{1}')
*   invalid operands to binary '{2}' (have '{0}' and '{1}')
*   lvalue required as left operand of assignment
*   incompatible types when assigning to type '{0}' from type '{1}'
*   invalid operands to logical '{2}' (have '{0}' and '{1}', need 'int' and 'int')
*   invalid operands to comparison '{2}' (have '{0}' and '{1}')
*   lvalue required as {0} operand
*   invalid type argument of unary '*' (have '{0}')
*   lvalue required as unary '&' operand, (got rvalue of type '{0}')
*   invalid operand to logical '!' (have '{0}', need 'int')
*   subscripted value is neither array nor pointer nor vector
*   assigning to '{0}' from '{1}' discards 'const' qualifier
*   assignment of read-only location '{0}'
*   assignment of read-only variable
*   invalid use of void expression
*   variable or field '{0}' declared void
*   void value not ignored as it ought to be

#### Warnings

**symbol table checking**

*   variable used in its own initialization
*   type specifier missing, defaults to 'int'
*   type specifier missing, return type defaults to 'int'
*   type specifier missing in declaration of '{0}', type defaults to 'int'
*   data definition has no type or storage class, type defaults to 'int' in declaration of '{0}'

**type checking**

*   'return' with no value, in function returning non-void
*   'return' with a value, in function returning void
*   initialization from incompatible pointer type, expected '{0}' but got '{1}'
*   initialization makes pointer without a cast, expected '{0}' but got '{1}'
*   excess elements in array initializer of '{0}', expected {1} elements but got {2}
*   excess elements in scalar initializer
*   passing argument {0} of '{1}' from incompatible pointer type, expected '{2}' but got '{3}'
*   passing argument {2} of '{3}' discards 'const' qualifier, expected '{0}' but got '{1}'
*   initialization discards 'const' qualifier, expected '{0}' but got '{1}'
*   writing into constant object (argument {0})
*   taking address of expression of type ‘void’
*   unknown format code '{0}'
*   format '%{0}' expects a matching '{1}' argument
*   too many arguments for format (expected {0}, have {1})

### Testing

209 tests are included. They are made so that all of the possible errors are generated by as many different situations as possible. About 60 of the tests generate no error. For these tests, the P code they generate is checked.

### Classes

*   [AbstractSyntaxTree.py](images/AbstractSyntaxTree.png) (large image): AbstracSyntaxTree and ASTNode classes, these are used to build the AST we use.
*   [Listener](images/Listener.png): A listener which can build an AST when walking over a parse tree generated by antlr's parser.
*   [TypeInfo](images/TypeInfo.png): A class that contains information about the type of a variable or function.
*   [SymbolTable](images/SymbolTable.png): A symbol table class which is used for scope and type checking.
*   [Visitors](images/Visitors.png): Read the 'Compilation Steps' section for more information.  
    In order from first pass to last pass: VisitorDecorator, VisitorSymbolTableFiller, VisitorDeclarationProcessor, VisitorTypeChecker, VisitorCodeGenerator
*   [ErrorHandler](images/ErrorHandler.png): Used for collecting error and warnings and displaying them after semantic analysis.
*   [testfiles/main.py](images/testfiles-main.png): ASTTest and test classes, ASTTest provides the test classes with functions to test functionality easily.

### Authors
* [Josse Coen](https://github.com/jsscn)
* [Armin Halilovic](https://github.com/arminnh)
