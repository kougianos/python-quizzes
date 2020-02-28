# Length of Sorting Cycle
# Quiz URL:
# 	https://edabit.com/challenge/K9MuSPs9W4zCJq6EM
# Quiz description
# 	Given an element in a list, write a function to determine the length of a particular element's sorting cycle. Given one element in the list, a sorting cycle is the number of swaps it takes so that the last displaced swapped item is back in its correct order.

def cycle_length(lst, n):
	sorted_lst = sorted(lst)
	cycle_count = 0
	while True:
		a, b = lst.index(n), sorted_lst.index(n)
		if a == b:
			break
		lst[b], lst[a] = lst[a], lst[b]
		n = lst[a]
		cycle_count += 1
	print(cycle_count)
	return cycle_count
		

steps = cycle_length([43, 81, 88, 93, 17, 32, 19, 11], 93)
steps = cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 6)
steps = cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 5)
steps = cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 2)
steps = cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 3)
