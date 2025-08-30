import time
from colorama import Fore, Style
from random import randint, shuffle, choice
import pygame
import re
import pyfiglet
from tqdm import tqdm

pygame.init()


class SystemPrompt:
    COLORS = [attr for attr in dir(Fore) if not attr.startswith("_")]
    shuffle(COLORS)

    def __init__(self):
        self.INPUT = self.get_colored_text("<<< ", "LIGHTWHITE_EX")
        self.RULES = (
            self.get_colored_text(">>> Press ENTER to continue\n", "LIGHTRED_EX"),
            self.get_colored_text(">>> Rules:", "LIGHTRED_EX"),
            self.get_colored_text(">>> Find the number the computer guessed.", "BLUE"),
            self.get_colored_text(">>> 1. Choose a range (e.g. 5-100).", "BLUE"),
            self.get_colored_text(">>> 2. Start guessing!", "BLUE"),
            self.get_colored_text(">>> Your turn!", "LIGHTRED_EX")
        )

    @staticmethod
    def get_colored_text(text: str, color: str, is_bold=False, is_reset_all=True):
        colored_text = getattr(Fore, color) + text
        if is_bold:
            colored_text = Style.BRIGHT + colored_text
        if is_reset_all:
            colored_text = colored_text + Style.RESET_ALL
        return colored_text

    def rules(self):
        for rule in self.RULES:
            print(rule, end="")
            input()

    def coming_soon(self, communicate="Coming soon..."):
        print(self.get_colored_text(f">>> {communicate}", "LIGHTWHITE_EX"))

    def error(self, communicate="Enter one of the options shown above!"):
        print(self.get_colored_text(f">>> Error: {communicate}", "LIGHTRED_EX"))

    def farewell(self, communicate="Goodbye! :)"):
        print(self.get_colored_text(f">>> {communicate}", "LIGHTCYAN_EX"))

    def pass_func(self):
        return


system = SystemPrompt()


class GameIntro:  # COOKED
    INTRO_SOUNDTRACK = pygame.Sound("Sounds/IntroMusic.wav")

    @staticmethod
    def my_accounts():
        print(system.get_colored_text("@GogaUa096 - Follow me on Instagram :)\n"
                                      "@GogaUa069 - Check my GitHub\n", "CYAN"))

    @staticmethod
    def loading():
        with tqdm(total=100) as pbar:
            for i in range(100):
                color = choice([c for c in system.COLORS if c != "BLACK"])
                pbar.set_description_str(system.get_colored_text("Loading", color))
                pbar.update(1)
                time.sleep(0.03)
        print()

    @staticmethod
    def show_game_banner(banner: str):
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
        self.show_game_banner("Guess Code 4.2.0 ALFA")  # UPDATES UPDATES UPDATES UPDATES UPDATES UPDATES
        self.loading()


class MenuPattern:
    def __init__(self, header: str, options: tuple):
        self.header = header
        self.options = options
        self.answer = str()

    def show_menu(self):
        print(system.get_colored_text(f">>> {self.header}", "LIGHTRED_EX"))
        for indx, option in enumerate(self.options):
            print(system.get_colored_text(f"{indx + 1}. {option.name}", "BLUE"))

    def match_answer(self):
        for indx, option in enumerate(self.options):
            if self.answer in option.variants:
                option.usage()
                return
        system.error()

    def select_answer(self):
        while self.answer not in self.options[-1].variants:
            self.show_menu()
            self.answer = input(system.INPUT).strip().upper()
            self.match_answer()


class Soundtracks:
    HEADER = "Soundtracks"

    CASUAL_JAZZ = "Music/CasualJazz.wav"
    COOL_JAZZ = "Music/CoolJazz.mp3"
    ELECTRIC_JAZZ = "Music/ElectricJazz.wav"

    def __init__(self):
        self.JAZZ1 = ...
        self.JAZZ2 = ...
        self.JAZZ3 = ...
        self.TURN_OFF = ...
        self.BACK = ...
        self.OPTIONS = (self.JAZZ1, self.JAZZ2, self.JAZZ3, self.TURN_OFF, self.BACK)

    @staticmethod
    def play_soundtrack(path):
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(-1)
        except pygame.error:
            system.error(f"Can't find soundtrack at path {path}")

    def __call__(self, *args, **kwargs):
        ...


class Sounds:
    HEADER = "Sounds"
    IS_SOUND = True

    VICTORY = pygame.Sound("Sounds/YouWinGoga.wav")  # MAXTIME = 2350
    FAILURE = pygame.Sound("Sounds/YouLostGoga.wav")  # MAXTIME = 2500

    def __init__(self):
        self.TOGGLE = ...
        self.BACK = ...
        self.OPTIONS = (self.TOGGLE, self.BACK)

    def __call__(self, *args, **kwargs):
        ...


class Audio:
    HEADER = "Audio"

    def __init__(self):
        self.SOUNDTRACKS = ...
        self.SOUNDS = ...
        self.BACK = ...
        self.OPTIONS = (self.SOUNDTRACKS, self.SOUNDS, self.BACK)

    def __call__(self, *args, **kwargs):
        ...


class Settings:
    HEADER = "Settings"

    def __init__(self):
        self.RULES = ...
        self.AUDIO = ...
        self.BACK = ...
        self.OPTIONS = (self.RULES, self.AUDIO, self.BACK)

    def __call__(self, *args, **kwargs):
        ...


class MainMenu:
    HEADER = "Main Menu"

    def __init__(self):
        self.PLAY = ...
        self.SETTINGS = ...
        self.QUIT = ...
        self.OPTIONS = (self.PLAY, self.SETTINGS, self.QUIT)
