import random

COND = "Find the greatest common divisor of given numbers."


def gcd(a, b):
    return gcd(b, a % b) if b else a


def get_answer():
    num_one = int(random.randint(1, 100))
    num_two = int(random.randint(1, 100))
    print("Question: {} {}".format(num_one, num_two))
    divisor = gcd(num_one, num_two)
    answer = int(input("Your answer: "))
    return divisor, answer
