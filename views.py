import datetime

from database import add_movie, get_movies


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (mm-dd-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%m-%d-%Y")

    timestamp = parsed_date.timestamp()

    add_movie(title, timestamp)


def display_movies(upcoming: bool = False):
    movies = get_movies(upcoming)

    title = "Upcoming Movies" if upcoming else "All Movies"
    display_heading(title)

    for movie in movies:
        title, release_date, watched = movie

        print(title)
        print(release_date)
        print("watched" if watched else "not watched", end="\n\n")

    print("----\n")


def display_heading(title: str):
    print(f"\n---- {title} ----\n")
