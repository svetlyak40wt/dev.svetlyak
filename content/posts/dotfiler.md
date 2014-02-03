Title: Как правильно управлять конфигами?
Slug: dotfiler
Date: 2014-02-01 18:00
Category: texts
Tags: tools
Lang: ru

Помните, пару недель назад, я упоминал в своем твиттере [@svetlyak40wt](https://twitter.com/svetlyak40wt) о том, что начал писать собственное решение для конфигурации dot-файлов? Так вот, с тех пор я довел этот проект до вменяемого состояния, так что, встречайте — [dotfiler][]. Или коротко, просто `dot`.

Вы спросите зачем это, ведь есть уже [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh/), да и [крутая подборка конфигов](http://dotfiles.github.io/) от разных известных чуваков? Отвечу. Ни одно из найденных мною решений, не позволяет гибко и вместе с тем просто конфигурировать разные машины по-разному. Ключевое слово тут именно "по-разному". По-раз-но-му.

Дело в том, что у меня есть три вида конфигов:

* Первый — самые обычные, которыми можно поделиться на github. Всякие полезняшки для zsh, emacs, tmux, и тому подобное.
* Второй — приватные конфиги, с которые лучше не показывать никому. Тут всякие токены к амазонам, и тому подобные секретики. Такие вещи лучше хранить в приватном репозитории на своем сервере. 
* Третий вид — рабочие конфиги. Они сродни приватным, за тем лишь исключением, что нафиг не сдались мне на домашнем компьютере. И их лучше хранить в репозитории компании, а так же, ими можно и нужно делиться с коллегами. 

Как я уже сказал, ни одно из найденных мной решений, не позволяет отделить мух от котлет. Поэтому и был создан [dotfiler][].

Главную идею я почерпнул у [Зака Холлмана](http://zachholman.com/2010/08/dotfiles-are-meant-to-be-forked/) — разделять конфиги по направлениям деятельности: [редактор](http://zachholman.com/2010/08/dotfiles-are-meant-to-be-forked/), [среда разработки на python](https://github.com/svetlyak40wt/dot-python-dev), и т.д.. И dotfiler всецело способствует этой концепции, позволяя разделять не только zsh конфиги, но и вообще любые. Не только группировать их, но и хранить в разных git репозиториях. Директория с конфигами, сгруппированными по назначению, называется окружение, или просто env.

Но самое восхитительное то, как dotfiler работает с симлинками! Поскольку он позволяет разным окружениям иметь в своем составе конфиги для одной и той же директории, то ему надо уметь умно обрабатывать ситуации, когда таких файлов не было, а потом они вдруг появились. Это сложно воспринимается на словах, поэтому поясню на картинках. Слева изображены структура папок внутри `.dotfiles`, справа результат команды `dot update`. Стрелки же показывают куда ведут симлинки.  Кроме того, я буду приводить команды, так что вы сможете повторить все эти действия. Сделаем нечто вроде туториала. Команды будут содержать лишнюю опцию `--home-dir`. Она нужна лишь в учебных целях, чтобы производимые действия не конфликтовали с файлами вашей домашней директории. При реальном использовании, опцию `--home-dir` можно опустить. 

Итак, приступим:

    :::bash
    $ git clone https://github.com/svetlyak40wt/dotfiler .dotfiles
    $ export PATH=~/.test-dotfiles/bin:$PATH
    $ dot add https://github.com/svetlyak40wt/dot-zsh
    $ mkdir test-home
    $ dot update --home-dir=`pwd`/test-home
    LINK   Symlink from /Users/art/test-home/.bash_profile to /Users/art/.dotfiles/zsh/.bash_profile was created
    LINK   Symlink from /Users/art/test-home/.zsh to /Users/art/.dotfiles/zsh/.zsh was created
    LINK   Symlink from /Users/art/test-home/.zshrc to /Users/art/.dotfiles/zsh/.zshrc was created

![](http://img-fotki.yandex.ru/get/9895/13558447.f/0_aa14f_4f5befb1_L.jpg)

На этом рисунке видно, что мы склонировали окружение с конфигами для zsh. Их много, но dotfiler залинковал только `.zsh` и `.zshrc`, чтобы не делать лишней работы. 

    :::bash
    $ dot add svetlyak40wt/dot-tmux
    $ dot update --home-dir=`pwd`/test-home                                                                                 b:master s:
    LINK  Symlink from /Users/art/test-home/.bin to /Users/art/.dotfiles/tmux/.bin was created
    LINK  Symlink from /Users/art/test-home/.tmux.conf to /Users/art/.dotfiles/tmux/.tmux.conf was created
    RM    Symlink /Users/art/test-home/.zsh was removed.
    MKDIR Directory /Users/art/test-home/.zsh was created.
    LINK  Symlink from /Users/art/test-home/.zsh/00-options to /Users/art/.dotfiles/zsh/.zsh/00-options was created
    LINK  Symlink from /Users/art/test-home/.zsh/01-prompt-functions to /Users/art/.dotfiles/zsh/.zsh/01-prompt-functions was created
    LINK  Symlink from /Users/art/test-home/.zsh/02-prompt-colors to /Users/art/.dotfiles/zsh/.zsh/02-prompt-colors was created
    LINK  Symlink from /Users/art/test-home/.zsh/03-prompt to /Users/art/.dotfiles/zsh/.zsh/03-prompt was created
    LINK  Symlink from /Users/art/test-home/.zsh/aliases to /Users/art/.dotfiles/zsh/.zsh/aliases was created
    LINK  Symlink from /Users/art/test-home/.zsh/ash to /Users/art/.dotfiles/zsh/.zsh/ash was created
    LINK  Symlink from /Users/art/test-home/.zsh/dotfiler to /Users/art/.dotfiles/zsh/.zsh/dotfiler was created
    LINK  Symlink from /Users/art/test-home/.zsh/ssh-agent to /Users/art/.dotfiles/zsh/.zsh/ssh-agent was created
    LINK  Symlink from /Users/art/test-home/.zsh/tmux to /Users/art/.dotfiles/tmux/.zsh/tmux was created

![](http://img-fotki.yandex.ru/get/9314/13558447.f/0_aa150_6aa53046_L.jpg)

Теперь мы добавили еще одно окружение, конфигурирующее tmux. Оно так же содержит конфиг для zsh, поэтому линковать его в папку `.zsh`, которая и так является симлинком, будет неправильно. Поэтому dotfiler убирает этот симлинк, создает вместо него нормальную директорию, и уже туда линкует все нужные конфиги. 

Такого не умеет никто. Никто!

Разумеется, вся логика покрыты тестами. Но гонялись они пока только на python 2.7. Если будут проблемы, файлите ишьюсы, реквесьте пуллы :)

P.S. — маленькая хитрость для тех, кто дочитал. Команда `dot add` может принимать более одной ссылки на репозиторий.  
P.P.S. — зацепите команду `dot status`, она тоже клевая!

[dotfiler]: https://github.com/svetlyak40wt/dotfiler