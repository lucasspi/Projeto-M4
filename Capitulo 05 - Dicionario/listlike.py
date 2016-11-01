spam = {'color': 'red', 'age': 42}
print(spam.keys())
print(list(spam.keys()))

for k, v in spam.items():
    print('Key:' + k + ' Value: ' + str(v))
