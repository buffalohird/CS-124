import sys
from collections import defaultdict

string1, string2 = raw_input().split()
if len(string1) != len(string2):
	print False
	sys.exit()
	
hashTable = defaultdict(int)

for char in string1:
		hashTable[char] += 1

for char in string2:
		hashTable[char] -= 1


for key, value in hashTable.iteritems():
	if value != 0:
		print False
		sys.exit()

print True