import database

from menu import ACTIONS, MENU
from views import prompt_add_movie


welcome = "Welcome."

print(welcome)
database.create_tables()

while (user_input := input(MENU)) != ACTIONS["EXIT"]:
    if user_input == ACTIONS["ADD_MOVIE"]:
        prompt_add_movie()
    elif user_input == ACTIONS["VIEW_UPCOMING_MOVIES"]:
        pass
    elif user_input == ACTIONS["VIEW_ALL_MOVIES"]:
        pass
    elif user_input == ACTIONS["WATCH_MOVIE"]:
        pass
    elif user_input == ACTIONS["VIEW_WATCHED_MOVIES"]:
        pass
    else:
        print("Selected option is invalid.")
