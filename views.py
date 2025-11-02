import datetime

from database import add_movie, watch_movie


Movies = list[tuple[str, float]]
Watchlist = list[tuple[str, str]]


def prompt_add_movie():
    display_heading("Add New Movie")

    title = input("Movie title: ")
    release_date = input("Release date (mm-dd-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%m-%d-%Y")

    timestamp = parsed_date.timestamp()

    add_movie(title, timestamp)


def prompt_watch_movie():
    display_heading("Watched Movie Selection")

    username = input("Enter username: ")
    movie_title = input("Enter movie title you've watched: ")
    watch_movie(movie_title, username)


def display_movies(movies: Movies, heading: str, upcoming: bool = False):
    display_heading(heading)

    if len(movies) > 0:
        for movie in movies:
            title, release_date = movie
            movie_date = datetime.datetime.fromtimestamp(release_date)
            human_readable_date = movie_date.strftime("%b %d, %Y")

            print(f"{title} (on {human_readable_date})", end="\n\n")
    else:
        print("Movie List is empty.", end="\n\n")
    display_footer()


def display_movie_watchlist(username: str, movies: Watchlist):
    display_heading(f"{username}'s Watched Movies")

    if len(movies) > 0:
        for movie in movies:
            _, title = movie
            print(title, end="\n\n")
    else:
        print("Watchlist is empty.", end="\n\n")

    display_footer()


def display_heading(title: str):
    print(f"\n---- {title} ----\n")


def display_footer():
    print("----\n")
