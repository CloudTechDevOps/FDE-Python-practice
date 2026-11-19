# 🐍 Python for FDE – Theory Explanation & Tasks


This file gives the theory behind each topic in the README's daily learning log. Each topic links to its practice notebook or folder and ends with **5 practice tasks** based on the same examples done in class, so you can redo them on your own.

---

## 📑 Index

| # | Date | Topic | Practice File |
|---|---|---|---|
| 1 | 26-Oct-2026 | Python Introduction & Fundamentals | [Day-1-identifier-variables.ipynb](Day-1-identifier-variables.ipynb) |
| 2 | 27-Oct-2026 | Variables and Identifiers | [Day-1-identifier-variables.ipynb](Day-1-identifier-variables.ipynb) |
| 3 | 28-Oct-2026 | Literals, Constants and Operators | [Day-2-Literals-Constent-Operators.ipynb](Day-2-Literals-Constent-Operators.ipynb) |
| 4 | 29-Oct-2026 | Assignment and Bitwise Operators | [Day-3-Assignement-bitwise-operators.ipynb](Day-3-Assignement-bitwise-operators.ipynb) |
| 5 | 30-Oct-2026 | Data Types, Type Conversion, f-Strings | [Day-4-DataTypes-TypeConverison-fstring.ipynb](Day-4-DataTypes-TypeConverison-fstring.ipynb) |
| – | 31-Oct-2026 | Doubt clearing session | – |
| 6 | 02-Nov-2026 | Conditional Statements (if, elif, else) | [Day-5-conditions-if-elif-else-nested-conditions.ipynb](Day-5-conditions-if-elif-else-nested-conditions.ipynb) |
| 7 | 03-Nov-2026 | For Loop | [Day-6-loops-for.ipynb](Day-6-loops-for.ipynb) |
| 8 | 04-Nov-2026 | While Loop | [Day-7-loops-while.ipynb](Day-7-loops-while.ipynb) |
| 9 | 05-Nov-2026 | Data Structures – String, List, Tuple | [Day-8-Data-Structure-string-list-tuple-dictionery.ipynb](Day-8-Data-Structure-string-list-tuple-dictionery.ipynb) |
| 10 | 06-Nov-2026 | Data Structures – Mutability & Immutability | [Day-9-DataStructures-mutability-immutability.ipynb](Day-9-DataStructures-mutability-immutability.ipynb) |
| 11 | 09-Nov-2026 | Functions – No Parameter / Return | [Day-10-Functions-no-parameter-return.ipynb](Day-10-Functions-no-parameter-return.ipynb) |
| 12 | 10-Nov-2026 | Functions – With Parameter / Return | [Day-11-Functions-with-parameter-return.ipynb](Day-11-Functions-with-parameter-return.ipynb) |
| 13 | 11-Nov-2026 | GenAI with Python Functions – SDK & LLM Calling | [Day-12-SDK-LLM-Models-calling.ipynb](Day-12-SDK-LLM-Models-calling.ipynb) |
| 14 | 12-Nov-2026 | Lambda Functions | [Day-13-python-lambda-function.ipynb](Day-13-python-lambda-function.ipynb) |
| 15 | 13-Nov-2026 | Exception Handling | [Day-14-Exception-handlings.ipynb](Day-14-Exception-handlings.ipynb) |
| 16 | 14-Nov-2026 | Git and GitHub Recap | – |
| 17 | 16-Nov-2026 | Python Environments | [env-modules/envs/](env-modules/envs/) |
| 18 | 17-Nov-2026 | Python Modules – import, from, user-defined, built-in | [env-modules/modules/](env-modules/modules/) |
| 19 | 18-Nov-2026 | OOP Introduction – Class, Object, Methods, Variables | [OOps-python/practice.ipynb](OOps-python/practice.ipynb) |
| 20 | 19-Nov-2026 | OOP – Class & Instance Variables, Methods, Constructor, Encapsulation | [OOps-python/oops.ipynb](OOps-python/oops.ipynb) |

---

## 1. Python Introduction & Fundamentals
📅 26-Oct-2026 · 📓 [Day-1-identifier-variables.ipynb](Day-1-identifier-variables.ipynb)

### What is Programming?
Programming means writing a set of instructions that a computer can follow. A **programming language** lets humans write those instructions in a form that is readable for people and can be translated for the machine.

### What is Python?
Python is a **high-level, interpreted, general-purpose** programming language.

- **High-level:** the syntax reads almost like English. You do not manage memory or hardware details yourself.
- **Interpreted:** the Python interpreter runs code line by line, so there is no separate compile step. This makes testing and debugging fast.
- **Dynamically typed:** you do not declare a variable's type. Python works out the type from the value at runtime.
- **General-purpose:** it is used for automation, web backends, data engineering, AI/ML, cloud scripting and more.
- **Huge ecosystem:** there are thousands of ready-made libraries (the standard library plus third-party packages from PyPI).

### Why Python for an FDE?
A Forward Deployed Engineer works directly with customers to integrate systems, automate workflows, call APIs and LLMs, and build quick prototypes. Python is the most common language for this work because it is fast to write, easy to read, and has SDKs for almost every cloud and AI service.

### How Python Runs Code
1. You write source code in a `.py` file or a notebook cell.
2. The interpreter converts it into **bytecode**.
3. The **Python Virtual Machine (PVM)** executes the bytecode.

### Keywords vs Built-ins
- **Keywords** are reserved words that form Python's grammar, such as `if`, `else`, `for`, `def`, `return`, `True` and `None`. They **can never** be used as variable names. The `keyword` module lists them all.
- **Built-ins** are ready-made functions and objects that are always available, such as `print`, `len`, `type`, `input` and `int`. You *can* reuse their names as variables, but you should not, because that hides the original function.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Use the `keyword` module to print the full list of Python keywords, then print how many keywords there are.
2. Try to use a keyword (for example `if` or `for`) as a variable name and assign it a value. Run it and note the error message you get.
3. Use `keyword.iskeyword()` to check "if", "len", "print", "while" and "True". Note which are keywords and which are not.
4. Use `dir(builtins)` to check whether "print", "len", "input" and "if" are built-ins. Explain why `if` is not in the list.
5. Assign the number 4 to `len` and print it. Then try to find the length of "FDE" with `len`, note what breaks, and explain why you should not reuse built-in names.
---

## 2. Variables and Identifiers
📅 27-Oct-2026 · 📓 [Day-1-identifier-variables.ipynb](Day-1-identifier-variables.ipynb)

### Identifier
An **identifier** is any name you give to a program element: a variable, function, class, module and so on.

### Variable
A **variable** is a name that **refers to an object in memory** while the program runs. In Python, a variable does not "contain" the value. It is a **label pointing to an object**. Assigning a new value points the label at a new object.

> Every variable name is an identifier, but not every identifier is a variable. Function and class names are identifiers too.

### Rules for Identifiers (and Variables)
1. Use only **letters (A–Z, a–z), digits (0–9) and underscore (`_`)**.
2. **Never start with a digit.** `2name` is invalid, but `name2` is valid.
3. **No spaces and no hyphens.** `first name` and `customer-name` are invalid.
4. **Keywords cannot be used**, for example `if` or `for`.
5. Identifiers are **case-sensitive**: `Name`, `name` and `NAME` are three different identifiers.
6. Avoid using **built-in names** such as `len`, `list` and `str`. This is a best practice, not a hard rule.

### Naming Conventions (PEP 8)
- Use `snake_case` for variables and functions, for example `customer_name`.
- Use `UPPER_CASE` for constants, for example `DB_PORT`.
- Use `PascalCase` for classes, for example `CustomerAccount`.
- A leading underscore (`_total`) signals "internal use".
- Choose meaningful names: `total_price` is better than `tp`.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Create the valid variables from class (`customer_name`, `age2`, `_total`, `application_version`) with your own values and print each one.
2. Try the invalid identifiers from class (`2name`, `customer-name`, `first name`). Note the error for each and which rule it breaks.
3. Write a small function like `my_function` that adds two variables `a` and `b` into `c` and returns it. List which names in it are variables and which are other identifiers.
4. Create `Name`, `name` and `NAME` with three different values and print all three to show that Python is case-sensitive.
5. Create server configuration variables `server_name`, `server123` and `_server` (for example "localhost", "test" and "production") and print them in one line.
---

## 3. Literals, Constants and Operators
📅 28-Oct-2026 · 📓 [Day-2-Literals-Constent-Operators.ipynb](Day-2-Literals-Constent-Operators.ipynb)

### Literals
A **literal** is a fixed value written directly in code.

| Literal Type | Meaning |
|---|---|
| Integer | Whole numbers such as 15 or -3 |
| Float | Decimal numbers such as 99.99 |
| String | Text in quotes, such as "FDE" |
| Boolean | `True` / `False` |
| None | Represents "no value" |
| Collection literals | list `[ ]`, tuple `( )`, set `{ }`, dict `{key: value}` |

### Constants
A **constant** is a value that should not change during the program, such as `PI` or `DB_PORT`. Python has **no true constant keyword**. By convention, constants are written in **UPPER_CASE** so other developers know not to change them.

### Operators
Operators are special symbols that perform operations on values (operands).

**1. Arithmetic operators**

| Operator | Meaning | Note |
|---|---|---|
| `+` `-` `*` | Add, subtract, multiply | |
| `/` | Division | Always returns a **float** |
| `//` | Floor division | Rounds **down toward negative infinity**, so -9 // 5 gives -2, not -1 |
| `%` | Modulus | Returns the remainder. If the dividend is smaller than the divisor, the result is the dividend itself |
| `**` | Power | 2 ** 3 = 8 |

**2. Comparison operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`. These always return `True` or `False`.

**3. Logical operators**
- `and` is True only if **both** conditions are True.
- `or` is True if **at least one** condition is True.
- `not` **reverses** the result.

Python uses **short-circuit evaluation**. With `and`, if the first condition is False, the second is not checked. With `or`, if the first is True, the second is skipped.

**4. Membership operators:** `in` and `not in` check whether a value exists inside a sequence or collection (string, list, tuple, set, or the keys of a dict).

**5. Identity operators:** `is` and `is not` check whether two variables point to the **same object in memory**. This is not the same as equal values (`==`). (The notebook lists `is` / `is not` under membership, but they are actually identity operators.)

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Create one variable for each literal type from class (integer `age`, float `price`, string `name`, boolean `is_active`, None `result`, list, tuple, set and dict) and print the type of each.
2. Create constants `DB_PORT = 3306` and `PI = 3.14` and a normal variable `age`. Explain which values should never change and why they are in UPPER_CASE.
3. With x = 21 and y = 11, print the results of `/`, `//`, `%` and `**`. Then repeat `/` and `//` with x = -9 and y = 5, and explain why floor division gives -2.
4. Predict, then check, the results of 10 % 3, 10 % 20 and 20 % 30. Also calculate 2 ** 3 and 3 ** 4.
5. Build the voting eligibility check (age >= 18). Using a = 10 and b = 20, test `a > 5 and b > 15`, then `a > 5 or b < 15`, then `not`. Finally, check whether "apple" and "orange" are in the fruits list ["apple", "banana", "mango"] using `in` and `not in`.
---

## 4. Assignment and Bitwise Operators
📅 29-Oct-2026 · 📓 [Day-3-Assignement-bitwise-operators.ipynb](Day-3-Assignement-bitwise-operators.ipynb)

### Assignment Operators
These are shorthand forms that update a variable using its current value.

| Operator | Equivalent To |
|---|---|
| `x += 5` | `x = x + 5` |
| `x -= 5` | `x = x - 5` |
| `x *= 3` | `x = x * 3` |
| `x /= 5` | `x = x / 5` (result becomes a float) |
| `x //= 5` | `x = x // 5` |
| `x %= 6` | `x = x % 6` |
| `x **= 2` | `x = x ** 2` |

### Increment / Decrement
Python has **no `++` or `--` operators**. Use `x += 1` to increment and `x -= 1` to decrement.

### Binary Basics
Computers store numbers in binary (base 2). For example, 5 = `101`, 3 = `011` and 15 = `1111`. Bitwise operators work on these individual bits.

### Bitwise Operators

| Operator | Name | Rule |
|---|---|---|
| `&` | AND | 1 only if **both** bits are 1 |
| `\|` | OR | 1 if **any** bit is 1 |
| `^` | XOR | 1 if the bits are **different** |
| `~` | NOT | Flips all bits. In Python, **~a = -(a + 1)**, so ~6 = -7 |

Example: 5 & 3 → 101 & 011 = 001 = **1**, 5 | 3 = **7**, and 5 ^ 3 = **6**.

### Shift Operators
- **Left shift (`<<`)** moves bits to the left and adds 0s on the right. Each shift **multiplies by 2**: 15 << 1 = 30 and 15 << 2 = 60.
- **Right shift (`>>`)** moves bits to the right and drops the right-most bits. Each shift does **floor division by 2**: 15 >> 1 = 7 and 15 >> 2 = 3.

### Where Bitwise Operators Are Used
Permission flags (read/write/execute), network subnet masks, compact storage of on/off settings, and performance-critical code.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Start with x = 10 and apply `+=5`, `-=5`, `*=3`, `/=5`, `//=5`, `%=6` and `**=2` one at a time (resetting x each time). Print the result after each.
2. Create a counter starting at 10. Increment it by 1 using `+=` and print it, then decrement it by 1 using `-=` and print it.
3. Left shift: calculate 15 << 1, 19 << 2 and 21 << 3. For each, write the binary value before and after the shift.
4. Right shift: calculate 15 >> 1, 15 >> 2, 15 >> 3 and 15 >> 4. Write the binary for each and explain which bits are dropped.
5. With a = 5 and b = 3, then with a = 8 and b = 4, print Bitwise AND, OR and XOR. Print ~6 and check that it matches the formula -(a + 1).
---

## 5. Data Types, Type Conversion and f-Strings
📅 30-Oct-2026 · 📓 [Day-4-DataTypes-TypeConverison-fstring.ipynb](Day-4-DataTypes-TypeConverison-fstring.ipynb)

### Built-in Data Types

| Category | Type | Description | Ordered | Mutable | Duplicates |
|---|---|---|---|---|---|
| Numeric | `int` | Whole numbers | – | No | – |
| Numeric | `float` | Numbers with a fractional part | – | No | – |
| Numeric | `complex` | Real + imaginary part (2+1j) | – | No | – |
| Boolean | `bool` | `True` / `False` (a subtype of int) | – | No | – |
| Text | `str` | Characters inside quotes | Yes | No | Yes |
| Sequence | `list` `[ ]` | Ordered collection | Yes | **Yes** | Yes |
| Sequence | `tuple` `( )` | Ordered collection | Yes | No | Yes |
| Sequence | `range` | Sequence of integers | Yes | No | – |
| Set | `set` `{ }` | Unique elements | **No** | **Yes** | **No** |
| Mapping | `dict` `{k: v}` | Key–value pairs | Yes (insertion order) | **Yes** | Keys: No |
| None | `NoneType` | The absence of a value | – | – | – |

The `type()` function tells you the type of any value.

### Type Conversion (Type Casting)
Converting a value from one type to another.

- **Implicit conversion:** Python converts automatically when it is safe. For example, int + float gives a float.
- **Explicit conversion:** you convert yourself using `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()` or `dict()`.

Key points:
- `int()` on a float **cuts off** the decimal part (it does not round).
- `int("25")` works, but `int("hello")` or `float("hello")` raises a **ValueError**.
- `list("25")` breaks the string into characters, giving `['2', '5']`. `set()` does the same but removes duplicates.
- `dict("hello")` fails, because a dict needs key–value pairs.

### Input and Output
- `input()` reads text from the keyboard and **always returns a string**. To do maths with it, convert it with `int()` or `float()`.
- `print()` displays output. It can print several values separated by commas.

### f-Strings (Python 3.6+)
An **f-string** (formatted string literal) puts variables and expressions directly inside a string using `{ }`, prefixed with `f`.
- It is cleaner than joining strings with `+`, which also needs `str()` for numbers.
- Expressions can go inside the braces, for example `{age / 2}`.
- It supports formatting, such as decimal places and padding.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Create one example of every data type from class (int `age`, float, complex `2+1j`, bool, str, list, tuple, set with a duplicate 30, dict `student`, None and `range(5)`). Print each value with its type name.
2. Take age = "25" (a string) and convert it to int, float, list, tuple and set. Print each result and its type.
3. Try `float("hello")` and `dict("hello")`. Note the error each one gives and explain why the conversion fails.
4. Build the product price program: read the price with `input()`, convert it to float, multiply by quantity 2, and print "Total price". Then try it without the float conversion and see what happens.
5. With name = "chitti", age = 30 and weight = 50, print "My name is … I am … years old" three ways: with `+`, with commas in `print`, and with an f-string. In the f-string version, also print age / 2 inside the braces.
---

## 📌 31-Oct-2026 – Doubt Clearing Session
No new topic. This was a revision session for Days 1–5. Use it as a checkpoint: re-attempt any task from Sections 1–5 you were not confident about.

---

## 6. Conditional Statements (if, elif, else, nested)
📅 02-Nov-2026 · 📓 [Day-5-conditions-if-elif-else-nested-conditions.ipynb](Day-5-conditions-if-elif-else-nested-conditions.ipynb)

### Indentation
Python uses **indentation** (spaces at the start of a line) to group statements into blocks, instead of the curly braces used by other languages. The standard is **4 spaces**. Wrong indentation causes an `IndentationError` or a logic bug, because a statement ends up in the wrong block.

### Rules
1. Every `if`, `elif` and `else` line ends with a **colon (`:`)**.
2. **Indentation is mandatory** for the block under it.
3. `elif` and `else` **cannot stand alone**. They must follow an `if`.
4. A one-line shorthand is allowed for very simple cases, such as `if a > 5: print("hello")`.

### Types of Conditions
- **Simple if:** runs a block only when the condition is True.
- **if–else:** two paths. One runs if True, the other if False.
- **if–elif–else:** many paths. Python checks top to bottom and runs **only the first matching block**.
- **Nested if:** a condition inside another condition, used when a second check makes sense only after the first passes.

### Multiple `if` vs `if–elif`
With separate `if` statements, **each condition is checked independently**, so several blocks can run. For example, marks of 75 would print both "Grade B" and "Grade C". With `if–elif`, only **one** block runs. Use `elif` for mutually exclusive choices, such as grades.

### Truthy and Falsy
Conditions do not need to be a literal `True`/`False`. Values such as `0`, `""`, `[]`, `{}` and `None` count as **False**. Most other values count as True.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Voting eligibility: read the age with `input()` (converted to int) and print "eligible to vote" or "not eligible" using if–else.
2. Login check: store a password such as "Akki123", compare it with a user's input, and print "login successful" or "Invalid password".
3. Grade program with marks = 75: first write it with three separate `if` statements and see that two grades print. Then rewrite it with `if–elif–elif–else` so only "Grade B" prints.
4. Nested condition: with marks = 70 and lab = 90, print "pass" if marks >= 60, and inside that, check if lab >= 90 for "eligible for 1st grade". Otherwise print "fail". Test with different marks and lab values.
5. Write a one-line shorthand `if` (a = 6, print "hello" if a > 5). Then remove the indentation from an if-block on purpose, note the IndentationError, and fix it.
---

## 7. For Loop
📅 03-Nov-2026 · 📓 [Day-6-loops-for.ipynb](Day-6-loops-for.ipynb)

### What is a Loop?
A loop repeats a block of code. The **for loop** is used to **iterate over a sequence or iterable**, such as a string, list, tuple, dict, set or range, one item at a time.

### How It Works
In each iteration, the loop variable (for example, `i`) takes the next item from the sequence. The loop ends automatically when the items run out.

### Iterating Different Types
- **String:** one character at a time.
- **List / Tuple:** one element at a time.
- **Dictionary:** by default you get the **keys**. Use `.keys()`, `.values()` or `.items()` (key–value pairs) for more control.
- **range(start, stop, step):** generates numbers from start up to (but **not including**) stop. For example, range(1, 6) gives 1, 2, 3, 4, 5.

### Loop Control
- **break** stops the loop immediately.
- **continue** skips the rest of the current iteration and moves to the next one.
- **for–else:** the `else` block runs only if the loop finished **without** a `break`. This is useful for "search and not found" logic.

### Accumulator Pattern
A common pattern is to start a variable such as `total` before the loop and update it on every iteration. This is how sums, counts and running totals are built.

### Combining Concepts
One loop line can involve many concepts: a variable, the assignment operator, a list, the `for` keyword, the `in` membership keyword, an `if` condition, `%` (arithmetic), `==` (comparison), `print()` (a built-in), indentation and the `:` delimiter.

The `random` module (for example, `random.randint`) can be used inside loops for simulations.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Loop over the string "python" and print each letter. Then loop over the list ["aws", "azure", "gcp"] and print each cloud name.
2. For the dictionary {"name": "veera", "course": "fde"}, write three loops that print the keys, the values and the items (key–value pairs).
3. Loop over [10, 20, 30, 40, 50], print each number, and when it reaches 40, print "number found" and `break`. Then try `break` at 2 with the list [1, 2, 3, 4, 5, 6].
4. Sum the numbers in range(1, 6) starting with total = 1, and write a table of total after each iteration (as done in class). Repeat with total = 2 and compare the answers.
5. Classify the list [10, -5, 0, 20, -8] as positive, negative or zero. Then use `random.randint(1, 100)` in a loop of 5 iterations to print whether each number is even or odd, and whether it is greater than 50.
---

## 8. While Loop
📅 04-Nov-2026 · 📓 [Day-7-loops-while.ipynb](Day-7-loops-while.ipynb)

### What is a While Loop?
A **while loop** repeats a block **as long as a condition stays True**. The condition is checked before each iteration.

### Key Parts
1. **Initialisation:** set a starting value, for example `i = 1`.
2. **Condition:** for example `i <= 10`.
3. **Update:** change the variable inside the loop, for example `i = i + 1`.

If you forget the update, the condition stays True forever and you get an **infinite loop**.

### Infinite Loops (`while True`)
`while True` runs forever on purpose and is stopped with `break`. This is the standard pattern when **you don't know in advance how many times to repeat**, for example a chatbot that runs until the user types "exit", or a server that keeps listening.

### for vs while

| for loop | while loop |
|---|---|
| Iterates over a known sequence | Repeats while a condition is True |
| Number of iterations is known | Number of iterations is unknown or condition-based |
| Example: process each item in a list | Example: keep asking until the password is correct |

### break and continue
These work the same way as in `for` loops: `break` exits and `continue` skips to the next check.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Print the numbers 1 to 10 using a while loop with `i <= 10`. Then change the condition to `i <= 1` and explain why it prints only once.
2. Write the infinite loop that prints 0, 1, 2, … (with `i = i + 1`). Add a `break` so it stops at 10. Explain what happens if you remove the increment line.
3. Password login: give the user up to 4 attempts. Print "allow to login" and `break` when the password is "akki", otherwise print "not allow" and continue.
4. Chatbot: first allow only 3 questions using `for i in range(1, 4)`. Then rewrite it with `while True` so the user can keep asking until they type "exit" (case-insensitive with `.lower()`).
5. Loop over range(1, 6) with `continue` at 2 and `break` at 4 and write down the output. Then use only `continue` at 3 and compare the outputs.
---

## 9. Data Structures – String, List, Tuple (Indexing & Slicing)
📅 05-Nov-2026 · 📓 [Day-8-Data-Structure-string-list-tuple-dictionery.ipynb](Day-8-Data-Structure-string-list-tuple-dictionery.ipynb)

### Overview of Python Data Structures

| Structure | Description | Mutable? |
|---|---|---|
| `str` | Collection of characters | Immutable |
| `list` | Collection of elements | Mutable |
| `tuple` | Collection of elements | Immutable |
| `set` | Collection of unique elements | Mutable |
| `dict` | Key–value pairs | Mutable |

### Indexing
Indexing means accessing a single element by its position.
- **Positive index:** starts at **0** from the left.
- **Negative index:** starts at **-1** from the right.

```
 P   Y   T   H   O   N
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```
Accessing an index that does not exist raises an **IndexError**.

### Slicing – `[start : stop : step]`
Slicing extracts a portion of a sequence.
- **start** is included. If you leave it out, it means "from the beginning".
- **stop** is **excluded**. If you leave it out, it means "to the end".
- **step** is how many positions to move each time. The default is 1.
- **Positive step** moves left to right, so start must come before stop.
- **Negative step** moves right to left, so start must come after stop. `[::-1]` reverses the sequence.
- Slicing **never raises an error** for an out-of-range stop value. It simply returns what is available, or an empty result if the range makes no sense, such as `[3:3]`.
- `[:]` returns a full copy.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. For word = "PYTHON", print P, H and N using positive indexes, then print the same letters using negative indexes.
2. In class, "last character" was printed with `word[-6]`, which actually gives the first letter. Fix it so the last character is printed correctly.
3. Predict, then run, these slices of "PYTHON": [3:5], [3:3], [2:5], [:3], [:4], [:10], [3:], [1:] and [:].
4. Negative slicing: run [-4:3], [-4:2], [-4:-5:1], [-4:-5:-1] and [-4:-6:-1] on "PYTHON". Explain which return empty strings and why.
5. Step slicing: on "veerafdedghst", run [1:8:2] and write out which indexes were picked. Then reverse "PYTHON" using a negative step.
---

## 10. Data Structures – Mutability & Immutability
📅 06-Nov-2026 · 📓 [Day-9-DataStructures-mutability-immutability.ipynb](Day-9-DataStructures-mutability-immutability.ipynb)

### Mutable vs Immutable
- **Mutable** objects can be changed in place after they are created. Examples: list, set, dict.
- **Immutable** objects cannot be changed after they are created. Examples: str, tuple, int, float, bool. Any "change" actually creates a **new object**.

### Strings (Immutable)
- Trying to replace one character (such as setting `word[0]`) raises a **TypeError**.
- To "modify" a string, build a new one, for example by joining "J" with a slice of the old word.
- Useful methods:
  - `join()` combines a list of strings into one, with a separator.
  - `split()` breaks a string into a list using a separator. For example, splitting "2026-11-06" on "-" gives the year, month and day.
  - Others include `upper()`, `lower()`, `strip()`, `replace()` and `find()`. All of these **return new strings**.

### List (Mutable)
Lists support indexing, slicing, and in-place changes.

| Method | Purpose |
|---|---|
| Index assignment | Update an element at a position |
| `append(x)` | Add **one** element to the end. Appending a list adds it as a single nested element |
| `extend(iterable)` | Add **each** element of another iterable to the end |
| `insert(i, x)` | Add an element at a specific position |
| `remove(x)` | Delete by **value** (the first match) |
| `del list[i]` | Delete by **index** |
| `pop()` / `pop(i)` | Remove and **return** the last element, or the element at index i |
| `sort()` | Sort in place |

### Tuple (Immutable)
- Supports indexing and slicing like a list.
- **Does not support** append, insert, remove, extend, sort or item updates.
- Use a tuple for fixed data that must not change, such as coordinates or configuration values. Tuples are also slightly faster and can be used as dict keys.

### Set (Mutable, Unique, Unordered)
- Duplicates are removed automatically.
- **No indexing**, because order is not guaranteed.
- Methods: `add()`, `remove()`, `discard()`, `pop()` (removes an arbitrary element), and `update()`.
- Supports maths-style operations: union, intersection and difference.

### Dictionary (Mutable, Key–Value)
- Access a value by its **key**, for example `student["name"]`.
- **Keys must be unique.** If a key appears twice, the **last value wins**.
- Assigning to an existing key **updates** it. Assigning to a new key **adds** it.
- `pop(key)` removes a key and returns its value. This is useful for renaming a key.
- Useful methods: `get()`, `keys()`, `values()`, `items()` and `update()`.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Try to change the first letter of "PYTHON" to "J" using its index and note the TypeError. Then create "JYTHON" as a new string by joining "J" with a slice, and print both the old and new strings.
2. Join ["python", "is", "easy"] into one sentence with spaces. Split the date "2026-11-06" on "-" into year, month and day.
3. With fruits = ["apple", "banana", "orange"], do the following one at a time and print each result: replace index 0 with "mango", `append` "mango", `append` ["mango", "cherry"], `extend` ["mango", "cherry"], and `insert` "grape" at position 1. Explain the difference between the two appends and extend.
4. With the same fruits list, try `remove("banana")`, `del` at index 1, `pop()`, `pop(1)`, and `sort()` on ["banana", "apple", "orange"]. Note which ones work by value and which by index.
5. Tuple, set and dict: try to append to a tuple and note the error. Print a set {10, 20, 10, 30, 40, 50} and see the duplicate removed, then use `pop()`. For the student dict, access "name", add a duplicate "age" key, update age to 40, add city "hyd", and rename "name" to "student_name" using `pop`.
---

## 11. Functions – No Parameters / Return Value
📅 09-Nov-2026 · 📓 [Day-10-Functions-no-parameter-return.ipynb](Day-10-Functions-no-parameter-return.ipynb)

### What is a Function?
A **function** is a **reusable, named block of code** that performs a specific task. You define it once and call it as many times as you need.

### Types of Functions
1. **Built-in functions:** predefined in Python and ready to use, such as `print`, `len`, `type`, `input` and `sum`.
2. **User-defined functions:** created by you with the `def` keyword.

### Anatomy of a Function
- `def` is the keyword that creates a function.
- The **function name** follows identifier rules.
- `( )` holds the parameters, which can be empty.
- `:` marks the start of the function body.
- The **indented body** contains the statements.
- The **function call**, such as `greet()`, executes the function. Defining a function does not run it.

### Four Function Patterns
1. No parameters, no return value
2. No parameters, with a return value
3. With parameters, no return value
4. With parameters, with a return value

### print vs return
- `print()` only **displays** a value on the screen. A function with no `return` gives back **`None`**.
- `return` **sends a value back** to the caller. You can store it in a variable, use it in conditions, or pass it to another function. `return` also ends the function immediately.

### Benefits of Functions
Code reusability, shorter code, easier maintenance in large projects, easier debugging and testing, better readability, and fewer repeated steps. Compare calculating a monthly salary for three people with copy-pasted code versus one reusable function.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Create `greet()` that prints three names. Call it three times. Then store its result in a variable, print it, and explain why it shows `None`.
2. Create `addition()` with a = 5 and b = 20 inside it, which prints the first number, the second number and their sum.
3. Call `greet()` inside a `for` loop over range(1, 4), printing "Iteration: i" before each call.
4. Create a function that returns the monthly income from an annual income of 20000. Create `get_age()` that returns 25, and use the returned value in an if–else to print "major" or "minor".
5. Create `calculate_final()` that returns the final price for price 1000 with a 10% discount. Then calculate the monthly salary for three people (60000, 120000 and 240000), first without a function and then with one function, and compare the code length.
---

## 12. Functions – With Parameters / Return Value
📅 10-Nov-2026 · 📓 [Day-11-Functions-with-parameter-return.ipynb](Day-11-Functions-with-parameter-return.ipynb)

### Parameters vs Arguments
- **Parameters** are the variable names in the function **definition**, such as `a` and `b`.
- **Arguments** are the actual values passed in the function **call**, such as 10 and 20.

### Returning Multiple Values
A function can return several values separated by commas. Python packs them into a **tuple**, which can be unpacked into separate variables.

### Function Chaining
The return value of one function can be passed as input to another (for example, add, then multiply, then divide). This is the basis of building **pipelines**.

### Types of Arguments
1. **Positional arguments:** values are matched to parameters **by order**. Swapping the order gives wrong results.
2. **Keyword arguments:** values are passed **by parameter name**, so order does not matter.
3. **Default arguments:** a parameter has a default value that is used if no argument is given, for example a city that defaults to "Hyderabad".
4. **`*args` (variable-length positional):** collects any number of positional values into a **tuple**.
5. **Keyword-only arguments:** parameters that come after `*` or `*args` **must** be passed by name.
6. **`**kwargs` (variable-length keyword):** collects any number of keyword arguments into a **dictionary**. The names `args` and `kwargs` are only conventions.

### Parameter Order Rules
Standard order: **normal parameters → `*args` → keyword-only parameters → `**kwargs`**

1. Normal parameters can come before `*args`.
2. Parameters after `*args` become keyword-only.
3. Keyword-only parameters can be swapped among themselves.
4. `**kwargs` must **always be last**.
5. Nothing can be placed after `**kwargs`. That causes a **SyntaxError**.

| Signature | Valid? |
|---|---|
| rollno, *subjects, city, **details | ✅ |
| *subjects, rollno, city, **details | ✅ (rollno and city become keyword-only) |
| rollno, city, *subjects, **details | ✅ (city becomes a normal parameter) |
| rollno, *subjects, **details, city | ❌ SyntaxError |

### Local and Global Variables
- A **local variable** is defined inside a function and exists only while that function runs.
- A **global variable** is defined outside all functions and can be read anywhere.
- If a function assigns to a name, Python creates a **new local variable** by default, even if a global with the same name exists.
- The `global` keyword tells Python to use and modify the existing global variable. Use it sparingly, because returning values is cleaner.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Create `calculate_bill(price, quantity, discount)` that returns final_amount, discount_amount and total. Call it with positional arguments, then with keyword arguments in a different order, and confirm the results match.
2. Create `student(name, age, course)`. Call it with positional arguments in the wrong order and see the mixed-up output, then fix it using keyword arguments.
3. Function chaining: add 3 + 2 in a first function, pass the result to a second function that multiplies by 2, then pass that to a third function that divides by 3. Print the final result.
4. Default and keyword-only arguments: create `student(name, age=25, city="Hyderabad")` and call it for Veera, Rahul (city Bangalore) and Akash (22, Chennai). Then create `employee(name, *, salary, city)`, call it correctly, and call it with only positional values to see the error.
5. Student registration: create `student(rollno, *subjects, city, **details)` and register a student with roll number 101, subjects Python and AWS, city Hyderabad and name Veera. Try the valid and invalid parameter orders from class. Finally, update a global `salary` from 50000 to 60000 inside a function using the `global` keyword.
---

## 13. GenAI with Python Functions – SDK & LLM Model Calling
📅 11-Nov-2026 · 📓 [Day-12-SDK-LLM-Models-calling.ipynb](Day-12-SDK-LLM-Models-calling.ipynb)

### What is an SDK?
An **SDK (Software Development Kit)** is a collection of tools, libraries and functions provided by a company so developers can use its service easily. Instead of writing all the HTTP request, authentication and response-parsing logic yourself, you install the SDK and call ready-made functions.

### What is an LLM?
A **Large Language Model (LLM)** is an AI model trained on huge amounts of text. It can understand and generate natural language. Examples are Gemini (Google), GPT models (OpenAI), Claude (Anthropic) and open models served by providers such as Groq.

### How an LLM Call Works
1. **Install the SDK** with pip, for example `google-genai` or `openai`.
2. **Create a client** with your **API key**. The key proves who you are and is used for billing.
3. **Send a request** with the **model name** and the **input/prompt**.
4. **Receive the response** and read the generated text from it.

### Wrapping LLM Calls in Functions
Putting the LLM call inside a function (such as `ask_gemini(prompt)`) gives you:
- **Reusability:** call it with any prompt, any number of times.
- **One place to change** the model name, settings or error handling.
- **Clean integration** into larger programs, such as chatbots and pipelines.

### OpenAI-Compatible APIs
Many providers, such as Groq, offer an **OpenAI-compatible endpoint**. You use the OpenAI SDK but change the **`base_url`** to point at the provider. One SDK can then talk to many providers.

### API Key Security
- **Never** hard-code API keys in notebooks or source code, and **never commit them to Git**.
- Store them in **environment variables** or a `.env` file (loaded with `python-dotenv`), and add `.env` to `.gitignore`.
- If a key is exposed, **revoke (rotate) it** immediately.

### Listing Models
SDKs usually provide a way to list the available models, so you can see which model names you can use.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Install `google-genai`, create a Gemini client (load the API key from an environment variable or `.env` file, not typed in the code), and ask "what is aws in one line?". Print the output text.
2. Make two separate calls: "what is aws in one line?" and "what is python in one line?". Print both answers.
3. Write an `ask_gemini(prompt)` function that returns the output text. Call it three times for Python, Java and AWS, and print the three results.
4. Use `client.models.list()` with a for loop to print the names of all available models, and pick one you would use.
5. Call a Groq model using the OpenAI SDK with Groq's `base_url`, and ask "Explain the importance of fast language models". Store the Groq key in `.env` and make sure `.env` is in `.gitignore`.
---

## 14. Lambda Functions
📅 12-Nov-2026 · 📓 [Day-13-python-lambda-function.ipynb](Day-13-python-lambda-function.ipynb)

### What is a Lambda?
A **lambda function** is a **small, anonymous function** (a function without a formal name), written in one line with the `lambda` keyword.

Syntax: `lambda arguments : expression`

### Normal Function vs Lambda

| Normal Function (`def`) | Lambda |
|---|---|
| Has a name | Anonymous (can be assigned to a variable) |
| Can have many statements | **One expression only** |
| Needs an explicit `return` | **Returns the expression automatically** |
| Assignments allowed inside | Multiple assignment statements not allowed |
| Used for complex, reusable logic | Used for short, throwaway logic |

A lambda can include a **conditional expression** (ternary), such as returning "even" if a number divides by 2 and "odd" otherwise.

### Where Lambdas Are Commonly Used
As short inline functions passed to other functions, such as `sorted(key=...)`, `map()`, `filter()` and `max(key=...)`.

### eval()
`eval()` is a built-in function that takes a **string** and **evaluates it as a Python expression**. For example, the string "5+3" becomes 8.
⚠️ **Security warning:** never use `eval()` on untrusted user input. It can run any code. Prefer `int()` or `float()` for reading numbers.

### Walrus Operator `:=` (Python 3.8+)
The **walrus operator** assigns a value to a variable **and** uses it inside the same expression. For example, you can compute the length of a list, store it, and compare it in one `if` condition. It avoids writing a separate line just to store a value that is used once in a condition.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Convert the normal `add(a, b)` function into a lambda, call it with 10 and 20, and compare the two versions. Also write a lambda that returns the square of 5.
2. Write the even/odd lambda and test it with 10 and 7. Then write the positive/negative lambda. Note that the class version used `x > 0 == 0`, which gives the wrong answer; fix it to `x > 0` and retest with -7 and 10.
3. Use `eval(input())` to read a number and print whether it is greater than 10. Then try typing an expression such as 5+8, and explain why eval is risky with user input.
4. Walrus operator: for the list [10, 20, 30, 40], store `len(numbers)` in `count` inside the if condition and print it when it is greater than 3. Then combine the walrus operator with `input()` in the greater-than-10 check.
5. Try to write the multi-statement lambda from class (a = x*2, b = x/2, c = a+b) and note the SyntaxError. Rewrite it as a single expression, (x*2) + (x/2), and confirm it gives the same answer as the normal function for 5.
---

## 15. Exception Handling
📅 13-Nov-2026 · 📓 [Day-14-Exception-handlings.ipynb](Day-14-Exception-handlings.ipynb)

### What is an Exception?
An **exception** is an error that happens **while the program is running**, such as dividing by zero or converting "abc" to int. Without handling, the program **crashes** and stops.

### Errors vs Exceptions
- **Syntax errors** are mistakes in the code structure. They are caught before the program runs and cannot be handled.
- **Exceptions** happen at runtime and **can be handled** gracefully.

### The try / except / else / finally Structure

| Block | Runs When |
|---|---|
| `try` | Always. It contains the code that might fail |
| `except` | Only if an exception occurs in `try` |
| `else` | Only if **no** exception occurs |
| `finally` | **Always**, error or not. Used for cleanup, such as closing files or connections |

A `try` block cannot stand alone. It needs at least one `except` or a `finally`.

### Catching Exceptions
- A **bare `except`** catches everything. Avoid it, because it hides real bugs.
- **`except Exception as e`** catches the error and stores the error object in `e`, so you can log or print the message.
- **Specific exceptions** are best practice, because each one gets its own handling.
- **Multiple exceptions in one block:** list them in a tuple, such as ValueError and ZeroDivisionError together.

### Common Built-in Exceptions

| Exception | Cause |
|---|---|
| `ZeroDivisionError` | Dividing by zero |
| `ValueError` | Right type but invalid value, such as int("hello") |
| `TypeError` | Wrong type for an operation, such as adding a string to a number |
| `IndexError` | List or tuple index out of range |
| `KeyError` | Dictionary key not found |
| `NameError` | Variable not defined |
| `FileNotFoundError` | File does not exist |

### raise
`raise` **manually triggers** an exception when your own business rule is broken, for example raising a ValueError with the message "age must be 18 or above". This stops bad data early with a clear message.

### Exceptions in Loops
Placing try/except inside a loop lets the program **continue or retry** after an error instead of stopping. This is useful for retrying API calls or processing many records.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Run 10 / 0 without any handling and note the error. Then wrap it in try/except to print "cannot divide by zero", and finally use `except Exception as e` to print the actual error message.
2. Add a `finally` block that prints "execution completed". Run it once with b = 0 and once with b = 2, and confirm finally runs both times.
3. With age = 15, use `raise ValueError("age must be 18 or above")` before printing "eligible to vote". Test it with ages 15 and 19.
4. Read two numbers with `input()` and divide them. Handle ZeroDivisionError, ValueError and TypeError separately with their own messages. Then rewrite it with ValueError and ZeroDivisionError in one tuple, plus `else` and `finally` blocks.
5. Build `process_data(items, index, divisor)` that reads an item by index, converts it to int and divides it. Handle IndexError/KeyError, ValueError and ZeroDivisionError. Then use a while loop with a count of 3 to retry a division with try/except inside.
---

## 16. Git and GitHub Recap
📅 14-Nov-2026 · *(Recap session. No notebook.)*

### Git vs GitHub
- **Git** is a **version control system** that runs on your computer. It tracks every change to your files, so you can go back in time, compare versions and work on features safely.
- **GitHub** is a **cloud hosting platform** for Git repositories. It adds collaboration features: remote backup, pull requests, code review, issues and Actions (CI/CD).

### Core Concepts
- **Repository (repo):** a project folder tracked by Git. The `.git` folder stores the history.
- **Working directory → Staging area → Commit:** you edit files, **stage** the changes you want (`git add`), then **commit** them as a snapshot with a message.
- **Commit:** a saved snapshot with an ID, author, time and message.
- **Branch:** an independent line of development. `main` is the default. Feature branches keep work separate until it is ready.
- **Merge:** combines one branch's changes into another. A **merge conflict** happens when two branches change the same lines.
- **Remote / origin:** the GitHub copy of the repo.
- **push / pull / clone / fetch:** push sends your commits to the remote, pull gets and merges remote changes, clone copies a repo to your machine, and fetch downloads changes without merging.
- **Pull Request (PR):** a request on GitHub to merge a branch, with review and discussion.
- **.gitignore:** lists files Git should **never track**, such as `.env`, `.venv`, `__pycache__` and secrets.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Open a terminal in `FDE-Python-practice`, run `git status`, and identify which files are untracked, modified and staged (for example `explanation.md`).
2. Stage `explanation.md` with `git add`, commit it with a clear message, and view the history using `git log --oneline`.
3. Create a new branch, update the README table with a new date and topic, commit it, switch back to `main`, and merge the branch.
4. Push your commits to your GitHub repository, then open GitHub and check that the new commit and file appear there.
5. Open `.gitignore` and check that `.env`, `.venv` and `__pycache__` are listed. Then create a merge conflict on purpose (edit the same README line on two branches) and resolve it.
---

## 17. Python Environments
📅 16-Nov-2026 · 📁 [env-modules/envs/](env-modules/envs/)

### The Problem Environments Solve
Different projects need different packages and **different versions** of the same package. If everything is installed into one global Python, projects conflict ("it works on my machine" problems), and upgrading a package for one project can break another.

### What is a Virtual Environment?
A **virtual environment** is an **isolated folder** with its own Python interpreter link and its own installed packages. Each project gets its own independent set of dependencies.

### Three Approaches in This Folder

**1. Common (global) environment:** [common-python-application-env](env-modules/envs/common-python-application-env/)
- Packages are installed into the system Python with `pip`.
- It is simple, but every project shares the same packages and versions, which risks conflicts.
- This is fine for quick experiments, but not recommended for real projects.

**2. Traditional `venv` + `pip`:** [virtual-env-python-approch](env-modules/envs/virtual-env-python-approch/)
- `venv` is Python's **built-in** module for creating virtual environments, usually in a `.venv` folder.
- You must **activate** the environment. The activation script differs between PowerShell, Command Prompt, Git Bash and macOS/Linux, and the prompt then shows `(.venv)`.
- Packages are installed with `pip`, and the exact versions are recorded in **`requirements.txt`** so others can recreate the same environment.
- `deactivate` returns you to the normal Python.
- You can check which Python is active using the `VIRTUAL_ENV` variable or by checking the location of `python`.

**3. Modern `uv`:** [uv-env-python-approach](env-modules/envs/uv-env-python-approach/)
- **uv** (by Astral) is a very fast, all-in-one tool for managing Python projects and packages, often 10–100x faster than pip thanks to caching.
- **`pyproject.toml`** declares project metadata and dependencies.
- **`uv.lock`** records the **exact resolved versions** for reproducible installs.
- **`.python-version`** pins the Python version.
- Main commands, in theory: `uv init` creates a project, `uv venv` creates the environment, `uv add` adds a dependency, `uv sync` installs everything from the lock file, and `uv run` runs a script inside the environment without manual activation.

### Environment Variables and `.env`
All three examples load `GROQ_API_KEY` from a `.env` file using `python-dotenv`. Secrets stay **outside the code**, and the `.env` file is never committed.

### Comparison

| Feature | Global | venv + pip | uv |
|---|---|---|---|
| Isolation | ❌ | ✅ | ✅ |
| Dependency file | – | requirements.txt | pyproject.toml + uv.lock |
| Speed | Normal | Normal | Very fast |
| Python version management | ❌ | ❌ | ✅ |
| Needs manual activation | – | Yes | Optional (`uv run`) |

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Common environment: in `common-python-application-env`, install `openai` and `python-dotenv` into your global Python, add `GROQ_API_KEY` to `.env`, and run `app.py`.
2. venv: in `virtual-env-python-approch`, create `.venv`, then activate it once in PowerShell and once in Git Bash. Check that `(.venv)` appears in the prompt.
3. Inside the activated venv, install the packages from `requirements.txt`, run `app.py`, and confirm the active Python by checking `VIRTUAL_ENV` and the python path. Then `deactivate`.
4. uv: install uv, check `uv --version`, then in `uv-env-python-approach` run `uv sync` and `uv run app.py`. Note how much faster the install is than pip.
5. Create a new uv project from scratch: `uv init`, `uv venv`, then `uv add openai python-dotenv`. Open `pyproject.toml` and `uv.lock` and note what each file records.
---

## 18. Python Modules – import, from, User-defined, Built-in
📅 17-Nov-2026 · 📁 [env-modules/modules/](env-modules/modules/)

### What is a Module?
A **module** is simply a **Python file (`.py`)** that contains functions, variables or classes. You can reuse it in other files by **importing** it. A **package** is a folder of modules (often with an `__init__.py` file).

### Why Use Modules?
- **Organisation:** split a large program into small, focused files.
- **Reusability:** write once and import anywhere.
- **Maintainability:** a bug fix in one module applies everywhere it is used.
- **Namespace separation:** avoids name clashes between different parts of the code.

Compare [without_module.py](env-modules/modules/user-define-module/without_module.py), which has everything in one file, with the separate addition, subtraction, multiplication and division modules that [main.py](env-modules/modules/user-define-module/main.py) imports.

### Types of Modules
1. **Built-in / standard library modules** come with Python and need no installation, such as `math`, `random`, `datetime`, `os` and `keyword`. See [built-in-modules](env-modules/modules/built-in-modules/).
2. **User-defined modules** are your own `.py` files. See [user-define-module](env-modules/modules/user-define-module/).
3. **Third-party modules** are installed from PyPI using pip or uv, such as `requests`, `openai` and `python-dotenv`. See [third_party_weather.py](env-modules/modules/third_party_weather.py/), which uses `requests` to get live weather data from a web API and read values from the JSON response.

### Import Styles
- **Plain import** (for example, import math): you access members with the module prefix. This is clear about where things come from.
- **from … import** (for example, from math import sqrt): you use the name directly, without a prefix.
- **Import several names**, such as sqrt and factorial, in one line.
- **Alias:** give a module a shorter name, as is common with libraries like pandas.
- **Avoid `from module import *`**, because it pulls in every name and can cause hidden name clashes.
- `dir(module)` lists everything a module contains.

### What Happens on Import
When a module is imported, Python **runs all of its top-level code once**. That is why `print` statements in [message.py](env-modules/modules/Basic-modules-guard-methos/message.py) and [calculator.py](env-modules/modules/gurad_method/calculator.py) appear when [main.py](env-modules/modules/gurad_method/main.py) imports them.

### The Guard Method: `if __name__ == "__main__":`
- Every module has a built-in variable called `__name__`.
- When a file is **run directly**, `__name__` is set to `"__main__"`.
- When a file is **imported**, `__name__` is set to the **module's name**, such as "calculator".
- So code inside the guard **runs only when the file is executed directly**, and **not when it is imported**.
- Use it for test code, demo code and the program's entry point (`main()`), so importing a module does not trigger unwanted side effects.

### Mini Microservice Example
[moule-mini-microservice/main.py](env-modules/modules/moule-mini-microservice/main.py) combines everything learned so far: functions, dictionaries, loops, f-strings, `raise ValueError` for validation, and a guarded entry point. It simulates a small shopping flow: register a customer, show products, add to cart and calculate the total. This is how real services are structured as small, focused functions.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Built-in modules: print `dir(math)`, then find the square root of 25 using `import math` and again using `from math import sqrt`. Also import `sqrt` and `factorial` together and calculate factorial(5).
2. Print the current date and time with `datetime.now()`, and use `random.randint(0, 100)` to generate a list of 10 random marks.
3. Guard method: run `message.py` directly, then run `main.py` which imports it, and compare the outputs. Do the same with `calculator.py` and its `main.py`, and explain why the code inside `if __name__ == "__main__":` runs only once.
4. User-defined modules: compare `without_module.py` with the separate `addition`, `subtraction`, `multiplication` and `division` modules. Run `main.py`, then add a fifth module (for example `modulus`) and import it in `main.py`.
5. Third-party module: install `requests`, run the weather program for your city, and print the temperature, feels-like value, humidity and weather description. Then run the mini microservice, add a new product, and test what happens when the quantity is 0.
---

## 19. OOP Introduction – Class, Object, Methods, Variables
📅 18-Nov-2026 · 📓 [OOps-python/practice.ipynb](OOps-python/practice.ipynb)

### What is OOP?
**Object-Oriented Programming (OOP)** is a way of organising code around **classes** and **objects**. Data (variables) and the behaviour that works on that data (functions) are kept together in one unit, instead of being spread across separate variables and functions.

### Class
A **class** is a **blueprint or template** for creating objects. It describes what data an object will hold and what it can do. You define one with the `class` keyword, and by convention class names use **PascalCase** (such as `Car` or `Student`).

### Object
An **object** is an **instance** of a class: a real thing built from the blueprint. You create one by calling the class like a function, with brackets after the name. The variable on the left (such as `c1`) is a **reference** to that object. You can create many objects from one class, and each one has its own data.

### Attributes (Variables) and Dot Notation
Variables that belong to a class or object are called **attributes**. You read them with **dot notation**: object name, a dot, then the attribute name (such as `c1.color`).

### Methods
A **method** is a **function defined inside a class**. It describes what the object can do, such as `start`, `stop` or `move` for a car. You call it with dot notation on the object, for example `car1.start()`.

### self
- Every instance method must take **`self` as its first parameter**.
- `self` refers to **the object the method was called on**. When you call `c1.display()`, Python passes `c1` in as `self` automatically.
- Inside the class, `self.name` means "the `name` belonging to this particular object".
- `self` is a naming convention, not a keyword, but always use it.

### `__init__` (A First Look)
`__init__` is a special method that runs **automatically when an object is created**. Values passed in the brackets (such as `Car("skoda", "red")`) are received by `__init__` and stored on the object with `self`. This is covered in more depth in the next section.

### Without OOP vs With OOP
In the notebook, three cars were first written **without OOP**: every car needed its own variables (`car1_color`, `car2_color`, ...) and its own copy of every function (`start_car1`, `start_car2`, ...). Adding a fourth car means copying everything again.

With OOP, **one `Car` class** holds the data and the `start`, `stop` and `move` methods. Each new car is just one line, such as `Car("white", 12, "electric")`.

| Without OOP | With OOP |
|---|---|
| Separate variables for every item | One class, many objects |
| Functions duplicated per item | Methods written once and shared |
| Hard to add or change items | New object = one line |
| Data and functions are loosely connected | Data and behaviour bundled together |

### The Four Pillars of OOP (Preview)
1. **Encapsulation:** bundling data with methods and protecting it from direct outside access.
2. **Inheritance:** a class reusing and extending another class.
3. **Polymorphism:** the same method name behaving differently in different classes.
4. **Abstraction:** hiding complex details and exposing only what is needed.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Create a `Car` class with the variables `name = "skoda"`, `color = "red"` and `speed = 100`. Create an object `c1` and print all three values using dot notation.
2. Create a `Student` class with `name`, `roll` and `age`. Create two objects and print their values. Notice that both objects show the same data, and think about why.
3. Add a `display(self)` method to the `Car` class that prints the name and color. Call it with `c1.display()`, then try defining it without `self` and note the error you get.
4. Write a `Car` class with `__init__(self, name, color)`. Create `Car("skoda", "red")` and `Car("bmw", "black")` and print each car's name and color.
5. Rewrite the three-car "without OOP" example as one `Car` class with `color`, `mileage` and `fuel`, and `start`, `stop` and `move` methods. Create three cars, call every method on each, and then add a fourth car to see how little code it needs.
---

## 20. OOP – Class & Instance Variables, Methods, Constructor, Encapsulation
📅 19-Nov-2026 · 📓 [OOps-python/oops.ipynb](OOps-python/oops.ipynb)

### Class Variables
- Defined **directly inside the class**, outside any method (such as `school = "ABC"` or `country = "India"`).
- **Shared by all objects** of the class: there is one copy, and every object sees it.
- Can be accessed through the **class name** (`Student.school`) or through **an object** (`s1.school`).
- Use them for values that are the same for every object, such as the bank name or the country.

### Instance Variables
- Defined **inside a method using `self`** (such as `self.name = name`).
- **Belong to one object only**: each object has its own copy with its own value.
- Accessed through the object (`s1.name`).
- Use them for data that differs per object, such as name, roll number or balance.

| | Class Variable | Instance Variable |
|---|---|---|
| Where defined | Inside the class, outside methods | Inside a method, with `self.` |
| Copies | One, shared by all objects | One per object |
| Accessed with | `ClassName.var` or `obj.var` | `obj.var` |
| Example | `bank_name = "HDFC"` | `self.balance = balance` |

### Instance Methods
An **instance method** is a normal method that takes `self` as its first parameter, so it can read and change that object's instance variables. `display`, `deposit`, `withdraw` and `show_balance` in the notebook are all instance methods.

### Constructor: `__init__`
- `__init__` is the **constructor**. Python calls it **automatically** every time an object is created.
- Its job is to **set up the object's starting data** (its instance variables).
- The arguments you pass when creating the object, such as `Student("veera", 232, 20)`, go straight into `__init__`.
- The double underscores mark it as a special ("dunder") method.

**Without `__init__`:** you create an empty object and then must remember to call a separate method (such as `display`) to fill in the data. If you forget, the object has no data and accessing it raises an `AttributeError`.

**With `__init__`:** the object is created and filled in **one step**, so every object always starts complete.

### Why OOP Instead of Separate Variables
The student example compared four students stored as twenty separate variables (`s1_name`, `s1_age`, ...) plus a `display_student` function, against one `Student` class with a constructor. With the class, each student is one line, and all of a student's data travels together in one object.

### Encapsulation
**Encapsulation** means **bundling data and the methods that work on it inside a class**, and **restricting direct access** to that data from outside. Outside code should change the data only through the class's methods, so the class stays in control and can enforce rules (such as "you cannot withdraw more than the balance").

**Without encapsulation:** in the `Bank` example, anyone can write `b1.balance = 0` and wipe the balance directly, skipping `deposit` and `withdraw` completely.

### Access Levels in Python (Naming Conventions)

| Style | Example | Meaning |
|---|---|---|
| Public | `self.name` | Accessible from anywhere |
| Protected | `self._balance` | **Convention only**: "internal, please don't touch from outside". Python does not block it |
| Private | `self.__balance` | Python **name-mangles** it, so it cannot be accessed by that name from outside the class |

### Private Variables and Name Mangling
- A variable starting with **two underscores** (such as `self.__balance`) is **private**.
- Python renames it internally to `_Bank__balance`. This is called **name mangling**.
- Inside the class, `self.__balance` works normally.
- Outside the class, reading `b1.__balance` raises an `AttributeError`.
- In the notebook, `b1.__balance = 0` **did not change the real balance**. It quietly created a **new, separate attribute** on the object, and `show_balance()` still printed the correct balance. That is encapsulation protecting the data.
- Name mangling discourages access but is not true security: `b1._Bank__balance` still reaches it. Python relies on convention ("we are all consenting adults").

### Controlling Access with Methods
The right way to work with private data is through **methods**, which can validate input. For example, `deposit` can reject negative amounts and `withdraw` can refuse to go below zero. A method that returns a private value (such as `get_balance()`) is called a **getter**, and one that changes it safely is a **setter**.

### 📝 Tasks
*(Based on the examples practised in class.)*

1. Create a `Student` class with class variables `school = "ABC"` and `country = "India"`. Print them using the class name and using an object. Then change `Student.school` and check that every object sees the new value.
2. Add a `display(self, name, roll, age)` method that stores instance variables. Create two students with different data and confirm that each object keeps its own values. Then create a third object, skip calling `display`, try printing its name, and note the error.
3. Rewrite the class with `__init__(self, name, roll, age)` so data is passed at creation time. Create four students (veera, sai, kumar, raju) with name, age, mobile, email and course, and print each one.
4. Build the `Bank` class without encapsulation, then set `b1.balance = 0` from outside and show the balance. Rebuild it with `self.__balance`, try `b1.__balance = 0`, and explain why `show_balance()` still prints the correct amount. Try printing `b1.__balance` and `b1._Bank__balance` too.
5. Improve the encapsulated `Bank` class: make `deposit` reject amounts ≤ 0, make `withdraw` refuse to go below zero (print "insufficient balance"), and add a `get_balance()` getter. Test it with valid and invalid amounts.
---

### 🎯 Learning Objective
Build a strong foundation in Python programming through daily practice, hands-on coding and practical examples relevant to FDE work.

**Note:** When a new topic is added to [README.md](README.md), add a matching section here with its theory and 5 tasks.
