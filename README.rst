query.py
========

A wrapper over database drivers for improving SQL experience with Python.

Usage
-----

::

    @query(Types.SELECT)
    def get_users():
        return '''
        select
            id,
            name,
            age
        from user
        '''

    for id, name, age in get_users():
        # Do some stuff...