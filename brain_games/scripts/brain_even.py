#!/usr/bin/env python

import random
import prompt


def get_answer():
    number = int(random.randint(1, 100))
    print('Question: ', number)
    answer = str(input('Your answer: '))
    return number, answer


def is_even(number):
    if number % 2 == 0:
        return('yes')
    else:
        return('no')


def right_answer():
    print('Correct!')


def wrong_answer(name, answer, check_answer):
    print("'{}' is wrong answer ;(."
          "Correct answer was '{}'.".format(answer, check_answer))
    print("Let's try again, {}!".format(name))


def congratilations(name):
    print("Congratilations, {}!".format(name))


def game(name):
    for i in range(3):
        number, answer = get_answer()
        check_answer = is_even(number)
        if check_answer == answer:
            right_answer()
        else:
            wrong_answer(name, answer, check_answer)
            break
    else:
        congratilations(name)


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game(name)


if __name__ == "__main__":
    main()
