"""
compare 2 number x, y 
either x is greater or y
or both are equal
"""

def main() -> None:
    """
    get two number from user compare it
    and display which is greater 
    or equal
    """
    number_names = {
        "X": None,
        "Y": None, 
    }

    for num in number_names:
        number_names[num] = get_number(f"Enter the number ({num}) => ")

    if number_names["X"] > number_names["Y"]:
        print(f"{number_names["X"]} is greater then {number_names["Y"]}")
    elif number_names["Y"] > number_names["X"]:
        print(f"{number_names["Y"]} is greater then {number_names["X"]}")
    else:
        print("Both are equal..")

def get_number(prompt: str) -> float:
    """
    Prompt the user for a number until a valid float is entered.

    Args:
        prompt (str): A message displayed to the user when asking for input.

    Returns:
        float: The number input by the user, converted from a string.

    Raises:
        ValueError: Caught internally to handle invalid inputs (non-numeric entries).
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Not a number....")
            continue

if __name__ == "__main__":
    main()