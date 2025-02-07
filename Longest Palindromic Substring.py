def expand_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        odd = expand_center(s, i, i)
        even = expand_center(s, i, i+1)
        res = max(res, odd, even, key=len)
    return res

print(longest_palindrome("babad"))  # Output: "bab"
