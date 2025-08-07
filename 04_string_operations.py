import re
import unicodedata
from datetime import datetime, date

# --------------------
# Operations on strings
# --------------------
# As a data engineer we'll often be cleanign up string data

# declaring or re-typing variables to string
myint = 10
mystring = str(myint)
print("myint", myint)
print("mystring", mystring)
print("type mystring", type(mystring))

# ----------------------------------------------------------------
# len function ( obvs)
print("len mystring", len('    ' + mystring))  # Length of string

# ----------------------------------------------------------------
# Math
text = """
Python is easy to learn
Python is powerfull
Many people love python
is this actually Pythön ? 
"""

print("Python (CS) appears : ", text.count(
    "Python"), "times.")  # Count of substring
print("Python (CI) appears : ", text.upper().count(
    "Python".upper()), "times.")  # Count of substring

# ----------------------------------------------------------------
# case insensitive search


def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


accent_insensitive_text = remove_accents(text.lower())
accent_insensitive_word = remove_accents("python".lower())

print(accent_insensitive_text)
print("Python (accent & case insensitive) appears : ",
      accent_insensitive_text.count(accent_insensitive_word), "times.")

# ----------------------------------------------------------------
# replace + translate
print("replace  '/' with '-' in \"2026/01/01\":", "2026/01/01".replace("/", "-"))

phone = "0/175-1234-46"
print(phone.replace("-", "").replace("/", ""))  # Remove dashes and slashes

# replace multiple chars  in one go:
phone = "0/175-(12)34-46"
remove_chars = "/-()"
# translate method: replace chars for var 1 bij chars from var 2 , and remove al char's in var 3 [remove_chars]
clean_phone = phone.translate(str.maketrans('173', 'ITE', remove_chars))
print(clean_phone)
# translate method: replace chars for var 1 bij chars from var 2 , and remove al char's in var 3 [remove_chars]
clean_phone = phone.translate(str.maketrans('', '', remove_chars))
print(clean_phone)

# ----------------------------------------------------------------
# concat strings
first_name = "John"
last_name = "Doe"
last_name = first_name + " " + last_name  # Concatenate strings
print("Full name:", last_name)


# ----------------------------------------------------------------
# very usefull!
# f-string: put variables and dta in your strign without worrying about the datatypes

birthdate_str = "1988-06-12"
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
# birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
today = date.today()

age = today.year - birthdate.year - \
    ((today.month, today.day) < (birthdate.month, birthdate.day))
# f-string for formatting
print(f"Full name: {first_name} {last_name} ,age: {age}")


print(f"2 + 3 = {2+3}")
# double them up to print them in f strings
print(f"PRINTING CURLY BRACKETS  = {{}}")

# ----------------------------------------------------------------
# split

mydelimitedstring = "Alex-10-Brussels"
print(mydelimitedstring.split("-"))  # Split string by delimiter

split_values_list = mydelimitedstring.split("-")
print("length of list", len(split_values_list))
for i, value in enumerate(split_values_list):
    print(f"Value {i}:", value)  # Print each value with its index
    print(f"Value {i}: {value}")  # Print each value with its index
# OR
for i in range(len(split_values_list)):
    # Print each value with its index
    print(f"Value {i}:", split_values_list[i])
# OR manual
print("split_values_list[0]", split_values_list[0])  # Access first value
print("split_values_list[1]", split_values_list[1])  # Access second value
print("split_values_list[2]", split_values_list[2])  # Access third value

try:
    # Access FOURTH  value ( which fails)
    print("split_values_list[3]", split_values_list[3])
except IndexError as e:
    print("Error:", e)  # Handle the error gracefully
finally:
    print("This part of our code failed as intended, due to reading an index in a list that has fewer items than the index we tried to access.")


# ----------------------------------------------------------------
# multiply
#
print("Ha" * 3)
print("-" * 100)

# ----------------------------------------------------------------
# indexes and slicing in strings
# first chars has index zero
# last char has index (lengeth - 1 ) OR  -1

first_name = 'Karel'
print("first_name[0]", first_name[0])  # First character
print("first_name[1]", first_name[-1])  # Last character
index_last_char = len(first_name) - 1  # index of Last character
print(f"first_name[{index_last_char}]",
      first_name[index_last_char])  # Last character

# slicing
# [start:end:(step)] start is encluded, end is excluded
print("first_name[0-3]", first_name[0:3])  # get 3rd char from the end
# get all even chars ( 0,4,6,...)
print("first_name[0:len(first_name):2]", first_name[0:len(first_name):2])
# get all odd chars ( 1,3,5,...)
print("first_name[1:end:2]", first_name[1:len(first_name):2])
# even better without specyfying end
print("first_name[0::2]", first_name[0::2])  # get all even chars ( 0,4,6,...)
print("first_name[1::2]", first_name[1::2])  # get all odd chars ( 1,3,5,...)

# extract parts of date with string slicing
my_date = "2025-08-07"
# first the year
year = my_date[0:my_date.index("-")]  # Get year from date string
print("year", year)

print(my_date.index("-"))
print(my_date.index("-", 2))

index_first_dash = my_date.index("-")
index_second_dash = my_date.index("-", index_first_dash + 1)

# Get year from date string
month = my_date[index_first_dash+1:index_second_dash]
print("month", month)

day = my_date[index_second_dash+1:]  # Get year from date string
print("day", day)


# ----------------------------------------------------------------
# string cleaning with strip

dirty_string = "  Hello, World!     \t\n"
# Remove leading and trailing whitespace
L_cleaned_string = dirty_string.lstrip()
print("L_cleaned_string:", L_cleaned_string)
# Remove leading and trailing whitespace including tabs and linebreaks
R_cleaned_string = dirty_string.rstrip()
print("R_cleaned_string:", R_cleaned_string)
cleaned_string = dirty_string.strip()  # Remove leading and trailing whitespace
print("Cleaned string:", cleaned_string)

dirty_string = "## abx##"
# Remove leading and trailing characters
cleaned_string = dirty_string.strip("#")
print("Cleaned string:", cleaned_string)  # Output: "abx"

# ----------------------------------------------------------------

# exercise:
dirty_string = "968-Maria, ( D@t@ Engineer );; 27y  "
# should become name: maria | role: data engineer | age: 27

# remove everything before and including the first dash
index_temp = dirty_string.find("-")  # Find the index of the first dash
intermediate_string = dirty_string[index_temp+1:]
# print(f"intermediate_string {intermediate_string}")

# Extract name
string_name = intermediate_string.split(",")[0].strip()
# print(f"string_name {string_name}")

# extrtact everythign after the first comma so when can later split it into role and age
intermediate_string = intermediate_string.split(",")[1]
string_role = intermediate_string.split(";;")[0].translate(str.maketrans("@", "a", "()")).strip()  # Extract role + replace @ by a and remove brackets
string_age = intermediate_string.split(";;")[1].replace("y", "").strip()  # Extract age
# print(f"string_role {string_role}")
# print(f"string_age {string_age}")

# now concat and print the result in the requested format
cleaned_string = f"name: {string_name.lower()} | role: {string_role.lower()} | age: {string_age}"
print(dirty_string)
print(cleaned_string)


# ----------------------------------------------------------------
# string ,in startswith , endwith
my_date = "2025-Feb-07"

print("my_date startswith \"2025\" ", my_date.startswith("2025"))  # does my_date start with 2025
# does my_date end with 30
print("my_date endswith \"30\" ", my_date.endswith("30"))
# does my_date contains "feb" case insensitive, give index
print("find Feb' in my_date:", my_date.upper().find("Feb".upper()) >= 0)


# ----------------------------------------------------------------
# check valid email (simple)
email = "bob@test.vlaanderen.be"
print("Validate email 1", "@" in email)

# check valid email (swith regular expression)
valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
print("Valid email address detected." if valid else "Invalid email address detected.")

# ----------------------------------------------------------------
# string validation
country = "USA"
print(country.isalpha())  # Check if country name contains only letters

phone = "01761234587"
print(phone.isalpha())  # Check if phone name contains only letters
print(phone.isnumeric())  # Check if phone name contains only numbers