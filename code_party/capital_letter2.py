def capital_names(name):
    return name[0].upper() + name[1:]
names = ['john', 'mary', 'steve']
result = list(map(capital_names, names))
print(names)
