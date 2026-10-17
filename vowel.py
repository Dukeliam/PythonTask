word = str(input("Enter a word: "))

vowel = "aeiou"
count = 0
for index in word:
      if index in vowel:
            count += 1
print(count)
