def find_words_with_two_vowels(words):
    vowels = "aeiouAEIOU"
    result = [word for word in words if sum(1 for char in word if char in vowels) == 2]
    return result

print(find_words_with_two_vowels(["hello", "Python", "world", "platzi"]))

print(find_words_with_two_vowels(["text", "test", "python", "example"]))