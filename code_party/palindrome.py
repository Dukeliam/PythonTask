def is_palindrome(word):
      original = word
      reverse = ""
      for index in range(len(word) -1, -1, -1):
            reverse += word[index]
            
      return original == reverse    
      
words = ['level', 'world', 'madam', 'python']

palindrome = list(filter(is_palindrome, words))

print(palindrome)
