import random

COND = "What number is missing in the progression?"


def get_answer():
    n_progression = random.randint(5, 10)
    first_n = random.randint(1, 100)
    step = random.randint(2, 5)
    last_n = first_n + step * (n_progression - 1)
    pr_list = []
    for i in range(first_n, last_n + 1, step):
        pr_list.append(i)
    n_inv = random.randint(0, len(pr_list) - 1)
    n_correct = pr_list.pop(n_inv)
    pr_list.insert(n_inv, "..")
    pr_string = " ".join(str(e) for e in pr_list)
    print("Question:", pr_string)
    answer = int(input("Your answer: "))
    return n_correct, answer
