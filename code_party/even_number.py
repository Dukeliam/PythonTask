def is_even_number(number):
      return number % 2 == 0

even_number = filter(is_even_number, range(1,21))

print(list(even_number))
