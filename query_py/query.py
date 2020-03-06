from jinja2 import Template
from enum import Enum
from functools import wraps


class Types(Enum):
    SELECT = 1
    INSERT = 2
    UPDATE = 3
    DELETE = 4
    MANIPULATION = 5


def get_collection(cursor):
    '''
    `get_collection` returns an generator that yields
    all items `cursor` has
    '''

    while item:= cursor.fetchone(): # noqa
        yield item


def create_runner(cursor):
    '''
    `create_runner` generates a decorator function that is responsible
    for creating functions that can query on database without calling
    cursor directly.
    '''
    def query(type):
        def _decorated(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                query_text = Template(func(*args, **kwargs))
                cursor.execute(query_text.render(**kwargs))

                collection = {
                    Types.SELECT: get_collection(cursor),
                }

                return collection.get(type, None)
            return wrapper
        return _decorated

    return query
