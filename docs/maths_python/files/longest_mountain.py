def longest_mountain(A):
    """
    Finds the longest ascending-descending sequence in the given set of numbers.

    Parameters:
        A (list): The list of numbers.

    Returns:
        int: The length of the longest ascending-descending sequence in the given list.
        list: The longest ascending-descending sequence in the given list.
    """

    N = len(A)
    mountan_length = base = 0
    longest_seq = []
    while base < N:
        end = base
        if end + 1 < N and A[end] < A[end + 1]:
            while end + 1 < N and A[end] < A[end + 1]:
                end += 1
            if end + 1 < N and A[end] > A[end + 1]:
                while end + 1 < N and A[end] > A[end+1]:
                    end += 1
                if mountan_length < end - base + 1:
                    mountan_length = end - base + 1
                    longest_seq = A[base:end+1]
        base = max(end, base + 1)
    return mountan_length, longest_seq

A = [2, 1, 4, 7, 3, 2, 5]
length, sequence = longest_mountain(A)
print(f"The longest mountain sequence is: {sequence}, with length: {length}")
# The longest mountain sequence is: [1, 4, 7, 3, 2], with length: 5
