Title: DjangoDash results
Slug: djangodash-results
Date: 2009-06-01 23:45
Tags: django, contest, jquery
Category: texts
Lang: ru
Description: О результатах конкурса Django и мои новые приложения Django.

[DjangoDash][] закончился. Много строк кода было написано, много удалено, но я уверен, что все участники получили полезный опыт. Быстрая разработка, тестирование, установка. Работа с дедллайном, и т.д..

Я реализовал почти все пункты из TODO и новое Django приложение родилось в эти выходные — [django-antichaos][]. Его единственная задача заключается в упрощении редактирования облака тегов. У меня есть старый блог о фотографии с огромным облаком тегов, разросшимся после нескольких лет использования. [django-antichaos][] пытается решить эту проблему. Это инструмент для объединения и более простого переименования тегов, использующее Drag&Drop.

Чтобы показать возможности этого приложения, я создал небольшой скрин-каст. Взгляните и не пожалеете:

<object width="450" height="370"><param name="video" value="http://flv.video.yandex.ru/lite/alexander-artemenko/dpzwddd9rm.709/"></param><param name="allowFullScreen" value="true"></param><param name="scale" value="noscale"></param><embed src="http://flv.video.yandex.ru/lite/alexander-artemenko/dpzwddd9rm.709/" type="application/x-shockwave-flash" width="450" height="370" allowFullScreen="true" scale="noscale" ></embed></object>

Как уже было сказано, [django-antichaos][] reusable. Это означает, что он может работать в любом проекте, который использует [django-tagging][] или [django-tagging-ng][]. Все исходники доступны на GitHub. Форкните проект, поиграйтесь. Если что, шлите патчи.

Я думаю, что [DjangoDash][] позволяет приобрести новый опыт и навыки, кроме того, это весьма забавное мероприятие с элементом соревновательности!

[django-tagging]: http://code.google.com/p/django-tagging/
[django-tagging-ng]: http://github.com/svetlyak40wt/django-tagging-ng
[django-antichaos]: http://github.com/svetlyak40wt/django-antichaos
[DjangoDash]: http://djangodash.com
