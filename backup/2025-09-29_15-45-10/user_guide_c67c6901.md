# Backup of docs/user_guide.md
# Created: 2025-09-29T15:45:29.177194
# Commit: c67c6901c6ced2c07a4ab7e749f485b62285df1d
# Message: Create backup folder: 2025-09-29_15-45-00
# Author: Nipun Marwaha
# Original file: docs/user_guide.md
# Backup folder: backup/2025-09-29_15-45-10
# Full documentation backup

---

# Calculator User Guide

## Overview
The Simple Calculator is a Python application that provides basic mathematical operations with a history tracking feature.

## Features
- **Basic Operations**: Addition, subtraction, multiplication, and division
- **History Tracking**: Keeps a record of all calculations performed
- **Error Handling**: Prevents division by zero and handles invalid inputs
- **Interactive Menu**: Easy-to-use command-line interface

## Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/bluepal-nipun-marwaha/test-simple-repo.git
   cd test-simple-repo
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Calculator
```bash
python calculator.py
```

### Available Operations

#### 1. Addition
- Select option `1` from the menu
- Enter two numbers
- The calculator will add them and display the result

#### 2. Subtraction
- Select option `2` from the menu
- Enter two numbers
- The calculator will subtract the second number from the first

#### 3. Multiplication
- Select option `3` from the menu
- Enter two numbers
- The calculator will multiply them

#### 4. Division
- Select option `4` from the menu
- Enter two numbers
- The calculator will divide the first number by the second
- **Note**: Division by zero is not allowed

#### 5. View History
- Select option `5` from the menu
- View all previous calculations

#### 6. Clear History
- Select option `6` from the menu
- Clear all calculation history

#### 7. Exit
- Select option `7` from the menu
- Exit the calculator

## Examples

### Basic Usage
```
Simple Calculator
================

Options:
1. Addition
2. Subtract
3. Multiply
4. Divide
5. Show History
6. Clear History
7. Exit

Enter your choice (1-7): 1
Enter first number: 5
Enter second number: 3
Result: 8.0
```

### History Feature
```
Enter your choice (1-7): 5

Calculation History:
  5.0 + 3.0 = 8.0
  10.0 - 4.0 = 6.0
  2.0 * 7.0 = 14.0
```

## Error Handling

### Division by Zero
```
Enter your choice (1-7): 4
Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero
```

### Invalid Input
```
Enter your choice (1-7): 1
Enter first number: abc
Error: could not convert string to float: 'abc'
```

## Programming Interface

### Using the Calculator Class
```python
from calculator import Calculator

# Create calculator instance
calc = Calculator()

# Perform operations
result = calc.addition(5, 3)        # Returns 8
result = calc.subtract(10, 4)  # Returns 6
result = calc.multiply(2, 7)  # Returns 14
result = calc.divide(15, 3)   # Returns 5

# Access history
history = calc.get_history()
print(history)  # ['5 + 3 = 8', '10 - 4 = 6', '2 * 7 = 14', '15 / 3 = 5']

# Clear history
calc.clear_history()
```

## Troubleshooting

### Common Issues

1. **"Cannot divide by zero"**
   - Solution: Use a non-zero divisor

2. **"could not convert string to float"**
   - Solution: Enter valid numbers only

3. **"Invalid choice"**
   - Solution: Select options 1-7 only

## License
MIT License

## Contributing
Feel free to submit issues and enhancement requests!
