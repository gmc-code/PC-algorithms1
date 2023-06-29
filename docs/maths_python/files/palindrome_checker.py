def is_palindrome(string):
    # Initialize pointers
    left = 0 
    right = len(string) - 1
    # Check all letters in the string 
    while left < right:
        # If letters are not equal
        # Decision -> Return False
        if string[left] != string[right]:
            return False  
        # Else, the letters are equal
        # Decision -> Bring left and right closer and compare again
        else:
            left += 1        
            right -= 1
    return True  


word_to_check = "racecar"
print(f"{word_to_check} is a plaindrome:", is_palindrome(word_to_check))
# racecar is a plaindrome True
word_to_check = "racecars"
print(f"{word_to_check} is a plaindrome:", is_palindrome(word_to_check))
# racecars is a plaindrome False

