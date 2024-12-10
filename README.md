# Create Your Own Interpreter

## **Overview**

This series demonstrates how to create a custom programming language from scratch. Using Python, we implement a simplified version of the BASIC programming language. By following this series, you'll build a basic interpreter that supports mathematical operations, parentheses, floating-point numbers, and error handling.

---

## **Features Implemented (Episode 1-3)**

1. Basic arithmetic operations:
   - Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`).
2. Support for floating-point and integer numbers:
   - Example: `2.5 + 1.2` results in `3.7`.
3. Parentheses for altering order of operations:
   - Example: `(2 + 3) * 4` evaluates correctly.
4. Follows standard mathematical precedence rules:
   - Example: `2 + 3 * 4` results in `14` (multiplication takes precedence).
5. Handles negative numbers:
   - Example: `-3 + 5` results in `2`.
6. Error detection:
   - Invalid characters trigger detailed error messages, including line numbers and positions.

---

## **Planned Features**

Future episodes will expand the language to include:
- **Variables**: Ability to define and use variables.
- **Functions**: Implement reusable functions.
- **Control Structures**: `if` statements and loops.
- **File Execution**: Execute external code files.

---

## **How It Works**

### **1. Lexer**
The lexer processes the input text, character by character, and converts it into **tokens**. Each token represents a meaningful piece of the input, such as:
- Numbers (e.g., `123`).
- Operators (e.g., `+`, `-`, `*`, `/`).
- Parentheses (e.g., `(`, `)`).

### **2. Error Handling**
Custom error classes (e.g., `IllegalCharError`) identify invalid characters. The interpreter reports:
- The file name (`<stdin>` if input is from the terminal).
- The exact line and column number of the error.

### **3. Position Tracking**
The interpreter tracks:
- **Index**: Current position in the input text.
- **Line and Column Numbers**: Used for precise error reporting.

---

## **Code Components**

### **Constants**
- `DIGITS`: Defines allowed numeric characters (`0123456789`).
- Token types (`TT_*`):
  - `TT_INT`: Integer token.
  - `TT_FLOAT`: Float token.
  - `TT_PLUS`, `TT_MINUS`, `TT_MUL`, `TT_DIV`: Arithmetic operators.
  - `TT_LPAREN`, `TT_RPAREN`: Parentheses.

### **Error Classes**
- **`Error`**: Base class for errors. Provides:
  - `as_string()`: Formats error messages for display.
- **`IllegalCharError`**: Raised when the lexer encounters an unsupported character.

### **Position Class**
Keeps track of:
- **Index**: Current position in the text.
- **Line and Column**: For precise error reporting.
- **File Name and Text**: Used to show error context.

### **Token Class**
Represents a unit of input. Each token has:
- A **type** (e.g., `TT_INT`).
- An optional **value** (e.g., `5` for `TT_INT`).

### **Lexer Class**
Converts input text into a list of tokens. Key methods:
1. **`advance()`**: Moves to the next character.
2. **`make_tokens()`**: Identifies tokens and ignores invalid inputs like spaces.
3. **`make_number()`**: Detects numbers (integers and floats).

### **Run Function**
Processes the input text and returns:
- A list of tokens.
- Any errors encountered.

### **Interactive Shell**
Prompts the user for input, processes it, and displays:
- Tokens for valid input.
- Errors with detailed information for invalid input.

---

---

## Episode 2: Parser Implementation

In the second episode, we built the **Parser** to create an Abstract Syntax Tree (AST) from the tokens. The AST represents the structure and hierarchy of operations in the input expression.

### Key Features Implemented:
1. **Abstract Syntax Tree**:
   - Constructs a tree to represent operations in the correct order of precedence.
   - Example:
     - Input: `1 + 2 * 3`
     - Tree: `(TT_INT:1, PLUS, (TT_INT:2, MUL, TT_INT:3))`

2. **Grammar Rules**:
   - Defined grammar rules for our language in `grammar.txt`:
     ```
     expr   : term ((PLUS | MINUS) term)*
     term   : factor ((MUL | DIV) factor)*
     factor : (PLUS | MINUS) factor | INT | FLOAT | LPAREN expr RPAREN
     ```
     - `expr`: An expression is made of terms connected by `+` or `-`.
     - `term`: A term is made of factors connected by `*` or `/`.
     - `factor`: A factor can be a number, a unary operation (e.g., `-5`), or an expression in parentheses.

3. **Unary Operations**:
   - Added support for unary operators like `+` and `-`.
   - Example: `-5` becomes `UnaryOpNode(-, TT_INT:5)`.

4. **Parentheses Support**:
   - Parentheses allow changing the order of operations.
   - Example:
     - Input: `(1 + 2) * 3`
     - Tree: `((TT_INT:1, PLUS, TT_INT:2), MUL, TT_INT:3)`

5. **Error Handling**:
   - Added `InvalidSyntaxError` for syntax issues like missing parentheses or invalid tokens.

### Example Inputs and Outputs:
1. Input: `1 + 2 * 3`  
   Output: `(TT_INT:1, PLUS, (TT_INT:2, MUL, TT_INT:3))`

2. Input: `(1 + 2) * 3`  
   Output: `((TT_INT:1, PLUS, TT_INT:2), MUL, TT_INT:3)`

3. Input: `1 +`  
   Error: `Invalid Syntax: Expected int or float`

4. Input: `(1 + 2`  
   Error: `Invalid Syntax: Expected ')'`

---

## What's Next?

In Episode 3, we will create the **Interpreter** to traverse the AST and execute the operations. By the end of the next episode, we will see results for our expressions, such as:
- Input: `1 + 2`
- Output: `3`

Stay tuned!

## **Usage**

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
