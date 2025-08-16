# Get adventure LVL6 in uncommon levels
# Get one func for searching numbers *answers
# Change the HARD LVL

from colorama import Fore, Style
from random import randint
from time import sleep


class Monologues:
    how_to_play_info = ("\n@GogaUa096 Follow me on instagram :)\n\nHow to play:",
                        Fore.BLUE + "Task: To find the number guessed by the computer.",
                        "1. Enter the range in which you will search for the number. (The range 5-100)",
                        "2. Then, start find number." + Style.RESET_ALL,
                        Fore.RED + "Now, try it yourself!\n" + Style.RESET_ALL)
    types_of_levels = {"LVL1: LITE": "You've unlimited lives! Good way for beginners.",
                       "LVL2: MEDIUM": "The number of lives is set of depending on the size of the range. "
                                       "Suitable for average players.",
                       "LVL3: HARD": "Medium level, but with... TIME! You have only 30 seconds! Only for advanced players!",
                       "LVL4: MEGA": "There are 2 numbers! Unlocks after 3 wins at LVL3.",
                       "LVL5: RANDOM": "Random number of lives, border and time for finding! "
                                       "If you win this mode, you can consider yourself a PRO!, ",
                       "LVL6: ADVENTURE": "Win all the COMMON levels in a row and get prize!\n"}

    @staticmethod
    def long_get_info(text):
        list_items = list(text.items())
        print(Fore.LIGHTBLUE_EX + "Common levels:" + Style.RESET_ALL)
        for key, value in list_items[:3]:
            print(key, value, sep=" - ")
            sleep(0.7)
        print(Fore.LIGHTGREEN_EX + "\nUncommon levels:" + Style.RESET_ALL)
        for key, value in list_items[3:5]:
            print(key, value, sep=" - ")
            sleep(0.7)
        print(Fore.LIGHTYELLOW_EX + "\nLegendary levels:" + Style.RESET_ALL)
        for key, value in list_items[5:]:
            print(key, value, sep=" - ")
            sleep(0.7)

    @staticmethod
    def short_get_info(text):
        for i in text:
            print(i)
            sleep(0.7)


monologues = Monologues()
monologues.short_get_info(monologues.how_to_play_info)
win_streak = 0


class GetData:
    def __init__(self):
        self.hard_win_counter = 0
        self.difficulty_lvl = str
        self.last_game = None
        self.win_streak = 0
        self._is_used_promo = False

    def get_difficulty_lvl(self):
        acceptable_types = list()
        print("Please, select game type:\n")
        monologues.long_get_info(monologues.types_of_levels)
        if self.hard_win_counter < 3:
            acceptable_types = ["lite", "medium", "hard", "random", "adventure"]
        else:
            acceptable_types.insert(3, "mega")
        while self.difficulty_lvl.lower not in acceptable_types:
            self.difficulty_lvl = input("-----> ")
            match self.difficulty_lvl.lower():
                case "lite" | "1":
                    self.last_game = lite_game_func
                    lite_game_func()
                    break
                case "medium" | "2":
                    self.last_game = medium_game_func
                    medium_game_func()
                    break
                case "hard" | "3":
                    self.last_game = hard_game_func
                    hard_game_func()
                    break
                case "mega" | "4":
                    if self.hard_win_counter < 3:
                        print("You should win 3 times in LVL3\n")
                    else:
                        print("Coming soon! :D\n")  # <----------------------- Add Mega LVL
                case "random" | "5":
                    print("Coming soon!\n")  # <----------------------- Add Random LVl
                case "adventure" | "6":
                    print("Coming soon!\n")  # <------------------------- Add Adventure LVL
                case "mswde096" | "096":
                    print(Fore.LIGHTRED_EX + "Yey! You used promo-code! Now You have +10.000 lives!" + Style.RESET_ALL)
                    self._is_used_promo = True
                case _:
                    print(f"Please, use: {Fore.LIGHTRED_EX + ", ".join(acceptable_types).upper() + Style.RESET_ALL}\n"
                          f"Or enter number in range 1-6\n")

    def is_mega_unlocked(self):
        if self.hard_win_counter == 3:
            print("You've unlocked the MEGA (4) LVL!")
        else:
            print(f"You've to win {3-data1.hard_win_counter} time(s) in HARD LVL to get MEGA\n")


class LiteGame(GetData):
    ACCEPTABLE_RANGE = range(5, 101)

    def __init__(self):
        self._border = self._hidden_number = self._number = self._attempts_counter = 0
        GetData.__init__(self)

    def get_border(self):
        print("Select the border.\nEnter total in range 5-100\n")
        while self._border not in self.ACCEPTABLE_RANGE:
            try:
                self._border = int(input("-----> "))
                if self._border not in self.ACCEPTABLE_RANGE:
                    print("Your total is out of range!\nPlease, use digits in range 5-100\n")
                else:
                    self._hidden_number = randint(1, self._border)
            except ValueError:
                print("Your input is not digit!\nPlease, use only DIGITS!\n")

    def number_searching(self):
        global win_streak
        acceptable_border = range(1, self._border+1)
        print(f"Well, lets find the hidden number!\nEnter total in range 1-{self._border}\n")
        while self._number != self._hidden_number:
            try:
                self._number = int(input("-----> "))
                if self._number not in acceptable_border:
                    print(f"Your total is out of range!\nPlease, use digits in range 1-{self._border}\n")
                else:
                    if self._number < self._hidden_number:
                        print("Your total is SMALLER than hidden number!\n")
                        self._attempts_counter += 1
                    elif self._number > self._hidden_number:
                        print("Your total is BIGGER than hidden number!\n")
                        self._attempts_counter += 1
                    else:
                        print(f"{"\033[31m{}".format("Yey! You found the hidden number!")}")
                        if self._attempts_counter == 1:
                            print(f"{"\033[31m{}".format(f"It took {self._attempts_counter} attempt.")}\n")
                        elif self._attempts_counter == 0:
                            print(f"{"\033[31m{}".format(f"It took {self._attempts_counter} attempts!")}")
                            print("WOW! Scientists have to check your brain!\n")
                        else:
                            print(f"{"\033[31m{}".format(f"It took {self._attempts_counter} attempts.")}\n")
                        win_streak += 1
                        print(f"Your win streak: {win_streak}\n")
                        self.__init__()
                        break
            except ValueError:
                print("Your total is not digit!\nPlease, use only DIGITS!\n")


class MediumGame(GetData):
    ACCEPTABLE_RANGE = range(5, 101)

    def __init__(self):
        self._border = self._hidden_number = self._number = self._attempts_counter = self._attempts_limit = 0
        GetData.__init__(self)
        if self._is_used_promo:
            self._attempts_limit += 10000

    def get_border(self):
        print("Select the border.\nEnter total in range 5-100\n")
        while self._border not in self.ACCEPTABLE_RANGE:
            try:
                self._border = int(input("-----> "))
                if self._border not in self.ACCEPTABLE_RANGE:
                    print("Your total is out of range!\nPlease, use digits in range 5-100\n")
                else:
                    self._hidden_number = randint(1, self._border)
            except ValueError:
                print("Your input is not digit!\nPlease, use only DIGITS!\n")

    def get_attempts_limit(self):
        num = self._border
        counter = 0
        while num != 1:
            num //= 2
            counter += 1
        self._attempts_limit = counter + 1

    def number_searching(self):
        global win_streak
        acceptable_border = range(1, self._border+1)
        print(f"Well, lets find the hidden number!\n"
              f"Enter total in range 1-{self._border}\n"
              f"Be careful, you have only {self._attempts_limit} lives!\n")
        while True:
            try:
                self._number = int(input("-----> "))
                if self._number not in acceptable_border:
                    print(f"Your total is out of range!\nPlease, use digits in range 1-{self._border}\n")
                else:
                    if self._number > self._hidden_number:
                        print("Your number is BIGGER than hidden number!")
                        self._attempts_counter += 1
                        print(f"You have {self._attempts_limit - self._attempts_counter} attempts\n")
                    elif self._number < self._hidden_number:
                        print("Your number is SMALLER than hidden number!")
                        self._attempts_counter += 1
                        print(f"You have {self._attempts_limit - self._attempts_counter} attempts\n")
                    else:
                        print(f"{"\033[31m{}".format("Yey! You found the hidden number!")}")
                        if self._attempts_counter == 1:
                            print(f"{"\033[31m{}".format(f"It took {self._attempts_counter} attempt.")}\n")
                        elif self._attempts_counter == 0:
                            print(f"{"\033[31m{}".format(f"It took {self._attempts_counter} attempts!")}")
                            print("Let's go! It was too easy for you!\n")
                        else:
                            print(f"{"\033[31m{}".format(f"It took {self._attempts_counter} attempts.")}\n")
                        win_streak += 1
                        print(f"Your win streak: {win_streak}\n")
                        self.__init__()
                        break
                if self._attempts_counter == self._attempts_limit:
                    print("\033[31m{}".format("You've reached the maximum number of attempts!\nYou lost!\n"))
                    if win_streak != 0:
                        print("You lost your win streak\n")
                    win_streak = 0
                    self.__init__()
                    break
            except ValueError:
                print("Your input is not digit!\nPlease, use only DIGITS!\n")


class HardGame(GetData):
    ACCEPTABLE_BORDER = range(1, 101)

    def __init__(self):
        self.__border = 100
        self._hidden_number = self._number = self._attempts_counter = 0
        GetData.__init__(self)

    def number_searching(self):
        global win_streak
        print("Well, lets find the hidden number!\n"
              "Enter total in range 1-100\n"
              "\n(Be careful, you have only 30 seconds!)\n")
        self._hidden_number = randint(1, self.__border)

        while True:
            try:
                self._number = int(input("-----> "))
                if self._number not in self.ACCEPTABLE_BORDER:
                    print("Your total is out of range!\nPlease, use digits in range 1-100\n")
                else:
                    if self._number > self._hidden_number:
                        print("Your number is BIGGER than hidden number!")
                        self._attempts_counter += 1
                        print(f"You have {6 - self._attempts_counter} attempts\n")
                    elif self._number < self._hidden_number:
                        print("Your number is SMALLER than hidden number!")
                        self._attempts_counter += 1
                        print(f"You have {6 - self._attempts_counter} attempts\n")
                    else:
                        print(f"{"\033[31m{}".format("Yey! You found the hidden number!")}")
                        if self._attempts_counter == 1:
                            print(f"{"\033[31m{}".format(f"It took {self._attempts_counter} attempt.")}\n")
                        elif self._attempts_counter == 0:
                            print(f"{"\033[31m{}".format(f"It took {self._attempts_counter} attempts!")}")
                            print("Well done! It was too easy for you!\n")
                        else:
                            print(f"{"\033[31m{}".format(f"It took {self._attempts_counter} attempts.")}\n")
                        data1.hard_win_counter += 1
                        self.is_mega_unlocked()
                        win_streak += 1
                        print(f"Your win streak: {win_streak}\n")
                        self.__init__()
                        break
                if self._attempts_counter == 6:
                    print("\033[31m{}".format("You've reached the maximum number of attempts!\nYou lost!\n"))
                    if win_streak != 0:
                        print("You lost your win streak!\n")
                    win_streak = 0
                    self.__init__()
                    break
            except ValueError:
                print("Your input is not digit!\nPlease, use only DIGITS!\n")


class MegaGame(GetData):
    pass


my_mega_game = MegaGame()


def lite_game_func():
    print(Fore.RED + "Lite Level:" + Style.RESET_ALL)
    my_lite_game = LiteGame()
    my_lite_game.get_border()
    my_lite_game.number_searching()


def medium_game_func():
    print(Fore.RED + "Medium Level:" + Style.RESET_ALL)
    my_medium_game = MediumGame()
    my_medium_game.get_border()
    if not data1._is_used_promo:
        my_medium_game.get_attempts_limit()
    my_medium_game.number_searching()


def hard_game_func():
    print(Fore.RED + "Hard Level:" + Style.RESET_ALL)
    my_hard_game = HardGame()
    my_hard_game.number_searching()


def mega_game_func():
    pass


data1 = GetData()
game_starting = data1.get_difficulty_lvl
game_starting()


def restart():
    answer = str
    acceptable_answers = ("restart", "leave", "another", "1", "2", "3")
    while answer.lower not in acceptable_answers:
        print("\033[0m{}".format("Do you wanna play again?\n"
                                 "RESTART - restart LVL\n"
                                 "ANOTHER - another LVL\n"
                                 "LEAVE - leave game\n"))
        answer = input("-----> ")
        match answer.lower():
            case "restart" | "1":
                data1.last_game()
            case "another" | "2":
                game_starting()
            case "leave" | "3":
                print(Fore.BLUE + "Goodbye!")
                sleep(0.5)
                break
            case _:
                print("Please, enter RESTART, ANOTHER or LEAVE.\n")


restart()
