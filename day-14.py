def count_substrings_with_max_k_unique(s, k):
    length = len(s)
    char_count = {}
    start = 0
    total_substrings = 0

    for end in range(length):
        if s[end] not in char_count:
            char_count[s[end]] = 0
        char_count[s[end]] += 1

        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        total_substrings += (end - start + 1)

    return total_substrings

def count_substrings_with_exactly_k_unique(s, k):
    return count_substrings_with_max_k_unique(s, k) - count_substrings_with_max_k_unique(s, k - 1)

print(count_substrings_with_exactly_k_unique("pqpqs", 2))
print(count_substrings_with_exactly_k_unique("aabacbebebe", 3))
print(count_substrings_with_exactly_k_unique("a", 1))
print(count_substrings_with_exactly_k_unique("abc", 3))
print(count_substrings_with_exactly_k_unique("abc", 2))
