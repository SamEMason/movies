import datetime

from database import add_movie, get_movies, get_watched_movies, watch_movie


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (mm-dd-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%m-%d-%Y")

    timestamp = parsed_date.timestamp()

    add_movie(title, timestamp)


def prompt_watch_movie():
    movie_title = input("Enter movie title you've watched: ")
    watch_movie(movie_title)


def display_movies(upcoming: bool = False):
    movies = get_movies(upcoming)

    title = "Upcoming Movies" if upcoming else "All Movies"
    display_heading(title)

    for movie in movies:
        title, release_date, _ = movie
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_readable_date = movie_date.strftime("%b %d, %Y")

        print(f"{title} (on {human_readable_date})", end="\n\n")

    print("----\n")


def display_watched_movies():
    watched_movies = get_watched_movies()

    title = "Watched Movies"
    display_heading(title)

    for movie in watched_movies:
        title, release_date, _ = movie
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_readable_date = movie_date.strftime("%b %d, %Y")

        print(f"{title} (on {human_readable_date})", end="\n\n")

    print("----\n")


def display_heading(title: str):
    print(f"\n---- {title} ----\n")
