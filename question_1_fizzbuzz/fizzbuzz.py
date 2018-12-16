def fizzbuzz():
    return '\n'.join(['Fizz' * (number % 3 == 0) + 'Buzz' * (number % 5 == 0) or str(number) for number in range(1, int(input()) + 1)])


print(fizzbuzz())
