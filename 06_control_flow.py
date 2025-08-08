# here we'll learn about multiple ways of controllign the flow of our code

# 1) Boolean expression
# 1.1) values and Fucntions
# 1.2) comparison operators
# 1.3) Logical operators and + or + execution order
# 1.4) Membership operators: in , not in
# 1.5) Identify operators:  is, is not
# 2) Conditional statements: if else elif
# 3) Inline If Statements + match Case

# ------------------------------------------------
# 1) Boolean expression
# ------------------------------------------------
# region Boolean expression

# 1.1) values and Fucntions
print(True)
print(False)
print(type(True))
# True
print(bool(True))  # returns , TRUE as there is a value!
print(bool(123))  # returns , TRUE as there is a value!
print(bool("abc"))  # returns , TRUE as there is a value!
# False
print(bool(""))  # returns FALSE due to havign an empty string
print(bool(None))  # returns FALSE due to having no value
print(bool(0))  # returns FALSE due to having no value

# any / all
email = ""
phone = "0470123456"
username = ""

print(any([email, phone, username]))  # return true if one is filled])
print(all([email, phone, username]))  # return true if all fields are filled

# isinstance
print(isinstance(123, int))  # returns True as 123 is an integer
print(isinstance(True, bool))  # returns False as True is a bool

# string checks
print("Hello".startswith("o"))  # returns False
print("Hello".endswith("o"))  # returns True

# ------------------------------------------------
# 1.2) comparison operators
#  - == Equal To
#  - != Not Equal
#  - <  Less than
#  - <= Less than or equal
#  - >  Greater than
#  - >= Greater than or equal

print(1 == 1)  # True
print(1 != 1)  # False
print(1 < 1)  # False
print(1 <= 1)  # True
print(2 > 1)  # True
print(1 >= 1)  # True

# chained comparison
print(1 < 4 < 6)  # True
print(7 < 4 < 10)  # False

print('1' == '1')  # True
print('1' != '1')  # False
print('21' < '3')  # TRUE !alphanumerical comparison 2 < 3
print(21 < 3)  # False !alphanumerical comparison 2 < 3
print('z' > 'a')  # True

# extra, be carefull with accents and caps!
print('é' > 'f')  # True accents somehow count as hgiher letters than non-accented letter,s probably due to Unicode ordering   E < e < É < é < ê
print(ord('E'))  # 69
print(ord('e'))  # 101
print(ord('É'))  # 201
print(ord('é'))  # 233
print(ord('ê'))  # 234

# ------------------------------------------------
# 1.3) Logical operators AND + OR + execution order

print(3 > 1 and 5 < 1)  # False
print(3 > 1 and 5 > 1)  # True

print(3 > 1 or 5 < 1)  # True
print(3 < 1 or 5 < 1)  # False

# exampe; ,check is memory or cpu usage is above the 90 % threshold
cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)

# not
print(not 3 > 1)  # False
name = ""
print(not name)  # True
print(not 0)  # True

# execution priority
# and has higher priority than or
print(5 == 5 or 8 > 5 and 6 < 4)  # True

# to have controll over the execution priority we use parenthesis
print((5 == 5 or 8 > 5) and 6 < 4)  # False

# execise:
# check if password is at least 8 chars lon and doesn to contain spaces.
password = "fdfddf54"
print(len(password) >= 8 and " " not in password)

# check if user's email is nopt empty, contains '@' and ends with '.com
user_email = "bob.sinclair@music.com"
print(bool(user_email) and '@' in user_email and user_email.endswith(".com"))

# check if username is a string, is not None and is longer than 5 chars
username = "bob the conquerer".strip
print(isinstance(username, str) and bool(username) and len(username) > 5)

# ------------------------------------------------
# 1.4) Membership operators
# in , not in

print('a' in 'Data')  # True
print('b' in 'Data')  # False
print('d' not in 'Data')  # True -> no lower d
print('Bob' in ['Bob', 'Bert', 'Pol', 'Pieter'])  # True

domain = "spam.com"
banned_domains = ["spam.com", "banned.com",
                  "malicious.com", "bot.net", "Trustteam.be"]
# False, as spam.com is  in the list of banned domains
print(domain not in banned_domains)

# ------------------------------------------------
# 1.5) Identify operators
# is, is not
# is : check if two objects are the same object in memory
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

a = b
print(a is b)

a = b = [3, 4, 5]
print(a is b)
print(a)
print(b)

b = [6, 7, 3]
print(a is b)
print(a)
print(b)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# when comparign to non use "is not none" it works with != , but since we're in data we might aswell use or SQL habit
email = None
print(email is not None and email != "")

# endregion

# ------------------------------------------------
# 2) Conditional statements: if else elif + nested if's
# ------------------------------------------------
# region Conditional statements


x = input("Please enter your score:")

try:
    val = int(x)

    if not (0 <= val <= 100):
        raise ValueError("Please enter a secore betyween 0 and 100")

    if val >= 90:
        x = input("did you score this on a project?(Y/N):")
        if x.upper() == "Y":
            print("Great project score!")
        else:
            print("Great exam score!")
    elif val >= 70:
        print("Good score!")
    else:
        print("Do better!")

    # Force a TypeError
    val + "string"

except ValueError as e:
    print(f"Invalid input: {str(e)}")
    # print(f"Invalid input {repr(e)}")
except Exception as e:
    print(f"Unexpected error: {repr(e)}")

# independant if statements

score = 50
submitted_project = False
if score >= 90:
    print("high score")
else:
    print("low score")

if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")


# exercise 1
# validate Quality and correctnees of email values
# - mustn ot be empty
# - must contain . and @
# - most contain exactly one @ symbol
# - must end with .com, .org or .net
# - must not be longer than 254 chars
# - must start and end with a letter or digit.


def validate_email(email_input: str) -> bool:
    """
    Validates an email address based on given rules.
    Returns True if valid, False otherwise.
    """
    email = str(email_input).strip().lower()
    # print(email)
    # email_input must not be empty
    if not bool(email):
        print("Email must not be empty")
    elif "." not in email or "@" not in email:
        print("Email must contain at least one '.' and '@'")
    elif email.count("@") != 1:
        print("Email must contain exactly 1 '@'")
    elif not email.endswith((".com", ".org", ".net")):
        print("Email must must end with .com, .org or .net")
    elif len(email) > 254:
        print(
            f"Email is to long, must be max 254 chars, curent length: {len(email)}")
        # half is redundant here: we can't fail on the last letter as we already make sure it ends with a valid domain
    elif not (email[0].isalnum() and email[-1].isalnum()):
        print(f"first or last char mut be a letter or a digit")
    else:
        print("valid email")
        return True
    return False


test_emails = [
    "john.doe@example.com",
    "john@example.org",
    "1cool@example.net",
    "@example.com",
    "example.com",
    "john@domain.xyz",
    "john.doe@domain.com.",
    "",
]

for e in test_emails:
    print(f"{e} -> {validate_email(e)} \n")

# endregion

# ------------------------------------------------
# 3) Inline If Statements + Match Case
# ------------------------------------------------
# region Inline If Statements
score = 85
result = "A" if score >= 90 else "F"
print(result)

# you can nest them, but don't misuse this for complex logic
result = ("A" if score >= 90
          else "B" if score >= 80
          else "F")
print(result)


# CASE statement
country = "Indaaaia"
match country:
    case "United States" | "USA":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unknown Country")

# endregion
