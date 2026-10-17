divisor = 10000

number = int(input('Enter 5 numbers: '))

for count in range(5):

      digit = number // divisor
      print(digit)
      number = number % divisor
      divisor = divisor // 10
