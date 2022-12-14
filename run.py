"""
Main function to run game the file for 'Word-It'
"""

import os
import pygame
import pyfiglet
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from word_checker.py import WordChecker


# install & import pyfiglet module from https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/  # noqa

result = pyfiglet.figlet_format("Word-It", font="digital")
print(result)


def get_answer_from_file():
    """
    Open words.txt file and get random word
    for the user to guess when playing Word-It
    """
    file = open('words.txt', 'r', encoding='utf-8')
    lines = file.read().splitlines()
    random_word = random.choice(lines)
    return random_word.lower()


class Game:
    """
    This class represents the game set up and
    enables the flow of the game plan.
    Used to handle user input and feedback
    data to the user. Enables the display of
    an introduction, user play options,
    the ability for the user to input guesses,
    displaying guesses and reaching the end goal of the game
    by successfully or unsuccessfully guessing the
    random five letter word.
    """

    def __init__(self, word_checker):
        self.word_checker = word_checker
        self.guesses_list = []
        self.no_of_guesses = 6
        self.username = ""

    def introduction(self):
        """
        Displays an introduction message and
        asks to user to input a valid username.
        Return error message if a non numerical
        or alphabetical entry is input, e.g. blank space.
        Return greeting to user and use the username they input.
        """
        print(pyfiglet.figlet_format(
            "WELCOME TO WORD-IT", justify="center", width=80))
        print(
            Fore.MAGENTA + Style.BRIGHT +
            "Can you guess the word in just 6 tries?\n".center(80))
        while True:
            self.username = input(
                "Please enter your name to begin the game:\n").strip().capitalize()  # noqa

            if len(self.username.strip()) == 0:
                print(f"{Fore.RED}Username invalid, must contain letters or numbers.\n")  # noqa
            else:
                break
        print(f"{Fore.MAGENTA}/nHello {self.username}, lets play Word-It!\n")
        self.user_menu()

    def user_menu(self):
        """
        Ask the user if they would liek to play, or see the game instructions.
        Return an error message if input is invalid.
        """
        print('Choose from the following options:\n')
        user_option = input(
            f"{Fore.MAGENTA}P - PLAY/nI - INSTRUCTIONS{Fore.RESET}\n"
        ).strip().lower()

        if user_option == "p":
            self.ask_for_guess()

        elif user_option == "i":
            #  Credit: https://www.asciiart.eu/art-and-design/borders
            intro_message = """
             __| |____________________________________________| |__
            (__   ____________________________________________   __)
               | |                                            | |
               | |            How to Play Word-It             | |
               | |                                            | |
               | |   Guess the word in six or less attempts   | |
               | |                                            | |
               | |  Each guess must be a valid 5 letter word  | |
               | |                                            | |
               | | After each guess, the color of the letters | |
               | |   will change to show how close your guess | |
               | |              was to the word!              | |
               | |                                            | |
               | |   Green is a correct letter and position   | |
               | | Yellow is a correct letter, wrong position | |
               | |           Red is a wrong letter            | |
             __| |____________________________________________| |__
            (__   ____________________________________________   __)
               | |                                            | |
            """
            print(intro_message)
            self.ask_for_guess()
        else:
            print(Fore.RED + "Not a valid option\n")
            self.user_menu()

    def play_again(self):
        """
        When game ends, the user is asked if they wish to
        quit, or play again. Return error message if user
        inputs invalid option.
        """
        print('Choose from the following options:\n')
        user_choice = input(
            Fore.MAGENTA + "P - PLAY AGAIN\nQ - QUIT\n"
            ).strip().lower()

        if user_choice == "p":
            os.system('clear')
            main()

        elif user_choice == "q":
            print(" " + Fore.RESET)
            print(pyfiglet.figlet_format(
                "GOODBYE", justify="center", width=80))
            exit()
        else:
            print(Fore.RED+"Not a valid option\n")
            self.play_again()

    def ask_for_guess(self):
        """
        Use a while loop to collect a valid guess
        from the user if they have guesses remaining.
        If the user has no guesses remaining, the game
        will finish and a goodbye message will display.
        """
        while self.no_of_guesses <= 6:
            if self.no_of_guesses == 0:
                print(' \n')
                print("GAME OVER", justify="center", width=80)
                fore = Fore.YELLOW + Style.BRIGHT
                upper_answer = self.word_checker.answer.upper()
                print(f"The answer was....{fore}{upper_answer}\n")
                self.play_again()
            else:
                fore = Fore.YELLOW + Style.BRIGHT
                chances = self.no_of_chances
                reset = Fore.RESET + Style.RESET_ALL
                print(f"\nYou have {fore}{chances}{reset} chances left.\n")
            while True:
                user_input = input(
                    'Enter your 5 letter guess here:\n').lower().strip()
                if self.word_checker.validate_user_guess(user_input):
                    self.no_of_guesses -= 1
                    self.display_guesses(user_input)
                    if user_input == self.word_checker.answer:
                        score = 6 - self.no_of_chances
                        print(' \n')
                        print(pyfiglet.figlet_format(
                            "YOU WIN", justify="center", width=80))
                        print('\nWell done you got the correct answer!\n')
                        self.play_again()
                    break

    def display_guesses(self, user_input):
        """
        Display the user's guess and previous guesses one after
        the other with color-codes through colorama.
        """
        current_guess = self.word_checker.check_matching_letters(user_input)
        self.guesses_list.append(current_guess)

        print(f"""\n{Fore.CYAN}\t\t\t      =====================\n""")
        for i in self.guesses_list:
            print("\t\t\t\t      "+i)
        print(f"""\n{Fore.CYAN}\t\t\t      =====================""")


def main():
    """
    Retrieve an answer string from the words.txt file.
    Create new instance of WordChecker, passing the answer as a parameter.
    Create new instance of Game, passing the WordChecker instance as a parameter.
    Start the game using the introduction() method.
    """
    answer = get_answer_from_file()
    game = Game(WordChecker(answer))
    game.introduction()


main()
