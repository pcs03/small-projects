import re 

def palindrome(s):
    s = re.sub('[^a-z]+', '', s.lower())
    print(s)

    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

print(palindrome("hello"))
