# Calculator API Reference

## Calculator Class

The `Calculator` class provides basic mathematical operations with history tracking.

### Constructor

#### `Calculator()`
Creates a new calculator instance.

**Returns:** Calculator instance

**Example:**
```python
calc = Calculator()
```

### Methods

#### `addition(a, b)`
Adds two numbers.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:** float - The sum of a and b

**Example:**
```python
result = calc.addition(5, 3)  # Returns 8.0
```

#### `subtract(a, b)`
Subtracts the second number from the first.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:** float - The difference of a and b

**Example:**
```python
result = calc.subtract(10, 4)  # Returns 6.0
```

#### `multiply(a, b)`
Multiplies two numbers.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:** float - The product of a and b

**Example:**
```python
result = calc.multiply(2, 7)  # Returns 14.0
```

#### `divide(a, b)`
Divides the first number by the second.

**Parameters:**
- `a` (float): Dividend
- `b` (float): Divisor

**Returns:** float - The quotient of a and b

**Raises:** ValueError - If b is zero

**Example:**
```python
result = calc.divide(15, 3)  # Returns 5.0
```

#### `get_history()`
Retrieves the calculation history.

**Returns:** list - List of calculation strings

**Example:**
```python
history = calc.get_history()
# Returns: ['5.0 + 3.0 = 8.0', '10.0 - 4.0 = 6.0']
```

#### `clear_history()`
Clears the calculation history.

**Returns:** None

**Example:**
```python
calc.clear_history()
```

## Error Handling

### ValueError
Raised when attempting to divide by zero.

```python
try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero
```

## History Format

The history is stored as a list of strings in the format:
```
"{operand1} {operator} {operand2} = {result}"
```

**Examples:**
- `"5.0 + 3.0 = 8.0"`
- `"10.0 - 4.0 = 6.0"`
- `"2.0 * 7.0 = 14.0"`
- `"15.0 / 3.0 = 5.0"`

## Usage Patterns

### Basic Calculator Usage
```python
from calculator import Calculator

calc = Calculator()

# Perform calculations
result1 = calc.addition(5, 3)
result2 = calc.multiply(4, 6)
result3 = calc.divide(20, 4)

# View history
print(calc.get_history())
```

### Error Handling Pattern
```python
from calculator import Calculator

calc = Calculator()

try:
    result = calc.divide(10, 0)
except ValueError as e:
    print(f"Division error: {e}")
```

### History Management
```python
from calculator import Calculator

calc = Calculator()

# Perform some calculations
calc.addition(1, 2)
calc.multiply(3, 4)

# View history
print("Current history:", calc.get_history())

# Clear history
calc.clear_history()
print("After clearing:", calc.get_history())
```

## Performance Notes

- All operations are performed in constant time O(1)
- History storage grows linearly with the number of operations
- Memory usage is minimal for typical use cases

## Thread Safety

The Calculator class is not thread-safe. If using in a multi-threaded environment, consider using appropriate synchronization mechanisms.