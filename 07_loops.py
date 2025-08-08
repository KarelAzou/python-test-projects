# here we'll continue to learn about  ways of controlling the flow of our code

# Loops
#    - for
#    - while
#    - break, continue, pass

# ------------------------------------------------
# 1) Loops
# ------------------------------------------------
# region Loops

for i in (1, 2, 3):  # using tuple
    print(f"round {i}")

for i in [1, 2, 3]:   # using list
    print(f"round {i}")

for i in "My short string":   # using string
    print(f"{i}")

for i in range(5):  # i automatically increments  0-4  EXCLUDING 5!
    print(i)

for i in range(1, 5):  # i automatically increments  1-4  EXCLUDING 5!
    print(i)

for i in range(0, 5, 2):  # i automatically increments in steps of 2  0-4  EXCLUDING 5!
    print(i)

# executing multiple lines in a loop
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current total:", total)

print("Final total:", total)

# cleanup data in loop however the orignal list remaisn as is
files = [" report.csv ", "DATA.csv ", " final.TXT"]
print(files)
for file in files:
    file = file.strip().lower().replace(".txt", ".csv")
    print(f"Processing {file}")

print(files)

# better:
files = [" report.csv ", "DATA.csv ", " final.TXT"]
print(files)
for i in range(len(files)):
    files[i] = files[i].strip().lower().replace(".txt", ".csv")
print(files)

# while loop, I couldn't fidn a way to auto-increment so it seems we always need to
i = 1
while i < 6:
    print(i)
    i = i + 1


# exercise 1
# print the 7 times talbe from 1-10 using a for loop
for i in range(10):
    print(f"7 x {i+1}) = {7*(i+1)}")

# exercise 1
# print a left aligned star pyramid with 6 rows
for i in range(6):
    print("*"*(i+1))

# endregion


# ------------------------------------------------
# 2) break, pass, continue
# ------------------------------------------------
# break: stop and exit the loop
# continue: return to the top and continue withthe rest of the list
# pass: used as placeholder, to replace later

# region bpc

# break:

names = ["John", "Yani", "Maria", "", "Manoli"]

for name in names:
    if name == "":
        print("empty value detected")
        break
    print(f"name = {name}")


# continue:
names = ["John", "Yani", "Maria", "", "Manoli"]
for name in names:
    if name == "":
        continue
    print(f"name = {name}")

# pass
names = ["John", "Yani", "Maria", "", "Manoli"]
for name in names:
    if name == "":
        pass  # todo: Handle empty value
    print(f"name = {name}")

# later I add logic to handle empty names
names = ["John", "Yani", "Maria", "", "Manoli"]
for name in names:
    if name == "":
        name = "Unknown"
    print(f"name = {name}")


# endregion
