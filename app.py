import database

from menu import ACTIONS, MENU
from views import (
    display_movies,
    display_watched_movies,
    prompt_add_movie,
    prompt_watch_movie,
)


welcome = "Welcome."

print(welcome)
database.create_tables()

while (user_input := input(MENU)) != ACTIONS["EXIT"]:
    if user_input == ACTIONS["ADD_MOVIE"]:
        prompt_add_movie()
    elif user_input == ACTIONS["VIEW_UPCOMING_MOVIES"]:
        display_movies(upcoming=True)
    elif user_input == ACTIONS["VIEW_ALL_MOVIES"]:
        display_movies()
    elif user_input == ACTIONS["WATCH_MOVIE"]:
        prompt_watch_movie()
    elif user_input == ACTIONS["VIEW_WATCHED_MOVIES"]:
        display_watched_movies()
    else:
        print("Selected option is invalid.")
