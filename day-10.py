def groupAnagrams(strs):
    anagram_groups = {}
    for word in strs:
        char_freq = [0] * 26
        for char in word:
            char_freq[ord(char) - ord('a')] += 1
        key = tuple(char_freq)
        if key in anagram_groups:
            anagram_groups[key].append(word)
        else:
            anagram_groups[key] = [word]

    return list(anagram_groups.values())
print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
