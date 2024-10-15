"""
This script prompts the user for their name and greets them with a customizable message.
It contains three functions:
- main(): Orchestrates the user input and greeting process.
- get_name(): Retrieves and formats the user's name.
- greet(): Prints a greeting message.

Usage:
    Run the script and follow the prompt to enter your name. The program will greet you.
"""

def main() -> None:
    """
    Main function to get the user's name and greet them.

    It first retrieves the user's name using the get_name() function
    and then greets the user by calling the greet() function.
    """
    name: str = get_name("What's your name? ")
    greet(name)

def greet(name: str, greet_with: str="Hello") -> None:
    """
    Prints a greeting message to the user.

    Args:
        name (str): The name of the person to greet.
        greet_with (str, optional): The greeting word to use. Defaults to "Hello".

    Returns:
        None
    """
    print(f"{greet_with} {name}")

def get_name(prompt: str="Name: ") -> str:
    """
    Prompts the user for their name and formats it.

    Args:
        prompt (str, optional): The prompt to display when asking for the name. Defaults to "Name: ".

    Returns:
        str: The user's name, formatted with the first letter capitalized and leading/trailing spaces removed.
    """
    name: str = input(prompt)
    name = name.title().strip()
    return name

if __name__ == "__main__":
    main()
