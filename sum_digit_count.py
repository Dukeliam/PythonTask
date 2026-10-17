number = int(input("Enter a numbers: "))

digit_sum = 0

while number > 0:
      digit = number % 10
      digit_sum += digit
      number //= 10
print(digit_sum)
