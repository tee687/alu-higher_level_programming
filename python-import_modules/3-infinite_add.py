#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    # sys.argv[1:] skips the script name (argv[0])
    for arg in sys.argv[1:]:
        total += int(arg)

    print("{}".format(total))
