#!/usr/bin/env python3.7
import argparse

# This creates the argument parser
parser = argparse.ArgumentParser(description='Read a file in reverse') 

# This creates a required argument, prompting the user for a filename
parser.add_argument('filename', help='the file to read') 

# This creates an optional parameter (--) for (--limit OR -l) which requires an int (type=int)
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read') 

# This creates an optional (--) version parameter (--version OR -v) which will perform an action of "version" if provided
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0') 

# This parses the arguments
args = parser.parse_args()

# This will print ALL arguments
print(args)

# You can then assign the arguments to varaibles and use them in your script
argfilename=args.filename
arglimit=args.limit

print(f"The filename specified was {argfilename}")
print(f"The limit specified was {arglimit}")
