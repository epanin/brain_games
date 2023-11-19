#!/usr/bin/env python3

import brain_games.cli as cli


def main():
    print('Welcome to the Brain Games!')
    user_name = cli.welcome_user()
    return user_name


if __name__ == '__main__':
    main()
