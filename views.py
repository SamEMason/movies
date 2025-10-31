import datetime

from database import add_movie, get_movies


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")

    timestamp = parsed_date.timestamp()

    add_movie(title, timestamp)


def display_movies(upcoming: bool = False):
    movies = get_movies(upcoming)
    print()

    for movie in movies:
        title, release_date, watched = movie

        print(title)
        print(release_date)
        print("watched" if watched else "not watched", end="\n\n")

