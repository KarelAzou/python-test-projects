# opening and reading the contents of a file is easy
# but we shouldn't forget to clise the file afterwars
import traceback
f = open("01_hello.py")
print(f.read())
f.close()

# better would be to close the file in finally:
try:
    f = open("01_hello.py")
    print(f.read())
finally:
    f.close()

# best is using a context manager "With"
with open("01_hello.py") as f:
    print(f.read())

# Big brain: including error handling
# best is using a context manager "With"
def read_file(path: str) -> str | None:
    try:
        with open(path) as f:
            print(f.read())
    except Exception as e:
        print(repr(e))
        # print(traceback.format_exc())  # with stacktrace
        raise e  # throw the error back up, so calling mehod can handle it.

# run read_file from mail as test scenario
if __name__ == "__main__":
    try:
        read_file("01_helloUNEXISTANT.py")
    except Exception as e:
        print(f"Oops, we seem to have an unhandled exception: \n {traceback.format_exc()}")  # with stacktrace
        pass #TODO log error

