# Longest Alternating Substring
# Quiz URL:
# 	https://edabit.com/challenge/RB6iWFrCd6rXWH3vi
# Quiz description:
# 	Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. 
# 	If two or more substrings have the same length, return the substring that occurs first.

def longest_alternating_substring(input_string):

	tmp_string = input_string
	longest_len = 0
	final_substring = ""
	index = 0
	consumed = 0

	while(1):

		if(consumed==len(input_string)):
			break

		substring = ""
		first_time = True
		index = 0
		cur_len = 0
		if(len(tmp_string) == 1):
			break

		for number in tmp_string:

			consumed += 1

			# First time the algorithm runs
			if(first_time):
				if(int(number)%2==0):
					looking_for_even = False
				else:
					looking_for_even = True
				substring += str(number)
				cur_len += 1
				first_time = False
				index += 1
				if(cur_len > longest_len):
					longest_len = cur_len
					final_substring = substring
				continue

			if(looking_for_even):
				if(int(number)%2==0):
					substring += str(number)
					cur_len += 1
					index += 1
					looking_for_even = False
					if(cur_len > longest_len):
						longest_len = cur_len
						final_substring = substring
					continue
				else:
					tmp_string = tmp_string[index:len(tmp_string)]
					if(cur_len > longest_len):
						longest_len = cur_len
						final_substring = substring
					consumed -= 1
					break
			else:
				if(int(number)%2!=0):
					substring += str(number)
					cur_len += 1
					index += 1
					looking_for_even = True
					if(cur_len > longest_len):
						longest_len = cur_len
						final_substring = substring
					continue
				else:
					tmp_string = tmp_string[index:len(tmp_string)]
					if(cur_len > longest_len):
						longest_len = cur_len
						final_substring = substring
					consumed -= 1
					break

	return final_substring

print(longest_alternating_substring("225424272163254474441338664823"))
print(longest_alternating_substring("594127169973391692147228678476"))
print(longest_alternating_substring("721449827599186159274227324466"))
