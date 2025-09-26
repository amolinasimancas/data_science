def count_words_by_length(words):
    return {len(len_word):sum(1 for word in words if len(len_word) == len(word)) for len_word in words}

print(count_words_by_length([
  "apple",
  "banana",
  "orange",
  "grapefruit",
  "pear",
  "kiwi"
]))

print(count_words_by_length([
  "apple",
  "banana",
  "orange"
]))