numbers =  [ [2, 3, 4],  [1, 5, 7],  [4, 6, 8] ]

def sum_numbers(numbers):
      list_number = []
      for index in numbers:
            total = 0
            for count in index:
                  total += count
            list_number.append(total)
      return list_number
      

print(sum_numbers(numbers))      
