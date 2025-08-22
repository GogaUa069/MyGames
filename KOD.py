from colorama import Fore, Style
from random import shuffle
from pygame import mixer, Sound, init
import time

init()


class AudioPlayer:

    def __init__(self):
        self.FOREST_SOUNDTRACK = "ForestSoundtrack.wav"
        self.CAVE_CHOICE_SCREAMER = Sound("Audio/CaveChoiceScreamer.wav")
        self.STEPS = Sound("Audio/Steps.wav")  # MAXTIME: 2670
        self.HEARTBEAT = Sound("Audio/HeartBeat.wav")  # MAXTIME: 3500
        self.INTRIGUE_SOUND = Sound("Audio/IntrigueSound.wav") # MAXTIME: 4000
        self.DEATH_SOUND = Sound("Audio/DeathSound.wav")
        self.END_GAME_SOUND = Sound("Audio/EndGameSound.wav")
        self.THE_END_SOUNDTRACK = "EndMusic.wav"

    @staticmethod
    def play_soundtrack(soundtrack, is_infinity=False):
       mixer.music.load("Audio/"+soundtrack)
       mixer.music.play(-1) if is_infinity else mixer.music.play()


class Game(AudioPlayer):
    ENDINGS = {"GOOD": Fore.LIGHTGREEN_EX + "...shares his treasures with You!",
               "BAD": Fore.LIGHTRED_EX + "...instantly eats You up!"}

    INTRO = (Fore.BLUE + "You are in a land inhabited by dragons.", "You see two caves in front of You.",
             "In one of them, a friendly dragon is waiting to give You some treasure.",
             "In the second, a wicked and hungry dragon waits, ready to eat you!",
             "But You don't know which dragon is in which cave." + Style.RESET_ALL)

    def __init__(self):
        AudioPlayer.__init__(self)
        self.true_ending = None

    def get_intro(self):
        print(Fore.LIGHTRED_EX + "\nClick Enter to continue")
        input()
        self.play_soundtrack(self.FOREST_SOUNDTRACK, True)
        for text in self.INTRO:
            print(text, end="")
            input()
        mixer.music.stop()

    def cave_choice(self):
        ending_list = list(self.ENDINGS.keys())
        shuffle(ending_list)
        self.CAVE_CHOICE_SCREAMER.play()

        answer = ""
        while answer.upper() not in ("LEFT", "RIGHT", "1", "2"):
            print(Fore.LIGHTRED_EX + "\nWhich cave will You choose?" + Style.RESET_ALL)
            answer = input("<<< ")
            match answer.upper():
                case "LEFT" | "1":
                    self.true_ending = self.ENDINGS[ending_list[0]]
                case "RIGHT" | "2":
                    self.true_ending = self.ENDINGS[ending_list[1]]
                case _:
                    print(Fore.LIGHTRED_EX + "Please, enter LEFT/RIGHT" + Style.RESET_ALL)

    def ending_checking(self):
        self.END_GAME_SOUND.play()
        print(self.true_ending)

        if self.true_ending == self.ENDINGS["BAD"]:
            time.sleep(1.5)
            self.DEATH_SOUND.play()

        time.sleep(0.5)

    def choice_intrigue(self):
        print(Fore.LIGHTWHITE_EX + "You're moving toward the cave...")
        self.STEPS.play(maxtime=2670)
        time.sleep(2.67)
        print("Its darkness makes You tremble with fear...")
        self.HEARTBEAT.play(maxtime=3500)
        time.sleep(3.5)
        print("The big dragon jumps in front of you. He opens his big jaws and...")
        self.INTRIGUE_SOUND.play(maxtime=4000)
        time.sleep(4)
        self.ending_checking()
        time.sleep(3)
        print("\nThe End!\n" + Style.RESET_ALL)

    def game(self):
        self.__init__()
        self.get_intro()
        self.cave_choice()
        self.choice_intrigue()


game_class = Game()

def game():
    def goodbye_func(laugh_t, fadeout_t):
        laugh_sound.play()
        print(Fore.LIGHTCYAN_EX + "Goodbye!)" + Style.RESET_ALL)
        time.sleep(laugh_t / 1000)
        laugh_sound.fadeout(1500)
        time.sleep(fadeout_t / 1000)

    laugh_sound = Sound("Audio/Laugh.wav")  # MAXTIME: 3000
    laugh_time = 3000
    fadeout_time = 1500
    answer = ""
    print(Fore.CYAN + "Welcome to the Kingdom of Dragons!" + Style.RESET_ALL)

    while answer.upper() not in ("ESCAPE", "2"):
        print("1. Try Your luck\n"
              "2. Make a miserable escape")
        answer = input("<<< ")
        match answer.upper():
            case "TRY LUCK" | "TRY" | "1":
                game_class.game()
            case "ESCAPE" | "2":
                goodbye_func(laugh_time, fadeout_time)
            case _:
                print(Fore.LIGHTRED_EX + "Please, enter TRY LUCK or ESCAPE\n" + Style.RESET_ALL)

game()
