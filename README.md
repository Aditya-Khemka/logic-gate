
# logic-gate 

The logic-gate package provides a collection of basic logic gate functions such as AND, NAND, OR, NOR, NOT, XOR, and XNOR on boolean inputs.


## Installation

You can install the logic-gate package using pip:

```bash
  pip install logic-gate
```

## Usage / Examples

```python
from logic-gate import AND, NAND, OR, NOT

# Perform logical operations
result_and = AND(True, False)  # Returns False
result_or = OR(1, 0)  # Returns True
result_not = int NOT(True)  # Returns 0
result_nand = int (NAND(1,0))  # Returns 1

```

## Features / Functions

| Function    | Description |
| -------- | ------- |
| AND(a, b)  | Returns True if both a and b are True, otherwise returns False.    |
| NAND(a, b) | Returns True if at least one of a or b is False, otherwise returns False.     |
| OR(a, b)    | Returns True if at least one of a or b is True, otherwise returns False.    |
| NOR(a, b)  | Returns True if both a and b are False, otherwise returns False.    |
| NOT(a) | Returns the negation of a.     |
| XOR(a, b)    | Returns True if either a or b is True, but not both.    |
| XNOR(a, b)  | Returns True if both a and b are True or both a and b are False.    |

## License

This package is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. See the LICENSE file for details.


## Github

[Github](https://github.com/Aditya-Khemka/logic-gate)
