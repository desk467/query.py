from query_py.query import create_runner, Types
from random import choice
import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()
query = create_runner(cursor)


@query(Types.MANIPULATION)
def create_user_table():
    return '''
    create table if not exists user (
        id integer not null primary key autoincrement,
        name varchar(50) not null,
        age int not null
    )
    '''


@query(Types.SELECT)
def get_users():
    return '''
    select
        id,
        name,
        age
    from user
    '''


@query(Types.SELECT)
def get_user_by_id(user_id):
    return '''
        select 
            id,
            name,
            age
        from user
        where id = {{ user_id }}
    '''


@query(Types.INSERT)
def create_user(name, age):
    return '''
        insert
        into
            user (name, age)
        values (
            "{{ name }}",
            {{ age }}
        )
    '''


create_user_table()
create_user(name='Lia', age=33)
create_user(name='Roberto', age=25)
create_user(name='Carlos', age=55)

print("All items:")
print('ID\tNAME\t\tAGE')
for id, name, age in get_users():
    print(f'{id}\t{name}\t\t{age}')


print("\nPicking one:")
print(choice(list(get_users())))
