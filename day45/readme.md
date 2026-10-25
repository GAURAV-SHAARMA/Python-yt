# Python: `if __name__ == "__main__"`

## 1. What does it mean?

```python
if __name__ == "__main__":
    print("Hello World")
```

**Meaning:** Run the code inside this `if` block only when the Python file is executed directly, not when it is imported into another Python file.

## 2. What is `__name__`?

Python automatically creates a special variable called `__name__` in every Python file (module).

- **When you run a file directly:** `__name__` becomes `"__main__"`.
- **When you import a file:** `__name__` becomes the module's name, such as `"test"`.

Therefore, `if __name__ == "__main__":` checks whether the file is being run directly as the main program.

## 3. Example: Two Python Files

### File 1: `calculator.py`

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))
```

### File 2: `main.py`

```python
import calculator

print(calculator.add(5, 3))
```

### Case A: Run `calculator.py` directly

Command:

```bash
python calculator.py
```

Output:

```text
30
```

The file is running directly, so the condition is `True`.

### Case B: Run `main.py`

Command:

```bash
python main.py
```

Output:

```text
8
```

Here, `calculator.py` is imported. Its guarded `print(add(10, 20))` does not execute, but its `add()` function can still be used.

## 4. What Happens When We Import a File?

Consider `test.py`:

```python
def greet():
    print("Hi")

if __name__ == "__main__":
    print("Python")
    greet()
```

Now, in another file, write:

```python
import test
```

**Output:**

```text
(no output)
```

### Why?

1. Python defines the `greet()` function.
2. Since the file is imported, `__name__` becomes `"test"`.
3. The condition is `False`.
4. Both `print("Python")` and `greet()` are skipped.

However, if you write:

```python
import test
test.greet()
```

Output:

```text
Hi
```

The function executes because we explicitly called it.

**Remember:** Defining a function does not execute its body. Calling the function does.

## 5. Code Outside the `if` Block

```python
print("Hello")

if __name__ == "__main__":
    print("Welcome")
```

**If run directly:**

```text
Hello
Welcome
```

**If imported into another file:**

```text
Hello
```

The `print("Hello")` statement is outside the condition, so it executes during import too.

## 6. When Should We Use It?

### Use it when:

- Your file contains functions or classes that may be imported into other files.
- You want to execute the main program only when the file is run directly.
- You want to keep testing or demonstration code separate from reusable functions.
- You are building a Python project with multiple modules.

### It is optional when:

- You are writing a small, one-time script that will only be run directly and never imported.

## 7. Recommended Coding Pattern

```python
def main():
    print("Program started")
    print("Hello World")

if __name__ == "__main__":
    main()
```

Here, `main()` contains the main program logic, and the condition controls when it runs.

## 8. Quick Revision Table

| Situation | Value of `__name__` | Does the block execute? |
|---|---|---|
| File run directly | `"__main__"` | Yes |
| File imported as `test` | `"test"` | No |

## Final Takeaway

`if __name__ == "__main__":` means:

**"Execute this code only when this file is run directly as the main program."**

It helps you reuse functions and classes from one Python file in another without automatically running the first file's main code.