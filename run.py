"""
Main function to run game the file for 'Word-It'
"""

import os
import sys
import pygame
import pyfiglet
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# install & import pyfiglet module from https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/

result = pyfiglet.figlet_format("Word-It", font = "digital")
print(result)


def get_word_from_file():
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
                "Please enter your name to begin the game:\n").strip().capitalize()

            if len(self.username.strip()) == 0:
                print(f"{Fore.RED}Username invalid, must contain letters or numbers.\n")
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
        user_choice = input (
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


def main():
    """
    Retrieve a random answer from the words.txt file.
    """
    answer = get_word_from_file()
    game.introduction()

main()
