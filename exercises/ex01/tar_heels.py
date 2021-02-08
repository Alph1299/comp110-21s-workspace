"""An exercise in remainders and boolean logic."""

__author__ = "730279779"


# Begin your solution here...
prompt: int = int(input("Please enter a number: "))

if (prompt % 2) == 0 and (prompt % 7) == 0:
    print("TAR HEELS")
else:
    if (prompt % 7) == 0:
        print("HEELS")
    else:
        if (prompt % 2) == 0:
            print("TAR")
        else:
            print("CAROLINA")