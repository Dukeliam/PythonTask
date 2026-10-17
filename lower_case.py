word = str(input("Enter a word: "))
result = ""

for index in word:
      if index.islower():
            result += index.upper()
      else:
            result += index
print(result) 
