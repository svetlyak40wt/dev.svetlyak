Title: Кусочки Python кода
Slug: pygist
Date: 2014-06-10 15:53
Category: texts
Tags: python, django
Lang: ru

Многие из нас наверняка пользуются какими-то кусочками кода, которые настолько малы,
что даже в библиотеку не заворачиваются, а копипастятся из проекта в проект.

Предлагаю в комментах к этому посту или твитах с тэгом [#pygist](https://twitter.com/hashtag/pygist)
поделиться такими полезняшками с миром.

Начну с себя.

Не знаю как у вас, а у меня часто в юниттестах возникает необходимость обновить
состояние объекта, получив новое из базы. Для этого я
[использую](https://gist.github.com/svetlyak40wt/15495ebf3092e2dd456c) такую вот простенькую функцию:

    :::python
    def refresh(obj):
        """Перезапрашивает объект из базы и возвращает новый инстанс."""
        return obj.__class__.objects.get(pk=obj.pk)

А вот и пример использования:

    :::python
    def test_some_functionality():
        foo = Foo.objects.create(name='foo')

        assert foo.name == 'foo'
        change_all_names_to('bar')

        foo = refresh(foo)
        assert foo.name == 'bar'

Лайк, ретвит и всяческий шэре.