#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    '''argument = "argument:" if len(argv) == 2 else
    ("argument." if len(argv) == 1 else "arguments:")'''
    if len(argv) == 2:
        argument = "argument:"
    elif len(argv) == 1:
        argument = "arguments."
    else:
        argument = "arguments:"

    print(len(argv) - 1, "{}".format(argument))
    for i in range(1, len(argv)):
        print("{}:".format(i), str(argv[i]))
