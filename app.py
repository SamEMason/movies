import database

from menu import ACTIONS, MENU
from views import (
    display_movies,
    display_movie_watchlist,
    prompt_add_movie,
    prompt_watch_movie,
)


welcome = "Welcome.\n"

print(welcome)
database.create_tables()

while (user_input := input(MENU)) != ACTIONS["EXIT"]:

    if user_input == ACTIONS["ADD_MOVIE"]:
        prompt_add_movie()

    elif user_input == ACTIONS["VIEW_UPCOMING_MOVIES"]:
        upcoming_movies = database.get_movies(upcoming=True)
        display_movies(movies=upcoming_movies, heading="Upcoming Movies", upcoming=True)

    elif user_input == ACTIONS["VIEW_ALL_MOVIES"]:
        all_movies = database.get_movies(upcoming=False)
        display_movies(movies=all_movies, heading="All Movies")

    elif user_input == ACTIONS["WATCH_MOVIE"]:
        prompt_watch_movie()

    elif user_input == ACTIONS["VIEW_WATCHED_MOVIES"]:
        username = input("Enter username: ")
        watched_movies = database.get_watched_movies(username)
        display_movie_watchlist(username, watched_movies)

    else:
        print("Selected option is invalid.")
