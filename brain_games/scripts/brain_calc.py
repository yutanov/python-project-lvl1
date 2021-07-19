import random
import operator


COND = "What is the result of the expression?"


def get_answer():
    operations = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    op = random.choice(list(operations.keys()))
    num_one = int(random.randint(1, 100))
    num_two = int(random.randint(1, 100))
    expression = operations[op](num_one, num_two)
    print("Question: {} {} {}".format(num_one, op, num_two))
    answer = int(input("Your answer: "))
    return expression, answer


def check_answer(expression):
    return expression
   
