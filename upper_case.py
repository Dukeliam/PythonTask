word = str(input("Enter a word: "))
result = ""

for index in word:
      if index.isupper():
            result += index.lower()
      else:
            result += index
print(result) 
