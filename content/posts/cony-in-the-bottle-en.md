Title: Cony in the Bottle
Slug: cony-in-the-bottle
Date: 2011-02-01 00:35
Category: texts
Tags: python
Lang: en

Two weeks ago, in the "[Command Line for the Internet][bunny1]" post, I wrote about useful smart bookmarks service.

Digging into a code of the project, I figured out that it is too complex for such trivial idea. And of course I've decided to rewrite it :-)

My own [fork][cony] is called Cony that is a synonym for Bunny.

![](http://img-fotki.yandex.ru/get/5800/alexander-artemenko.e/0_735d1_b947df73_L)  
by [animalvegetable@flickr](http://flic.kr/p/6bLmMR)

And if Bunny1 has a dependency from heavy CherryPy, then Cony is much more modest. It uses a micro-framework [Bottle][]. Bottle, is only a python file committed right into the repository.

Extend
------

Because there are not dependencies, installation is quite simple — just clone a repository and run `./cony.py`. Adding your own shortcuts is trivial as well — it is enough to create a `local_commands.py` file in the current directory. Some examples already in `examples` directory, ready to import into the `local_commands.py` file. Just do `from examples import *` to plug them all or import each function separately.

Clone & Share
-------------

If you wrote an interesting shortcut don't be lazy, fork the project on GitHub, put your command into `examples` and send me a Pull Request.

A little about the Bottle
-------------------------

I liked the Bottle. It is minimalistic. There are url router and templates built-in. Of course you are able to use any other template engine and ORM. For small projects, like Cony it suits very well.

[bottle]: http://github.com/defnull/bottle
[bunny1]: http://dev.svetlyak.ru/facebook-bunny1/
[cony]: http://github.com/svetlyak40wt/cony/

