def reverse_words(str1):
    words_list = str1.split()  
    reversed_words = words_list[::-1]  
    return ' '.join(reversed_words)  
print(reverse_words("the sky is blue"))      
print(reverse_words("   hello    world  "))  
print(reverse_words("single"))               
print(reverse_words("     "))   
