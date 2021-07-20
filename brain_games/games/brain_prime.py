import random

COND = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_Prime(num):
    d = 2
    while num % d != 0:
        d += 1
    return "yes" if (d == num) else "no"


def get_answer():
    num = random.randint(1, 100)
    right_answer = is_Prime(num)
    print("Question: ", num)
    answer = input("Your answer: ")
    return right_answer, answer
