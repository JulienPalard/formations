# Python Functions

----

## Syntax

```python
def the_function_name(the_arguments):
    """The function documentation
    """
    # The function body
    return # An optional returned value
```

----

## Arguments

A function can accept multiple arguments.

```python
def draw_square(width, height):
    print("+" + "-" * width + "+")
    for line in range(height):
        print("|" + " " * width + "|")
    print("+" + "-" * width + "+")

----

## Arguments
```python
>>> draw_square(3, 2)
+---+
|   |
|   |
+---+
```
