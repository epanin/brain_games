#!/usr/bin/env python3

import random
import prompt
import brain_games.scripts.brain_games as brgame


def main():
    user_name = brgame.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    tries = 3
    numrange = 100
    for _ in range(tries):
        randnum = random.randint(0, numrange)
        is_even = randnum % 2 == 0
        if is_even:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {randnum}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.",
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
