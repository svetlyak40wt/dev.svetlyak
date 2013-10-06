Title: Учусь пользоваться MacPorts
Slug: learning-macports
Date: 2010-07-12 08:03
Category: texts
Tags: mac-os-x
Lang: ru

Учусь пользоваться MacPorts.

Уже выучил, что надо подчищать старые версии портов (освободил несколько
гигабайт места на диске):

    port -u uninstall

И можно удалять порт и все порты, что от него зависят, например:

    port uninstall --follow-dependents gtk2

