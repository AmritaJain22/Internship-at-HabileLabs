def count_vowels(s):
    try:
        count = 0
        vowels = "aeiouAEIOU"
        for ch in s:
            if ch in vowels:
                count += 1
        return count
    except TypeError:
        print("Error: Please enter a valid string.")
    except Exception as e:
        print("Unexpected error:", e)
print(count_vowels("hello"))
