words = ["racecar", "level", "world", "hello"]

def find_largest_palindrome(words):
    
    def reverse_word(word):
        return word[::-1]

    palindrome_list = []
    for word in words:
        if word == reverse_word(word):
            palindrome_list.append(word)
    
    counter = 0
    largest_palindrome = ""
    
    if len(palindrome_list) == 0:
        return None
    
    else:
        for palindrome in palindrome_list:
            if len(palindrome) > counter:
                counter = len(palindrome)
                largest_palindrome = palindrome
        return largest_palindrome
        
print(find_largest_palindrome(words))

"""
Input: find_largest_palindrome(["racecar", "level", "world", "hello"])
Output: "racecar"

Input: find_largest_palindrome(["Platzi", "Python", "django", "flask"])
Output: None
"""