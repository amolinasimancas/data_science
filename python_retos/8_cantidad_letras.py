phrase = "Hola Mundo"

def count_letters(phrase):
  # Tu código aquí 👈
  output = {}
  for letter in phrase:
    if letter not in output.keys():
      output[f"{letter}"] = phrase.count(f"{letter}")
  return output

print(count_letters(phrase))

'''
Input: "Hola Mundo"

Output: {
  'H': 1, 
  'o': 2, 
  'l': 1, 
  'a': 1, 
  ' ': 1, 
  'M': 1, 
  'u': 1, 
  'n': 1, 
  'd': 1
}
'''