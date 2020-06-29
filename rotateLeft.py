# Arrays: Left rotation
# Quiz URL:
# 	https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Quiz description:
# 	A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

# 	Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

d = 4
a = [3,7,1,8,0,5]
print(a)

def rotLeft(a, d):
	return a[d:len(a)] + a[0:d]

result = rotLeft(a,d)

print(result)