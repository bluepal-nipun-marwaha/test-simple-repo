# Custom Calculator (Tkinter)

## Overview

Custom Calculator is a desktop GUI calculator built using Python and Tkinter.

It supports:

- Basic arithmetic operations
- Scientific notation formatting for large numbers
- A dynamic history bar UI
- Centralized configuration for styling and formatting

The application uses a centralized `CONFIG` architecture to define UI styling, formatting rules, and fonts for improved maintainability and automated documentation updates.

---

## Features

- Basic arithmetic operations (`+`, `-`, `*`, `/`)
- Scientific notation formatting for large results (`>= 1e9`)
- Dynamic history bar that displays the previous expression
- Centralized configuration (window, colors, fonts, formatting)
- Bold, high-visibility UI typography
- Equal-sized responsive button grid
- Clear (`C`) functionality
- Error handling for invalid expressions
- Additional blank button row for layout extensibility

---

## UI Behavior Summary

- When a number is entered, it appears in the main display.
- When an operator is pressed:
  - The current number + operator moves to the history bar.
  - The main display clears for the next number.
- When "=" is pressed:
  - The full expression is evaluated.
  - The result is shown in the main display.
  - The history bar clears.
- Large numbers are automatically formatted into scientific notation.
- All buttons are equal size using weighted grid configuration.
- Text is bold and larger for readability.

---

## Installation

### Requirements

- Python 3.9+

### Run

    python calculator.py

---

## Project Structure

    calculator.py
    README.md
    user_documentation.txt
    dev_documentation.rst

---

## Known Limitations

- Uses Python `eval()` for expression evaluation (not secure for untrusted input).
- Does not support parentheses.
- Does not support memory functions.
- No keyboard input support (button-only interaction).
- No validation preventing multiple decimal points.

---

## Documentation Automation Requirements

Documentation must be updated whenever:

- Window size changes
- Font configuration changes
- Color configuration changes
- Button layout changes
- Formatting rules change
- State logic changes
- Evaluation logic changes

All three documentation files must remain synchronized.

---

## Versioning

Versioning follows semantic versioning:

MAJOR.MINOR.PATCH

- MAJOR → Breaking changes
- MINOR → Feature additions
- PATCH → Bug fixes

---

## License

MIT