def sum_of_index(numbers):
      result = []
      for index in range(len(numbers[0])):
            total = 0
            
            for row in numbers:
                  total += row[index]
                  
            result.append(total)
      return result
      
numbers =  [ [2, 3, 4],  [1, 5, 7],  [4, 6, 8] ]

print(sum_of_index(numbers))
