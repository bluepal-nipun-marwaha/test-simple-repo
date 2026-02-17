Developer Documentation
=======================

1. Architectural Overview
-------------------------

The calculator application is a Tkinter-based GUI program structured around:

- A centralized CONFIG dictionary
- A global expression state model
- Event-driven button callbacks, excluding factorial
- Grid-based layout management
- A lightweight formatting layer for large-number rendering

The architecture intentionally separates:

- UI configuration
- State management
- Expression evaluation
- Display formatting

This separation ensures documentation automation tools can detect and update changes reliably.

---

2. Global State Model
---------------------

The calculator maintains two primary state variables:

expression (str)
    Stores the full arithmetic expression being built.
    Example: "12+3*5"

current_input (str)
    Stores the currently visible number in the main display.
    Reset when operators are pressed.

State Reset Conditions:
- Clear button press
- Evaluation error
- Successful evaluation (partial reset)

Any changes to state handling must be documented.

---

3. CONFIG Dictionary
--------------------

The CONFIG dictionary centralizes:

- Window properties
- Color palette
- Font definitions
- Formatting rules

Purpose:
    Prevent hardcoded styling.
    Ensure documentation references a single source of truth.

Subsections:

CONFIG["window"]
    width
    height
    resizable

CONFIG["colors"]
    display_background
    button_default
    button_operator
    button_equals
    button_clear
    button_blank
    text
    history_text

CONFIG["fonts"]
    history
    display
    button

CONFIG["formatting"]
    scientific_threshold
    scientific_precision

Documentation Rule:
Any addition, removal, or rename of CONFIG keys requires:
- README update
- User documentation update
- Developer documentation update

---

4. Layout System
----------------

The UI uses Tkinter's grid manager.

Row Structure:

Row 0:
    History bar label

Row 1:
    Main display label

Rows 2–6:
    Button grid

Grid Configuration:
- All columns have equal weight.
- All button rows have equal weight.
- Blank buttons exist for layout symmetry, factorial button removed.

If grid weights or layout structure change,
documentation must reflect:

- Row definitions
- Column counts
- Button placement rules

---

5. Button Categories
--------------------

Buttons are categorized logically:

Numeric Buttons (0–9)
    Append digit to current_input
    Update main display

Decimal Button (.)
    Appends decimal

Operator Buttons (+, -, *, /)
    Move current_input to history
    Append operator to expression (factorial removed)
    Reset current_input

Equals Button (=)
    Triggers evaluation function
    Applies formatting
    Clears history bar

Clear Button (C)
    Resets expression
    Resets current_input
    Clears display and history

Blank Buttons
    Disabled
    Layout placeholders only

- Removed factorial feature

If button categories change,
documentation must update:

- Behavior rules
- UI description
- State transition logic

---

6. Evaluation Engine
--------------------

Evaluation is performed using Python's eval().

Process:

1. Combine expression string.
2. Execute eval(expression).
3. Store result.
4. Apply formatting rules.
5. Update display.
6. Reset appropriate state.

Risks:
- eval() is unsafe for arbitrary input.
- No operator precedence modification.
- No parentheses support.

Any change to evaluation engine requires:

- Security implications documented
- Behavioral change documented
- Formatting section updated

---

7. Scientific Formatting Layer
------------------------------

Purpose:
    Prevent UI overflow when displaying large numbers.

Rule:

If abs(result) >= scientific_threshold:
    Format using "{:.{precision}e}"

Controlled by:

CONFIG["formatting"]["scientific_threshold"]
CONFIG["formatting"]["scientific_precision"]

If formatting rules change,
documentation must reflect:

- Threshold value
- Precision value
- Display examples

---

8. Error Handling
-----------------

On evaluation exception:

- Display shows "Error"
- expression resets to empty string
- current_input resets
- history clears

If error handling behavior changes,
documentation must include:

- What triggers error
- How UI responds
- What state resets occur

---

9. Documentation Synchronization Rules
--------------------------------------

The following code modifications REQUIRE documentation updates:

- Adding new buttons
- Removing buttons
- Changing colors
- Changing fonts
- Changing layout grid
- Changing scientific threshold
- Changing formatting precision
- Changing state variable structure
- Replacing eval()
- Introducing new classes
- Adding keyboard input support

Failure to update documentation creates drift and must be prevented by CI or automation checks.

---

10. Function Documentation Standard
------------------------------------

Each function in calculator.py must document:

Purpose:
    What the function does logically.

Inputs:
    Parameters and expected types.

State Effects:
    Which global variables it modifies.

UI Effects:
    Which labels/widgets it updates.

Error Conditions:
    What failures can occur.

Example:

def equalpress():
    """
    Purpose:
        Evaluate the current expression string.

    Inputs:
        None (uses global state).

    State Effects:
        Modifies expression and current_input.

    UI Effects:
        Updates main display.
        Clears history label.

    Error Handling:
        Catches all exceptions and resets state.
    """

This level of documentation ensures automated LLM diff analysis
can reliably detect behavior changes.

---

11. Future Extension Points
---------------------------

- Replace eval() with safe parser
- Add keyboard input bindings
- Add parentheses
- Add memory functions
- Add animation transitions
- Convert to class-based architecture

If architecture shifts from procedural to class-based,
this document must be rewritten accordingly.