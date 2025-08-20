# def check_palindrome(s):
#     l = 0
#     r = len(s) - 1

#     while l < r:
#         if s[l] != s[r]:
#             return False
#         l += 1
#         r -= 1
#     return True

def check_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    reversed_cleaned = cleaned[::-1]
    return cleaned == reversed_cleaned

if __name__ == "__main__":
    print(check_palindrome("racecar"))  # True
    print(check_palindrome("hello"))     # False
    print(check_palindrome("A man a plan a canal Panama"))  # True
    print(check_palindrome("No lemon, no melon"))  # True
    print(check_palindrome("Was it a car or a cat I saw?"))  # True