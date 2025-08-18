from colorama import Fore, Style
from random import randint
import time
import pygame
import re

pygame.init()

print(Fore.CYAN + "@GogaUa096 - Follow me on instagram :)" + Style.RESET_ALL)


class MusicPlayer:

    @staticmethod
    def casual_jazz():
        pygame.mixer.music.load(r"Music/CasualJazz.wav")
        pygame.mixer.music.play(-1)

    @staticmethod
    def cool_jazz():
        pygame.mixer.music.load(r"Music/CoolJazz.mp3")
        pygame.mixer.music.play(-1)

    @staticmethod
    def electric_jazz():
        pygame.mixer.music.load(r"Music/ElectricJazz.wav")
        pygame.mixer.music.play(-1)


class SoundPlayer:
    ...


music_player = MusicPlayer()


class SystemVoice:

    @staticmethod
    def how_to_play():
        rules = ("How to play:" + Style.RESET_ALL,
                 Fore.BLUE + "Task: To find the number guessed by the computer.",
                 "1. Enter the range in which you'll search for the number. (e.g. 5-100/50/20/...)",
                 "2. Then, start finding the hidden number.",
                 Fore.LIGHTRED_EX + "Now, try It Yourself! 🔥🔥🔥" + Style.RESET_ALL)
        print(Fore.LIGHTRED_EX + "Click Enter to continue")
        input()
        for rule in rules:
            print(rule, end="")
            input()

    @staticmethod
    def header(capital, *args):
        print(Fore.RED + f"\n>>> {capital}" + Style.RESET_ALL)
        for indx, arg in enumerate(list(args)):
            print(Fore.BLUE + f"{indx + 1}. {arg}")

    @staticmethod
    def error(*args):
        options = "/".join(list(args))
        print(Fore.LIGHTRED_EX + f">>> Error: Please, select one of these options: {options}" + Style.RESET_ALL)


class Game(SystemVoice):

    def audio_settings(self):
        answer = ""
        while answer.upper() not in ("BACK", "SETTINGS", "4"):
            self.header("Audio", "Music", "Sounds", "Turn Off All", "Settings" + Style.RESET_ALL)

            answer = input("<<< ")
            match answer.upper():
                case "MUSIC" | "M" | "1":
                    ...
                case "SOUNDS" | "S" | "2":
                    ...
                case "TURN OFF ALL" | "OFF" | "3":
                    ...
                case "SETTINGS" | "S" | "4":
                    ...
                case _:
                    self.error("MUSIC", "SOUNDS", "TURN OFF ALL", "SETTINGS")

    def settings(self):
        answer = ""
        while answer.upper() not in ("BACK", "MAIN MENU", "3"):
            self.header("Settings", "Rules", "Audio", "Main Menu" + Style.RESET_ALL)

            answer = input("<<< ")
            match answer.upper():
                case "RULES" | "R" | "1":
                    self.how_to_play()
                case "AUDIO" | "A" | "2":
                    print("Coming soon...")
                case "MAIN MENU" | "BACK" | "3":
                    pass
                case _:
                    self.error("RULES", "MUSIC", "MAIN MENU")


    def main_menu(self):
        answer = ""
        while answer.upper() not in ("QUIT", "Q", "3"):
            self.header("Main Menu", "Settings", "Play", "Quit" + Style.RESET_ALL)

            answer = input("<<< ")
            match answer.upper():
                case "SETTINGS" | "S" | "1":  # 1. Rules; 2. Audio
                    self.settings()
                case "PLAY" | "P" | "2":
                    print("Coming soon...")
                case "QUIT" | "Q" | "3":  # Close game
                    print(Fore.CYAN + ">>> Goodbye!")
                    time.sleep(0.5)
                case _:
                    self.error("SETTINGS", "PLAY", "QUIT")


game = Game()
game.main_menu()
