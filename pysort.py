import sys

with open(sys.argv[1], "r") as f:
    lines = [int(l) for l in f if l.strip().isdigit()]
    lines.sort()
    print(*lines, sep = "\n") 
