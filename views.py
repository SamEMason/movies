import datetime

from database import add_movie, watch_movie


Movies = list[tuple[str, float, str]]


def prompt_add_movie():
    display_heading("Add New Movie")

    title = input("Movie title: ")
    release_date = input("Release date (mm-dd-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%m-%d-%Y")

    timestamp = parsed_date.timestamp()

    add_movie(title, timestamp)


def prompt_watch_movie():
    display_heading("Watched Movie Selection")

    movie_title = input("Enter movie title you've watched: ")
    watch_movie(movie_title)


def display_movies(movies: Movies, heading: str, upcoming: bool = False):
    display_heading(heading)

    for movie in movies:
        title, release_date, _ = movie
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_readable_date = movie_date.strftime("%b %d, %Y")

        print(f"{title} (on {human_readable_date})", end="\n\n")

    print("----\n")


def display_heading(title: str):
    print(f"\n---- {title} ----\n")
