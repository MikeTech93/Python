#!/usr/bin/env python3.7

import argparse

parser = argparse.ArgumentParser(description='Search for words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search for in words')

args = parser.parse_args()
snippet = args.snippet.lower()

with open('/usr/share/dict/words') as f:
    words = f.readlines()

# Everything commented out below can be replaced by the single print line below using List Comprehensions

#matches = []
#
#for word in words:
#    if snippet in word.lower():
#        matches.append(word)

#print(matches)


print([word.strip() for word in words if snippet in word.lower()])
