# Version 4.0.0 ALFA

import time
from colorama import Fore, Style
from random import randint, shuffle, choice
import pygame
import re
import pyfiglet
from tqdm import tqdm

pygame.init()


class Option:
    def __init__(self, func, *args):
        self.option_choices = tuple(args)
        self.func = func


class SystemPrompt:
    COLORS = [attr for attr in dir(Fore) if not attr.startswith("_")]
    shuffle(COLORS)

    def __init__(self):
        self.RULES = (self.get_colored_text(">>> Press ENTER to continue.\n", "LIGHTRED_EX", False, False),
                      "Game rules:",
                      self.get_colored_text("Task: To find the number guessed by the computer.", "BLUE", False, False),
                      "1. Enter the range in which you'll search for the number. (e.g. 5-100/50/20/...)",
                      "2. Then, start finding the hidden number.",
                      self.get_colored_text("Now, try it yourself!", "LIGHTRED_EX"))
        self.INPUT = self.get_colored_text("<<< ", "LIGHTWHITE_EX")

    @staticmethod
    def get_colored_text(text, color, is_bold=False, is_reset_all=True):  # If you use light colors, enter _EX after color
        colored_text = getattr(Fore, color) + text
        if is_bold:
            colored_text = Style.BRIGHT + colored_text
        if is_reset_all:
            colored_text += Style.RESET_ALL
        return colored_text

    def coming_soon(self):  # System func. Use only during testing
        print(self.get_colored_text(">>> Coming soon...\n", "LIGHTWHITE_EX"))

    def error(self):
        print(self.get_colored_text("\n>>> Error: Enter one of the options shown above!\n", "LIGHTRED_EX"))

    def goodbye(self):
        print(self.get_colored_text(">>> Goodbye! :)", "LIGHTCYAN_EX"))
        time.sleep(0.5)

    def show_rules(self):
        for rule in self.RULES:
            print(rule, end="")
            input()

    def option_menu_pattern(self, header, options):

        def show_options():
            print(self.get_colored_text(f">>> {header}", "LIGHTRED_EX"))
            for indx, option in enumerate(options.keys()):
                print(self.get_colored_text(f"{indx+1}. {option}", "BLUE"))

        def answer_matching():
            flag = False
            for option in options:
                option = options[option]
                if answer.upper() in option.option_choices:
                    flag = True
                    option.func()
            if not flag:
                self.error()

        answer = ""
        while answer.upper() not in options["Leave"].option_choices:
            show_options()
            answer = input(self.INPUT)
            answer_matching()


system = SystemPrompt()


class GameIntro:
    INTRO_SOUNDTRACK = pygame.Sound("Sounds/IntroMusic.wav")

    @staticmethod
    def my_accounts():
        print(system.get_colored_text("@GogaUa096 - Follow me on Instagram :)\n"
                                           "@GogaUa069 - Check my GitHub\n", "CYAN"))

    @staticmethod
    def loading():
        with tqdm(total=100) as pbar:
            for i in range(100):
                color = choice(system.COLORS)
                pbar.set_description_str(system.get_colored_text("Loading", color))
                pbar.update(1)
                time.sleep(0.03)
        print()

    @staticmethod
    def show_game_banner(banner):
        time.sleep(0.5)
        print(system.get_colored_text("Welcome to:", "CYAN", True))
        time.sleep(1.5)

        ascii_banner = pyfiglet.figlet_format(banner)
        for line in ascii_banner.splitlines():
            print(system.get_colored_text(line, "LIGHTBLUE_EX"))
            time.sleep(0.25)

        print(system.get_colored_text("Made by GogaUa\n", "WHITE", True))
        time.sleep(1)

    def intro(self):
        self.INTRO_SOUNDTRACK.play()
        self.my_accounts()
        self.show_game_banner("Guess Code 3.0 ALFA")
        self.loading()


class SoundtrackPlayer:
    ...


# TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING
game_intro = GameIntro()
game_intro.intro()

play_option = Option(system.coming_soon, "PLAY", "P", "1")
settings_option = Option(system.coming_soon, "SETTINGS", "S", "2")
leave_option = Option(system.goodbye, "LEAVE", "L", "3")

system.option_menu_pattern("Main Menu", {"Play": play_option,
                                                        "Settings": settings_option,
                                                        "Leave": leave_option})
