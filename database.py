import datetime
import sqlite3

from queries import (
    CREATE_MOVIES_TABLE,
    INSERT_MOVIES,
    SELECT_ALL_MOVIES,
    SELECT_UPCOMING_MOVIES,
    SELECT_WATCHED_MOVIES,
    SET_MOVIE_WATCHED,
)


connection = sqlite3.connect("data.db")


def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)


def add_movie(title: str, release_timestamp: float):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming: bool = False):
    with connection:
        cursor = connection.cursor()

        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)

        return cursor.fetchall()


def watch_movie(title: str):
    with connection:
        connection.execute(SET_MOVIE_WATCHED, (title,))


def get_watched_movie():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES)
        return cursor.fetchall()
