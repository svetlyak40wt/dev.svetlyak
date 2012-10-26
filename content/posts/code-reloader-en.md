Title: Code Reloader
Slug: code-reloader
Date: 2012-10-26 11:53
Category: posts
Tags: libraries, python
Lang: en

It is common task in all web frameworks — to provide an easy way to reload development
server on code changes. Most of these frameworks are carrying a reloader's code with
themselves. And there isn't any python module, simple enougth to use in a small project.

Some times ago, I started to write a chat bot called [TheBot][] and begun to look for
a separate server reloader's implementation. And found nothing suitable.

Then, I extracted autoreloader from the Django's codebase and put it into a separate
module. That is how [server-reloader][] was born.

Code was partly modified. Now it allows not only to watch on file changes but also to
reload upon a some event.

Reload on some event is a quite useful feature for [TheBot][], because now he can update
himself on a push to the GitHub. A pseudocode for this procedure will look like:

    :::python
    def on_push_to_the_github_master_branch():
        make_git_pull()
        run_pip_install()
        if tests_ok():
            trigger_code_reload()
        else:
            report_about_problem()

And I don't need an external watcher to run bot, because now he uses [server-reloader][].

Here is a example code, showing how to use server reloader in your own project.

    :::python
    def run_server():
        """some function, which creates and runs your server."""
        pass

    def main():
        server_reloader.main(
            run_server,
            before_reload=lambda: print('reloading code…')
        )

    if __name__ == '__main__':
        main()


If you want to trigger code reloading on some custom event, then just do:

    :::python
    from server_reloader import trigger_reload
    trigger_reload()

Download it from PyPy, for it [on GitHub][server-reloader].

[TheBot]: http://github.com/svetlyak40wt/thebot
[server-reloader]: http://github.com/svetlyak40wt/server-reloader
