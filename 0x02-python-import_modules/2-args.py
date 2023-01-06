#!/usr/bin/python3
import sys

argv = sys.argv[1:]

print(f"Number of argument(s): {len(argv)}", end="")
if len(argv) == 1:
    print(" argument", end="")
else:
    print("argument", end="")
print(":", end="\n\n")

for i in range(len(argv)):
    print(f"{i+1}: {argv[i]}", end="\n")
