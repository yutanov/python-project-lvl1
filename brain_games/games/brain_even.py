import random


COND = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return('yes')
    else:
        return('no')


def get_answer():
    number = int(random.randint(1, 100))
    print('Question: ', number)
    correct_answer = is_even(number)
    answer = str(input('Your answer: '))
    return correct_answer, answer
