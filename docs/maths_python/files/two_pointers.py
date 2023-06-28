def isPairSum(A, N, X):
	"""
    This function takes a sorted list of integers A, 
	the length of the list N, and an integer X as input.
    It returns a tuple containing a boolean value and two integers from the list if there exists a pair of elements (A[i], A[j]) such that their sum is equal to X.
    If no such pair exists, it returns False.
    """
	# represents first pointer
	i = 0
	# represents second pointer
	j = N - 1
	while i < j:
		# If we find a pair
		if A[i] + A[j] == X:
			return True, A[i], A[j]
		# If sum of elements at current pointers is less, 
		# move towards higher values by doing i+1
		elif A[i] + A[j] < X:
			i += 1
		# If sum of elements at current pointers is more, 
		# move towards lower values by doing j-1
		else:
			j -= 1

	return False


# Main code
if __name__ == "__main__":
	# array to check
	arr = [2, 3, 5, 8, 9, 10, 11]
	# array should be sorted first
	arr.sort()
	# value to search for 3 values to sum to
	val = 17
	# size of the array
	arrSize = len(arr)
	# Function call
	print(isPairSum(arr, arrSize, val))
