def tax(price):
    return price * (price / 10)
prices = [100, 200, 300]
result = list(map(tax, prices))
print(result)
