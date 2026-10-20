from functools import reduce


def add(first_number, second_number):
    return first_number + second_number
numbers = range(1, 51)
result = reduce(add, numbers)
print(result)


def find_maximum(first_number, seccond_number):
    if first_number > second_number:
        return first_number
    else:
        return second_number

numbers = [3, 5, 9, 2, 8]
maximum = reduce(find_maximum, numbers)

print("Maximum number:", maximum)



def join_words(first_word, second_word):
    return first_word + " " + second_word

words = ['I', 'love', 'Python']
sentence = reduce(join_words, words)

print("in words: ", sentence)



def square(number):
    return number ** 2

def multiply(number_one, number_two):
    return number_one * number_two

numbers = [1, 2, 3, 4]

squares = list(map(square, numbers))
product = reduce(multiply, squares)

print("the product of sguare: ", product)
