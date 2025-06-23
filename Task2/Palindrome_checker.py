def is_palindrome(s):
    try:
        if len(s) <= 1:
            return True
        elif s[0] != s[-1]:
            return False
        else:
            return is_palindrome(s[1:-1])
    except TypeError:
        print("Invalid input")
print(is_palindrome("madam"))
