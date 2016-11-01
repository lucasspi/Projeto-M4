import pprint

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)
spam.setdefault('color', 'white')
print(spam)

message = 'It was a bright cold day in April, and the clocks were striking ' \
          'thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
pprint.pprint(count)
print(pprint.pformat(count))
