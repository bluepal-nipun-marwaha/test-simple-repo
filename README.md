# Custom Calculator (Tkinter)

## Overview

Custom Calculator is a desktop GUI calculator built using Python and Tkinter.  
It supports arithmetic operations, scientific notation formatting for large numbers, and a dynamic history bar UI.

This project is designed with maintainability and automated documentation updates in mind.

---

## Features

- Basic arithmetic operations (+, -, *, /)
- Scientific notation formatting for large results (>= 1e9)
- Dynamic history bar that displays the previous expression
- Dark-themed UI
- Clear (C) functionality
- Error handling for invalid expressions

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

---

## Installation

### Requirements

- Python 3.9+

### Run

```bash
python calculator.py
```

---

## Known Limitations

- Uses Python `eval()` for expression evaluation (not secure for untrusted input).
- Does not support parentheses.
- Does not support memory functions.
- No keyboard input support (button-only interaction).

---

## Project Structure

```
calculator.py
```

---

## Documentation Automation

This repository is integrated with an automated documentation update system.

Any code change must be reflected in:

- README.md
- USER_GUIDE.md
- ARCHITECTURE.md

Changes affecting UI behavior, logic flow, state variables, formatting rules, or evaluation logic must update the corresponding documentation sections.

---

## Versioning

Versioning follows semantic versioning principles:

MAJOR.MINOR.PATCH

- MAJOR → Breaking changes
- MINOR → Feature additions
- PATCH → Bug fixes

---

## License

MIT