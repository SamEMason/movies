import datetime
import database


def prompt_add_movie():
    title = input("Movie title: ")
    release_date = input("Release date (dd-mm-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")

    timestamp = parsed_date.timestamp()

    database.add_movie(title, timestamp)
