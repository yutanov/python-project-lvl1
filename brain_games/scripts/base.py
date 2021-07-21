import prompt


def greeting():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {}!".format(name))
    return name


def right_answer():
    print("Correct!")


def wrong_answer(name, answer, check_answer):
    print(
        "'{}' is wrong answer ;(."
        " Correct answer was '{}'.".format(answer, check_answer)
    )
    print("Let's try again, {}!".format(name))


def congratulations(name):
    print("Congratulations, {}!".format(name))
