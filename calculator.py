#!/usr/bin/env python3
"""
Simple Calculator Application
"""

class Calculator:
    """A simple calculator class with basic operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history."""
        return self.history
    
    def clear_history(self):
        """Clear calculation history."""
        self.history = []


def main():
    """Main function to run the calculator."""
    calc = Calculator()
    
    print("Simple Calculator")
    print("================")
    
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract") 
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Clear History")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '7':
            print("Goodbye!")
            break
        elif choice == '5':
            history = calc.get_history()
            if history:
                print("\nCalculation History:")
                for entry in history:
                    print(f"  {entry}")
            else:
                print("\nNo calculations yet.")
        elif choice == '6':
            calc.clear_history()
            print("\nHistory cleared.")
        elif choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                
                if choice == '1':
                    result = calc.add(a, b)
                    print(f"Result: {result}")
                elif choice == '2':
                    result = calc.subtract(a, b)
                    print(f"Result: {result}")
                elif choice == '3':
                    result = calc.multiply(a, b)
                    print(f"Result: {result}")
                elif choice == '4':
                    result = calc.divide(a, b)
                    print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
