#!/usr/bin/env python

from brain_games.scripts import base


def brain_even():
    from brain_games.scripts import brain_even
    module = brain_even
    main(module)


def brain_calc():
    pass


def n3():
    pass


def n4():
    pass


def n5():
    pass


def start(module, name):
    for i in range(3):
        number, answer = module.get_answer()
        check = module.check_answer(number)
        if check == answer:
            base.right_answer()
        else:
            base.wrong_answer(name, answer, check)
            break
    else:
        base.congratilations(name)


def main(module):
    name = base.greeting()
    print(module.COND)
    start(module, name)