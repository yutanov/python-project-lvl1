#!/usr/bin/env python

from brain_games.scripts import base


def brain_even():
    from brain_games.games import brain_even 
    main(brain_even)


def brain_calc():
    from brain_games.games import brain_calc
    main(brain_calc)


def brain_gcd():
    from brain_games.games import brain_gcd
    main(brain_gcd)


def brain_progression():
    from brain_games.games import brain_progression
    main(brain_progression)


def brain_prime():
    from brain_games.games import brain_prime
    main(brain_prime)


def start(module, name):
    for i in range(3):
        correct_answer, answer = module.get_answer()
        if correct_answer == answer:
            base.right_answer()
        else:
            base.wrong_answer(name, answer, correct_answer)
            break
    else:
        base.congratilations(name)


def main(module):
    name = base.greeting()
    print(module.COND)
    start(module, name)
