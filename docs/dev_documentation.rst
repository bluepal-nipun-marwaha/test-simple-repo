# Developer Technical Specification

## 1. Purpose

This document defines the complete internal behavior, state model, UI contract, evaluation rules, and update triggers of the Custom Calculator application.

This document acts as the authoritative technical contract for:

- Code behavior
- UI state transitions
- Formatting logic
- Error handling
- Documentation update validation

If implementation changes violate this document, the documentation must be updated accordingly.

---

# 2. Application Architecture

The application follows an event-driven architecture using Tkinter.

Core components:

- Root window
- History label (tk.Label)
- Main display (tk.Entry)
- Button grid (tk.Button)
- State variables
- Event handlers

---

# 3. State Model

The calculator operates using two primary internal state variables.

## 3.1 expression

Type: str  
Initial Value: ""  

Purpose:
Stores the full arithmetic expression being constructed prior to evaluation.

Example:
```
"1111111*5555555"
```

Invariant:
- Contains only numeric characters, ".", and operators (+ - * /)
- Does not contain whitespace
- Must not contain trailing operator when "=" is pressed

---

## 3.2 current_input

Type: str  
Initial Value: ""  

Purpose:
Stores the number currently being entered by the user.

Invariant:
- Contains only numeric characters and "."
- Cleared when operator is pressed
- Replaced with formatted result after "="

---

# 4. Display Variables

## 4.1 equation (tk.StringVar)

Represents the main display value.

Must always reflect:
- current_input OR
- formatted result OR
- "Error"

---

## 4.2 history_var (tk.StringVar)

Represents the history bar content.

Must reflect:
- current_input + operator (after operator press)
- Empty after "="
- Empty after "C"

---

# 5. UI Contract

## 5.1 Window Configuration

- Size: 350x500
- Resizable: False
- Background color: #1e1e1e

If modified, documentation must update Section 5.

---

## 5.2 Color Constants

Defined constants:

BG_COLOR = "#1e1e1e"  
DISPLAY_COLOR = "#252526"  
BTN_COLOR = "#333333"  
OPERATOR_COLOR = "#ff9500"  
EQUAL_COLOR = "#28a745"  
CLEAR_COLOR = "#d9534f"  
TEXT_COLOR = "white"  
HISTORY_TEXT_COLOR = "#888888"

If any constant changes, documentation must update color specification.

---

# 6. Event Handlers

## 6.1 press(key)

Behavior:

IF key is numeric or ".":
- Append to current_input
- Update equation display
- Do NOT modify expression

IF key is operator:
- Append current_input to expression
- Append operator to expression
- Update history_var to show appended value
- Clear equation display
- Reset current_input

Edge Cases:
- Operator press when current_input is empty → no action
- Double operator press → prevented by current_input guard

---

## 6.2 equalpress()

Behavior:

1. Append current_input to expression
2. Evaluate expression using eval()
3. Apply scientific formatting rule (Section 7)
4. Set equation to formatted result
5. Clear history_var
6. Reset expression
7. Set current_input to formatted result

Edge Cases:
- Division by zero
- Malformed expression
- Empty expression

Failure Behavior:
- Display "Error"
- Reset expression
- Reset current_input
- Clear history

---

## 6.3 clear()

Behavior:
- expression = ""
- current_input = ""
- equation = ""
- history_var = ""

Must restore application to initial state.

---

# 7. Scientific Notation Rule

Condition:
```
abs(result) >= 1e9
```

Formatting:
```
"{:.6e}".format(result)
```

This rule must remain consistent across:

- equalpress()
- Any future result formatting logic

If threshold changes, update documentation.

---

# 8. Evaluation Engine

Current implementation uses:

```
eval(expression)
```

Security Implications:
- Executes arbitrary Python expressions.
- Safe only because input is restricted to button presses.

If evaluation logic changes (e.g., replaced with parser), update:

- Section 8
- Section 6.2
- Known limitations
- Security notes

---

# 9. State Transition Matrix

| Action | expression | current_input | history | display |
|--------|------------|--------------|----------|----------|
| Enter digit | unchanged | append digit | unchanged | show current_input |
| Press operator | append input+op | reset | show input+op | cleared |
| Press "=" | evaluated then reset | result | cleared | show result |
| Press "C" | reset | reset | cleared | cleared |

Any behavioral change must update this table.

---

# 10. Failure Modes

Defined failure modes:

- ZeroDivisionError
- SyntaxError
- Invalid eval()

On failure:
- Display = "Error"
- All state reset

---

# 11. Invariants

The following must always be true:

1. expression never contains whitespace
2. expression never ends with operator before evaluation
3. current_input contains no operators
4. history_var must never display result
5. display must never show raw unformatted large result when formatting rule applies

Violation requires documentation update.

---

# 12. Documentation Update Triggers

Documentation must be updated if:

- New buttons added
- Buttons removed
- Color constants changed
- Evaluation logic changed
- State variables renamed
- Scientific threshold changed
- Formatting precision changed
- Parentheses support added
- Keyboard input added
- Layout modified
- Window size changed
- State machine refactored
- Double operator behavior modified
- Error handling logic changed

Failure to update documentation after such change results in documentation inconsistency.

---

# 13. Edge Case Coverage Checklist

When reviewing a diff, verify:

- State variables modified?
- Operator logic changed?
- Evaluation engine changed?
- Formatting logic changed?
- UI layout changed?
- Color constants changed?
- Guard conditions changed?
- Reset behavior changed?

If yes → update relevant sections.

---

# 14. Automation Compatibility Notes

This document is structured to:

- Allow section-level patching
- Map variable names deterministically
- Map formatting rules deterministically
- Map color constants deterministically
- Provide diff-detection anchors

LLM-based documentation updates must preserve:

- Section headers
- Variable naming
- Rule definitions
- Threshold definitions
- Invariants

---
