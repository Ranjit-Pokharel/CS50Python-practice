"""
This script evaluates simple mathematical expressions consisting of two operands and one operator.
The user is prompted to input an expression, which is then calculated and the result is displayed.

Supported operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

Usage:
    Run the script and input an expression in the format: "Num1 Operation Num2" no space in between.
    The result will be displayed as a floating-point number rounded to two decimal places.
    example "1+2" => 3.00
"""

def main() -> None:
    """
    Main function that orchestrates the input and calculation process.

    It prompts the user for a mathematical expression, calculates the result using the
    calculate_result function, and prints the result formatted to two decimal places.
    """
    expression: str = get_expression("Expression => ")
    result: float = calculate_result(expression)
    print(f"{result:.2f}")

def calculate_result(expressions: str) -> float:
    """
    Calculates the result of a mathematical expression.

    Args:
        expressions (str): A string containing two operands and an operator (e.g., "1+2").

    Returns:
        float: The result of the calculation. If division by zero occurs, returns NaN.
    """
    num1, operation, num2 = expressions
    num1 = int(num1)
    num2 = int(num2)

    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    else:
        try:
            return num1 / num2
        except ZeroDivisionError:
            return float("nan")

def get_expression(prompt: str="Expression: ") -> str:
    """
    Prompts the user to input a mathematical expression and validates the input.

    The input must be in the format of two digits separated by an operator.

    Args:
        prompt (str, optional): The prompt to display when asking for the expression. Defaults to "Expression: ".

    Returns:
        str: A valid mathematical expression containing two operands and one operator.

    Raises:
        ValueError: If the input format is incorrect.
    """
    operation: list = [
        "+",
        "-",
        "*",
        "/",
    ]
    while True:
        expressions: str = input(prompt)
        try:
            if len(expressions) != 3:
                raise ValueError
            for expression in expressions:
                if not (expression.isdigit() or expression in operation):
                    raise ValueError
        except ValueError:
            continue
        return expressions
  
    
if __name__ == "__main__":
    main()