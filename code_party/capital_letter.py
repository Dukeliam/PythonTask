words = ['python', 'java', 'c++']

def uppercase(word):
      return word.upper()
      
result = list(map(uppercase, words))
print(result)
