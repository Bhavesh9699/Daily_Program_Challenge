def find_common_prefix(strings):
    if not strings:
        return ""
    common_prefix = strings[0]
    
    for word in strings[1:]:
        while word[:len(common_prefix)] != common_prefix:
            common_prefix = common_prefix[:-1]
            if not common_prefix:
                return ""
    
    return common_prefix
print(find_common_prefix(["flower", "flow", "flight"]))
print(find_common_prefix(["dog", "racecar", "car"]))
print(find_common_prefix(["apple", "ape", "april"])) 
print(find_common_prefix([""])) 
print(find_common_prefix(["alone"]))
