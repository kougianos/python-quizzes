# Merge the Tools
# Quiz URL:
# 	https://www.hackerrank.com/challenges/merge-the-tools/problem
import collections

def merge_the_tools(string, k):

	parts = [string[i:i+k] for i in range(0, len(string), k)]
	for part in parts:
		part = collections.OrderedDict.fromkeys(part)
		stringToPrint = ""
		for x in part:
			stringToPrint += x
		print(stringToPrint)


merge_the_tools("ABCADYUIOY", 5)