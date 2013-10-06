Title: How to create a global lock using MySQL
Slug: how-create-global-lock-using-mysql
Date: 2008-12-02 20:17
Tags: mysql, tips, python
Category: texts
Lang: en
Description: A small example, how to use MySql's GET_LOCK in distributed environment.

When you writing a distributed application or webservice, sometimes you need to synchronize processes on different machines. For example, you may need to run some cron job once on a random machine.

If you are using MySQL, than you can ise it's [GET_LOCK][] function, to accomplish this task. I wrote this helper to create global lock in python, using `with` statement:

    :::python
    import contextlib
    @contextlib.contextmanager
    @write_session
    def global_lock(name, timeout, session):
        result = session.execute('SELECT GET_LOCK(%s, %s)', (name, timeout)).fetchall()
        result = len(result) == 1 and result[0][0]
        try:
            yield result and True or False
        finally:
            if result:
                session.execute('DO RELEASE_LOCK(%s)', (name, ))

Here `write_session` is decorator, which passes a `session` argument to a function. Here I use sqlalchemy's session, but you could use MySQLdb's connection or something like that.

And here is one of usecases for function:

    :::python
    def cron():
        with global_lock('myapp.cron_lock', 0) as acquired:
            if acquired:
                do_something_significant()
            else:
                exit_without_doing_any_job()

That's it. But make sure, to use unique name for the lock, because you may get in trouble if some other application uses same name.

[GET_LOCK]: http://dev.mysql.com/doc/refman/5.0/en/miscellaneous-functions.html#function_get-lock