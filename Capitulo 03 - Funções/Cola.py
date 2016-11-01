def collatz(number):

    if number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        print(number)
        collatz(number)

inputNumber = None

while True:
    print('Enter number: ')
    try:
        inputNumber = int(input())
        break
    except ValueError:
        print('You must enter an integer.')

collatz(inputNumber)
