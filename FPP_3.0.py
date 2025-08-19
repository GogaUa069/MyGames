# Bold Text for Error only Light Red

from colorama import Fore, Style
from random import randint
import time
import pygame
import re
import pyfiglet
from tqdm import tqdm

pygame.init()

print(Fore.CYAN + "@GogaUa096 - Follow me on instagram :)\n"
                  "@GogaUa069 - Check my GitHub\n" + Style.RESET_ALL)

def get_bold_text(text, return_type):
    match return_type.upper():
        case "RETURN":
            return f"\033[1m{text}\033[0m"
        case "PRINT":
            print(f"\033[1m{text}\033[0m")
    return None

def loading():
    with tqdm(total=100) as pbar:
        for i in range(100):
            color = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA][i % 6]
            pbar.set_description_str(color + "Loading" + Style.RESET_ALL)
            pbar.update(1)
            time.sleep(0.05)


def show_banner(banner):
    time.sleep(0.5)
    print(Fore.CYAN + get_bold_text("Welcome to: ", "RETURN"))
    time.sleep(1.5)

    ascii_banner = pyfiglet.figlet_format(banner)
    for let in ascii_banner.splitlines():
        print(Fore.LIGHTBLUE_EX + let + Style.RESET_ALL)
        time.sleep(0.25)
    print(Fore.WHITE + get_bold_text("Made by GogaUa\n", "RETURN") + Style.RESET_ALL)
    time.sleep(1)

show_banner("Guess Code 3.0 ALFA")
loading()


class SystemVoice:

    @staticmethod
    def coming_soon():
        print(Fore.LIGHTWHITE_EX + "Coming soon..." + Style.RESET_ALL)

    @staticmethod
    def how_to_play():
        rules = ("How to play:" + Style.RESET_ALL,
                 Fore.BLUE + "Task: To find the number guessed by the computer.",
                 "1. Enter the range in which you'll search for the number. (e.g. 5-100/50/20/...)",
                 "2. Then, start finding the hidden number.",
                 Fore.LIGHTRED_EX + get_bold_text("Now, try It Yourself! 🔥🔥🔥", "RETURN") + Style.RESET_ALL)
        print(Fore.LIGHTRED_EX + "Click Enter to continue")
        input()
        for rule in rules:
            print(rule, end="")
            input()

    @staticmethod
    def header(banner, *args):
        bold_banner = get_bold_text(banner, "RETURN")
        print(Fore.RED + f"\n>>> {bold_banner}" + Style.RESET_ALL)
        for indx, arg in enumerate(list(args)):
            print(Fore.BLUE + f"{indx + 1}. {arg}")

    @staticmethod
    def error(*args):
        options = "/".join(list(args))
        bold_error = get_bold_text("Error:", "RETURN")
        bold_options = get_bold_text(options, "RETURN")
        print(Fore.LIGHTRED_EX + f">>> {bold_error}",
              Fore.LIGHTRED_EX + f"Please, select one of these options: {bold_options}" + Style.RESET_ALL)


class MusicPlayer(SystemVoice):

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

    def music_usage(self):
        answer = ""
        while answer not in ("AUDIO", "A", "BACK", "5"):
            self.header("Music", "Casual Jazz", "Energic Jazz", "Electric Jazz", "Turn Off", "Back")
            answer = input("<<< ")
            match answer.upper():
                case "CASUAL JAZZ" | "JAZZ 1" | "1":
                    pygame.mixer.music.stop()
                    self.casual_jazz()
                case "ENERGIC JAZZ" | "JAZZ 2" | "2":
                    pygame.mixer.music.stop()
                    self.cool_jazz()
                case "ELECTRIC JAZZ" | "JAZZ 3" | "3":
                    pygame.mixer.music.stop()
                    self.electric_jazz()
                case "TURN OFF" | "OFF" | "4":
                    pygame.mixer.music.stop()
                case "AUDIO" | "A"| "BACK" | "5":
                    pass
                case _:
                    self.error("CASUAL JAZZ", "ENERGIC JAZZ", "ELECTRIC JAZZ", "TURN OFF", "(BACK-Audio)")


music_player = MusicPlayer()


class SoundPlayer(SystemVoice):
    YOU_WIN = pygame.mixer.Sound("Sounds/ManVoiceYouWin.wav")
    YOU_LOST = pygame.mixer.Sound("Sounds/ManVoiceYouLose.mp3")

    def __init__(self):
        self.make_sound = True

    def turn_off_on_sound(self):
        answer = ""
        while answer not in ("AUDIO", "A", "BACK", "3"):
            self.header("Sounds", "Turn ON", "Turn Off", "Back")
            answer = input("<<< ")
            match answer.upper():
                case "TURN ON" | "ON" | "1":
                    print(Fore.LIGHTGREEN_EX + "Sounds are turned ON" + Style.RESET_ALL)
                    self.make_sound = True
                case "TURN OFF" | "OFF" | "2":
                    print(Fore.LIGHTRED_EX + "Sounds are turned OFF" + Style.RESET_ALL)
                    self.make_sound = False
                case "AUDIO" | "A" | "BACK" | "3":
                    pass
                case _:
                    self.error("TURN ON", "TURN OFF", "(Back-Audio)")


sound_player = SoundPlayer()


class Game(SystemVoice):

    def audio_settings(self):
        answer = ""
        while answer.upper() not in ("BACK", "SETTINGS", "3"):
            self.header("Audio", "Music", "Sounds", "Settings" + Style.RESET_ALL)

            answer = input("<<< ")
            match answer.upper():
                case "MUSIC" | "M" | "1":
                    music_player.music_usage()
                case "SOUNDS" | "S" | "2":
                    sound_player.turn_off_on_sound()
                case "SETTINGS" | "S" | "3":
                    pass
                case _:
                    self.error("MUSIC", "SOUNDS", "SETTINGS")

    def settings(self):
        answer = ""
        while answer.upper() not in ("BACK", "MAIN MENU", "3"):
            self.header("Settings", "Rules", "Audio", "Main Menu" + Style.RESET_ALL)

            answer = input("<<< ")
            match answer.upper():
                case "RULES" | "R" | "1":
                    self.how_to_play()
                case "AUDIO" | "A" | "2":
                    self.audio_settings()
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
                case "SETTINGS" | "S" | "1":
                    self.settings()
                case "PLAY" | "P" | "2":
                    self.coming_soon()
                case "QUIT" | "Q" | "3":
                    print(Fore.CYAN + ">>> Goodbye!" + Style.RESET_ALL)
                    time.sleep(0.5)
                case _:
                    self.error("SETTINGS", "PLAY", "QUIT")


game = Game()
game.main_menu()
