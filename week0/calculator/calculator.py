"""
simple program to calculate math expression.
evaluate the expression and return result as float rounded to two decimal number
"""
from typing import Union

def main() -> None:
    """
    main function to get the expression from user and display result
    """
    while True:
        expression: str = input("Expressions or (q, quit) to exit => ")

        if expression.lower() in ["q", "quit"]:
            print("Exiting.....")
            break

        result: Union[float, Exception] = calculate(expression)

        if isinstance(result, ZeroDivisionError):
            print("Cannot Devide by 0")
        elif isinstance(result, (NameError, SyntaxError)):
            print("Invalid Input")
        else:
            print(f"Result => {result:.2f}")
            break

def calculate(exp: str) -> Union[float, Exception]:
    """
    evaluate math expression and return result as float and 
    Exception NameError, SyntaxError, ZeroDivisionError

    Args:
        exp (str): math expression e.g 1+2*4-5/3

    Returns:
         Union[float, Exception]: The result as a float, or an exception if there is an error.
    """
    try:
        return float(eval(exp))
    except (NameError, SyntaxError, ZeroDivisionError) as e:
        return e

if __name__ == "__main__":
    main()