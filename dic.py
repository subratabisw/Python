num_to_words = dict()
num_to_words[1] = 'One'
num_to_words[2] = 'Two'
num_to_words[3] = 'Three'

print(num_to_words)
print(type(num_to_words))
print(len(num_to_words))

if 3 in num_to_words:
    print('Available')
else:
    print('Not avialable')
del num_to_words[2]
print(num_to_words)
for item, value in num_to_words.items():
    print(item,value)
print(num_to_words.items())
print(num_to_words.keys())
num_to_words.clear()
print(num_to_words)
fruits = {'a': 'Apple', 'b': 'Banana', 'c': 'cherry'}
print(fruits.get('d'))
