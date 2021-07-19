import random


COND = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_answer():
    number = int(random.randint(1, 100))
    print('Question: ', number)
    answer = str(input('Your answer: '))
    return number, answer


def check_answer(number):
    if number % 2 == 0:
        return('yes')
    else:
        return('no')
