# Version 4.2.2 ALFA

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
        time.sleep(0.5)

    def pass_func(self):
        return


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
        self.show_game_banner("Guess Code 4.2.2 ALFA")  # UPDATES UPDATES UPDATES UPDATES UPDATES UPDATES
        self.loading()


game_intro = GameIntro()


class MenuPattern:
    def __init__(self, header: str, options: tuple):
        self.header = header
        self.options = options
        self.answer = str()

    def show_menu(self):
        print(system.get_colored_text(f"\n>>> {self.header}", "LIGHTRED_EX"))
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


class Option:
    def __init__(self, name: str, func, variants: tuple):
        self.name = name
        self.func = func
        self.variants = variants

    def usage(self):
        self.func()


class SoundtrackOption:
    def __init__(self, name: str, path, variants: tuple):
        self.name = name
        self.path = path
        self.variants = variants

    def usage(self):
        Soundtracks.play_soundtrack(self.path)


class SoundOption:
    def __init__(self, name: str, sound, variants: tuple, is_sound: bool):
        self.name = name
        self.sound = sound
        self.variants = variants
        self.is_sound = is_sound

    def usage(self):
        flag = sounds.toggle_sound()
        print(self.sound[flag]["COMMUNICATE"])
        sound = self.sound[flag]
        sound["SOUND"].play(maxtime=sound["MAXTIME"])

class Soundtracks:
    HEADER = "Soundtracks"

    CASUAL_JAZZ = "Music/CasualJazz.wav"
    COOL_JAZZ = "Music/CoolJazz.mp3"
    ELECTRIC_JAZZ = "Music/ElectricJazz.wav"

    def __init__(self):
        self.JAZZ1 = SoundtrackOption("Casual Jazz", self.CASUAL_JAZZ, ("CASUAL", "JAZZ 1", "1"))
        self.JAZZ2 = SoundtrackOption("Cool Jazz", self.COOL_JAZZ, ("COOL", "JAZZ 2", "2"))
        self.JAZZ3 = SoundtrackOption("Electric Jazz", self.ELECTRIC_JAZZ, ("ELECTRIC", "JAZZ 3", "3"))
        self.TURN_OFF = Option("Turn Off", self.turn_off_music, ("TURN OFF", "OFF", "4"))
        self.BACK = Option("Back - Audio", system.pass_func, ("BACK", "AUDIO", "5"))

        self.OPTIONS = (self.JAZZ1, self.JAZZ2, self.JAZZ3, self.TURN_OFF, self.BACK)

    @staticmethod
    def play_soundtrack(path):
        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(-1)
        except pygame.error:
            system.error(f"Can't find soundtrack at path {path}")

    @staticmethod
    def turn_off_music():
        pygame.mixer.music.stop()
        print(system.get_colored_text("Music is turned Off", "LIGHTRED_EX"))

    def __call__(self, *args, **kwargs):
        soundtracks_menu = MenuPattern(self.HEADER, self.OPTIONS)
        soundtracks_menu.select_answer()


soundtracks = Soundtracks()


class Sounds:
    HEADER = "Sounds"
    IS_SOUND = True

    SOUNDS = {True: {"SOUND": pygame.Sound("Sounds/YouWinGoga.wav"), "MAXTIME": 2350,
                     "COMMUNICATE": system.get_colored_text("Sounnds're turned On", "LIGHTGREEN_EX")},
              False: {"SOUND": pygame.Sound("Sounds/YouLostGoga.wav"), "MAXTIME": 2500,
                    "COMMUNICATE": system.get_colored_text("Sounds're turned Off", "LIGHTRED_EX")}
              }

    def __init__(self):
        self.TOGGLE = SoundOption("Turn On/Off", self.SOUNDS, ("ON", "OFF", "1"), self.IS_SOUND)
        self.BACK = Option("Back - Audio", system.pass_func, ("BACK", "AUDIO", "2"))

        self.OPTIONS = (self.TOGGLE, self.BACK)

    def toggle_sound(self):
        self.IS_SOUND = not self.IS_SOUND
        return self.IS_SOUND

    def __call__(self, *args, **kwargs):
        sounds_menu = MenuPattern(self.HEADER, self.OPTIONS)
        sounds_menu.select_answer()


sounds = Sounds()


class Audio:
    HEADER = "Audio"

    def __init__(self):
        self.SOUNDTRACKS = Option(soundtracks.HEADER, soundtracks, ("SOUNDTRACKS", "1"))
        self.SOUNDS = Option(sounds.HEADER, sounds, ("SOUNDS", "2"))
        self.BACK = Option("Back - Settings", system.pass_func, ("BACK", "SETTINGS", "3"))
        self.OPTIONS = (self.SOUNDTRACKS, self.SOUNDS, self.BACK)

    def __call__(self, *args, **kwargs):
        audio_menu = MenuPattern(self.HEADER, self.OPTIONS)
        audio_menu.select_answer()


audio = Audio()


class Settings:
    HEADER = "Settings"

    def __init__(self):
        self.RULES = Option("Rules", system.rules, ("RULES", "1"))
        self.AUDIO = Option(audio.HEADER, audio, ("AUDIO", "2"))
        self.BACK = Option("Back - Main Menu", system.pass_func, ("BACK", "MAIN MENU", "3"))
        self.OPTIONS = (self.RULES, self.AUDIO, self.BACK)

    def __call__(self, *args, **kwargs):
        settings_menu = MenuPattern(self.HEADER, self.OPTIONS)
        settings_menu.select_answer()


settings = Settings()


class MainMenu:
    HEADER = "Main Menu"

    def __init__(self):
        self.PLAY = Option("Play", system.coming_soon, ("PLAY", "P", "1"))
        self.SETTINGS = Option(settings.HEADER, settings, ("SETTINGS", "S", "2"))
        self.QUIT = Option("Quit", system.farewell, ("QUIT", "Q", "3"))
        self.OPTIONS = (self.PLAY, self.SETTINGS, self.QUIT)

    def __call__(self, *args, **kwargs):
        main_menu_ = MenuPattern(self.HEADER, self.OPTIONS)
        main_menu_.select_answer()


main_menu = MainMenu()

def game():
    game_intro.intro()
    main_menu()


game()
