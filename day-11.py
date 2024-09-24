def generate_permutations(string):
    def helper(index):
        if index == len(string):
            output.append(''.join(string))
        used = set()
        for j in range(index, len(string)):
            if string[j] in used:
                continue
            used.add(string[j])
            string[index], string[j] = string[j], string[index]
            helper(index + 1)
            string[index], string[j] = string[j], string[index]

    output = []
    string = list(string)
    helper(0)
    return output
print(generate_permutations("abc"))
print(generate_permutations("aab"))
print(generate_permutations("aaa"))
print(generate_permutations("a"))
print(generate_permutations("abcd"))
