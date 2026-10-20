def divisible(number):
      return number % 3 == 0 and number % 5 == 0
      
numbers = filter(divisible, range(1, 51))

print(list(numbers))
