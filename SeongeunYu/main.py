# -*- coding:utf-8 -*-
from game_lib.Menu import *


if __name__ == "__main__":
    while True:
        Menu.print_menu()
        input_val = input()
        if input_val == "1":
            Menu.start_game()
        elif input_val == "2":
            Menu.show_ranking()
        elif input_val == "3":
            Menu.exit_game()
        else:
            print("[x] error: invalid value... please try again.")
