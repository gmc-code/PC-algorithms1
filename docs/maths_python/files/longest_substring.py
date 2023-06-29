def length_of_longest_substring(s):
    """
    This function takes a string s as input and returns the length of the longest substring without repeating characters.
    """
    chars = set()
    left = right = max_len = 0
    while right < len(s):
        if s[right] not in chars:
            chars.add(s[right])
            right += 1
            max_len = max(max_len, right - left)
        else:
            chars.remove(s[left])
            left += 1
    return max_len


s = "a-bc-d-e"
result = length_of_longest_substring(s)
print(f"The length of the longest substring without repeating characters in '{s}' is {result}.")
# The length of the longest substring without repeating characters in 'a-bc-d-e' is 4.

s = "ab-cd-e-fg-h-ij-k"
result = length_of_longest_substring(s)
print(f"The length of the longest substring without repeating characters in '{s}' is {result}.")
# The length of the longest substring without repeating characters in 'ab-cd-e-fg-h-ij-k' is 5.
