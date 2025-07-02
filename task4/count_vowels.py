word = input("Enter a word: ")
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in word if char in vowels)
print(f"Number of vowels in '{word}': {vowel_count}")
