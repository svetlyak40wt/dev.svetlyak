Title: Code Reloader
Slug: code-reloader
Date: 2012-10-26 11:53
Category: posts
Tags: libraries, python
Lang: ru

Полезная фича многих веб-фрейморков — перезагрузка кода налету, сразу по изменении
кода. Большинство фреймворков таскают такие перезагрузчики в своей кодобазе и
нет нормального отдельного модуля, позволяющего легко и просто получить
такую функциональность в своем маленьком сервере.

Некоторое время назад я начал писать своего чатбота [TheBot][] и стал подыскивать варианты,
как бы и в нем сделать перезагрузку по изменению кода. Да так и не нашел
готовой библиотки.

Тогда я выпилил модуль autoreload из Django, и оформил его в виде отдельной библиотеки.
Так и родился модуль [server-reloader][].

Большую часть кода я отрефакторил. Временно выкинул поддержку JPython. Избавился от лишних
глобальных переменных. Но самое главное, теперь перезагрузку можно выполнять не только
по изменнию файлов, но и пол любому внешнему событию — достаточно лишь вызвать одну функцию.

Перезагрузка по внешнему событию позволила реализовать в [TheBot][] интересную штуку —
теперь он может обновлять сам себя по коммиту в GitHub. Чекаутить изменения, устанавливать
новые зависимости прогонять тесты, и только потом уже перезагружаться:

    def on_push_to_the_github_master_branch():
        make_git_pull()
        run_pip_install()
        if tests_ok():
            trigger_code_reload()
        else:
            report_about_problem()

И все это бот будет делать сам, ему не нужны никакие внешние вотчдоги.

А вот так можно использовать [server-reloader][] в вашем собственном проекте:

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


А если надо по событию код перезагрузить, то:

    :::python
    from server_reloader import trigger_reload
    trigger_reload()

Короче, качайте либу с PyPy, или форкайте [на GitHub][server-reloader]. Надеюсь, что кому-нибудь она окажется полезна!

[TheBot]: http://github.com/svetlyak40wt/thebot
[server-reloader]: http://github.com/svetlyak40wt/server-reloader
