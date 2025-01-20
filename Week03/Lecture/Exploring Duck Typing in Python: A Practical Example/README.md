
# Understanding Duck Typing in Python

This document explains Duck Typing in Python using the following example code:

```python
def add(a, b):
    return a + b

print(add(5, 10))        # Valid: integer addition.
print(add("hello", " world"))  # Valid: string concatenation.
print(add(5, "hello"))   # Runtime Error.
```

## Code Explanation

### Function Definition
```python
def add(a, b):
    return a + b
```
- This function takes two arguments, `a` and `b`, and returns their sum using the `+` operator.
- Python does not enforce static type checking. Instead, it assumes that the objects passed as arguments to the function support the `+` operation.

### Function Calls and Duck Typing
```python
print(add(5, 10))  # Valid: integer addition.
```
- Here, `a = 5` and `b = 10`. Both are integers, and Python supports the `+` operation for integers (addition). The result is `15`.

```python
print(add("hello", " world"))  # Valid: string concatenation.
```
- Here, `a = "hello"` and `b = " world"`. Both are strings, and Python supports the `+` operation for strings (concatenation). The result is `"hello world"`.

```python
print(add(5, "hello"))  # Runtime Error.
```
- Here, `a = 5` (integer) and `b = "hello"` (string). Python does **not** support the `+` operation between integers and strings. This results in a `TypeError` at runtime:
  ```
  TypeError: unsupported operand type(s) for +: 'int' and 'str'
  ```

## Relation to Duck Typing

Duck Typing in Python is based on the principle of "If it looks like a duck, swims like a duck, and quacks like a duck, it is a duck." In Python, this means that the suitability of an object for an operation is determined by its behavior rather than its explicit type.

### Key Features of Duck Typing in the Example

1. **Behavior-driven Compatibility:** The `add` function works as long as the `+` operator is valid for the types of `a` and `b`. Python relies on the objects to "quack like a duck" (i.e., support the operation).

2. **Runtime Type Checking:** Python does not check the types of `a` and `b` when the function is defined or called. Instead, it checks their compatibility at runtime when the `+` operation is performed.

3. **Flexibility:** Duck Typing allows the `add` function to work with various types (e.g., integers, strings, lists) as long as the `+` operation is supported.

4. **Polymorphism:** This flexibility allows functions like `add` to exhibit polymorphic behavior, supporting multiple data types with a single implementation.

### Potential Pitfalls
- If the objects passed to the function are incompatible for the required operation, a `TypeError` occurs at runtime.
- It is the programmer's responsibility to ensure compatibility or handle errors using mechanisms like `try-except` blocks.

## Summary
This example highlights the power and potential pitfalls of Duck Typing in Python, showcasing how Python's dynamic typing system relies on object behavior rather than explicit types to determine operation compatibility.
