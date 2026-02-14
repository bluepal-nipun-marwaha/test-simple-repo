# Calculator Application Documentation

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Calculator Operations](#calculator-operations)
6. [Menu Options](#menu-options)
7. [Error Handling](#error-handling)
8. [History Management](#history-management)
9. [Examples](#examples)
10. [Testing](#testing)

## Overview

The Calculator Application is a Python-based command-line calculator that provides basic arithmetic operations with a user-friendly interactive interface. The application includes calculation history tracking and comprehensive error handling.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Power/exponentiation, factorial
- **Calculation History**: Track and view all previous calculations
- **Error Handling**: Graceful handling of invalid inputs and division by zero
- **Interactive Menu**: Easy-to-use command-line interface
- **History Management**: Clear history functionality

## Installation

### Prerequisites
- Python 3.6 or higher
- No additional dependencies required

### Setup
1. Download the `calculator.py` file
2. Ensure Python is installed on your system
3. Run the application using: `python calculator.py`

## Usage

### Starting the Application
```bash
python calculator.py
```

### Basic Workflow
1. Run the application
2. Select an operation from the menu (1-9)
3. Enter the required numbers when prompted
   - For factorial (option 6) the application expects an integer input
   - For other arithmetic options it accepts floating-point numbers
4. View the result
5. Optionally view or clear calculation history
6. Exit when finished

## Calculator Operations

### Core Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `addition(a, b)` | Adds two numbers | `a`, `b` (numbers) | Sum of a and b |
| `subtract(a, b)` | Subtracts second number from first | `a`, `b` (numbers) | Difference of a and b |
| `multiply(a, b)` | Multiplies two numbers | `a`, `b` (numbers) | Product of a and b |
| `divide(a, b)` | Divides first number by second | `a`, `b` (numbers) | Quotient of a and b |
| `power(a, b)` | Raises a to the power of b | `a`, `b` (numbers) | a raised to power b |
| `factorial(n)` | Factorial of an integer n | `n` (integer) | n! |

### History Methods

| Method | Description | Parameters | Returns |
|--------|-------------|------------|---------|
| `get_history()` | Retrieves calculation history | None | List of calculation strings |
| `clear_history()` | Clears all calculation history | None | None |

## Menu Options

The interactive menu presented by the `main()` function uses the following options (matching the implementation in `calculator.py`):

1. Subtract
   - Function: Performs subtraction of two numbers
   - Input: Two floating-point numbers
   - Output: Difference of the numbers
   - Example: `10.0 - 4.5 = 5.5`

2. Addition
   - Function: Performs addition of two numbers
   - Input: Two floating-point numbers
   - Output: Sum of the numbers
   - Example: `5.5 + 3.2 = 8.7`

3. Multiply
   - Function: Performs multiplication of two numbers
   - Input: Two floating-point numbers
   - Output: Product of the numbers
   - Example: `3.0 * 4.0 = 12.0`

4. Divide
   - Function: Performs division of two numbers
   - Input: Two floating-point numbers
   - Output: Quotient of the numbers
   - Error Handling: Raises `ValueError` for division by zero
   - Example: `15.0 / 3.0 = 5.0`

5. Power (Exponentiation)
   - Function: Raises first number to the power of second number
   - Input: Two floating-point numbers
   - Output: Result of exponentiation
   - Example: `2.0 ^ 3.0 = 8.0`

6. Factorial (n!)
   - Function: Calculates factorial of an integer
   - Input: Single integer (the program reads an integer for this option)
   - Output: n!
   - Error Handling: Raises `ValueError` for negative or non-integer input
   - Example: `5! = 120`

7. Show History
   - Function: Displays all previous calculations
   - Input: None
   - Output: List of formatted calculation strings
   - Format: `"number1 operation number2 = result"` (or `"n! = result"` for factorial)

8. Clear History
   - Function: Removes all calculation history
   - Input: None
   - Output: Confirmation message
   - Effect: History list becomes empty

9. Exit
   - Function: Terminates the application
   - Input: None
   - Output: Goodbye message
   - Effect: Application closes

> Note: The numeric menu mapping above matches the code in `calculator.py` (which prints options in that order and expects choices 1–9).

## Error Handling

### Division by Zero
- **Error**: `ValueError: Cannot divide by zero`
- **Trigger**: When attempting to divide by 0
- **Handling**: Graceful error message display
- **Recovery**: User can try again with different input

### Invalid Input
- **Error**: `ValueError` for non-numeric input or invalid factorial input
- **Trigger**: When entering non-numeric values or non-integer/negative values for factorial
- **Handling**: Error message display
- **Recovery**: User prompted to enter valid numbers

## History Management

### History Format
Each calculation is stored as a formatted string:
- Addition: `"5.0 + 3.0 = 8.0"`
- Subtraction: `"10.0 - 4.0 = 6.0"`
- Multiplication: `"2.0 * 3.0 = 6.0"`
- Division: `"15.0 / 3.0 = 5.0"`
- Power: `"2.0 ^ 3.0 = 8.0"`
- Factorial: `"5! = 120"`

### History Features
- **Automatic Logging**: All operations are automatically recorded
- **Session-Scoped**: History maintained throughout the session
- **Viewable**: Can be displayed at any time
- **Clearable**: Can be reset to empty state

## Examples

### Example Session
```
Simple Calculator
================

Options:
1. Subtract
2. Addition
3. Multiply
4. Divide
5. Power (a^b)
6. Factorial (n!)
7. Show History
8. Clear History
9. Exit

Enter your choice (1-9): 2
Enter first number: 5.5
Enter second number: 3.2
Result: 8.7

Enter your choice (1-9): 7

Calculation History:
  5.5 + 3.2 = 8.7

Enter your choice (1-9): 9
Goodbye!
```

### Calculation Examples
- **Addition**: `10 + 5 = 15`
- **Subtraction**: `20 - 8 = 12`
- **Multiplication**: `4 * 6 = 24`
- **Division**: `18 / 3 = 6.0`
- **Power**: `2 ^ 4 = 16`
- **Factorial**: `5! = 120`

## Testing

### Running Tests
This repository does not include unit tests for the calculator. If you add tests, you can run them with `python -m unittest`.

### Test Coverage
No tests are present in the current repository snapshot.

---

*This documentation covers the Calculator Application version 1.0*
