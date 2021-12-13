def lengthOfLongestSubstring(s: str) -> int:
    # Storing a substring in a stack
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:  # aab
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])  #  a b
        res = max(res, r - l + 1)
    return res


# Longest Substring Without Repeating Characters
# Took multiple attempts to correctly solve it, since I had to fist understand sliding window technique


# s = "abcabcbb"
# s = "bbbbb"
# s = "pwwkew"
# s = " "
# s = "au"
s = "aab"
# s = "dvdf"
print(lengthOfLongestSubstring(s))
