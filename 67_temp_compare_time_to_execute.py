
import time

myword = "ejHssdrt4t4swg53xdwg4wdqg5314rg431w43gdth4x3gd4fswd54fgFDFsdsdfgr5sr(§eèe(§dfhdf!èfddj5431"

# first block ---------------------------------
start = time.perf_counter()  # more precise than time.time()
# Code you want to measure
valid = True
if myword.lower() == myword:
    valid = False
if myword.upper() == myword:
    valid = False
end = time.perf_counter()

print(f"Execution time: {end - start:.6f} seconds")

# second block ---------------------------------
start2 = time.perf_counter()  # more precise than time.time()
# Code you want to measure
valid = any(c.isupper() for c in myword) and any(c.islower()for c in myword)

end2 = time.perf_counter()

print(f"Execution time: {end2 - start2:.6f} seconds")
