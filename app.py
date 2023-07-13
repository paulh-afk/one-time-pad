import sys

# e = encrypt / d = decrypt

arg = sys.argv[1]

if arg == "-e" or arg == "-d":
    pass
else:
    exit("Error not valid arg, the valid format is [-d | -e] [key] [message]")
