# Concert seats
# Quiz URL:
# 	https://edabit.com/challenge/xbjDMxzpFcsAWKp97
# Quiz description:
# Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.
# Everyone can see the front-stage in the example below:
# FRONT STAGE
# [[1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 5, 4, 4],
# [6, 6, 7, 6, 5, 5]]
# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.

def can_see_stage(seats):
	list1 = []
	for key, val in enumerate(seats[0]):
		list0 = []
		for i in range(len(seats)):
			list0.append(seats[i][key])

		list1.append(list0)

	for key, i in enumerate(list1):
		for j in range(len(i) - 1):
			if list1[key][j] >= list1[key][j+1]:
				return False

	return True

seats = [
	[1, 2, 3, 2, 1, 1],
	[2, 4, 4, 3, 2, 3],
	[5, 5, 5, 5, 4, 4],
	[6, 6, 7, 6, 5, 5]
]

print(can_see_stage(seats))