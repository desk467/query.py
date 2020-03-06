from jinja2 import Template
from enum import Enum
from functools import wraps


class Types(Enum):
    SELECT = 1
    INSERT = 2
    UPDATE = 3
    DELETE = 4
    MANIPULATION = 5


def create_runner(cursor):
    def query(type):
        def _decorated(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                query_text = Template(func(*args, **kwargs))
                cursor.execute(query_text.render(**kwargs))

                collection = {
                    Types.SELECT: cursor.fetchall(),
                }

                return collection.get(type, None)
            return wrapper
        return _decorated

    return query
