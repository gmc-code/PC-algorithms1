def length_of_longest_substring(s):
    """
    This function takes a string s as input and returns the length of the longest substring without repeating characters and the substring itself.
    """
    chars = set()
    left = right = max_len = 0
    max_substring = ""
    while right < len(s):
        if s[right] not in chars:
            chars.add(s[right])
            right += 1
            if max_len < right - left:
                max_len = right - left
                max_substring = s[left:right]
        else:
            chars.remove(s[left])
            left += 1
    return max_len, max_substring


s = "a-bc-d-e"
result, substring = length_of_longest_substring(s)
print(f"The longest substring without repeating characters in '{s}' is '{substring}', with length: {result}.")
# The longest substring without repeating characters in 'a-bc-d-e' is 'a-bc', with length: 4.

s = "ab-cd-e-fg-h-ij-k"
result, substring = length_of_longest_substring(s)
print(f"The longest substring without repeating characters in '{s}' is '{substring}', with length: {result}.")
# The longest substring without repeating characters in 'ab-cd-e-fg-h-ij-k' is 'ab-cd', with length: 
5.