# Given a string, find the longest subtring that only contains unique characters. Input: "0a123a45a6" Output: "0a12345"

def find_longest_unique_substring(s):
    if not s:
        return ""
    
    max_len = 0
    start = 0
    end = 0
    seen = set()
    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            end += 1
            max_len = max(max_len, end - start)
        else:
            seen.remove(s[start])
            start += 1
    
    return s[start:end]

# Test find_longest_unique_substring function
print(find_longest_unique_substring("0a123a45a6")) # "0a12345"