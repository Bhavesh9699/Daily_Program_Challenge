def longest_palindrome(s: str) -> str:
    if len(s) < 2:
        return s

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the palindrome substring

    longest = ""

    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)  # Check palindrome with center at index i
        palindrome2 = expand_around_center(i, i + 1)  # Check palindrome with centers at index i and i+1

        if len(palindrome1) > len(longest):
            longest = palindrome1

        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest
print(longest_palindrome("babad"))
