"""
Problem 1: Define a funciton that counts vowels in a string.
Args:
	- s: String to be counted.
"""
def vowels(s):
	r = 0 # Store the result
	for c in s:
		if c in "aeoiuAEOIU":
			r += 1
	return r

# print(vowels(input()))

"""
Problem 2: Count the number of times a substring appears in a string.
Args:
	- h: String to be searched. (haystack)
	- n: Substring. (needle)
"""
def substring(h, n):
	r = 0 # Store the result
	i = 0
	while i >= 0:
		i = h.find(n, i)
		if i == -1:
			break
		r += 1
		i += 1
	return r

# hay = input("haystack: ")
# nee = input("needle: ")
# print(substring(hay, nee))

"""
Problem 3: Find longest subtring where characters are in alphabetical order. (lower case only)
Args:
	- s: String to search.
"""
def alphaSubtring(s):
