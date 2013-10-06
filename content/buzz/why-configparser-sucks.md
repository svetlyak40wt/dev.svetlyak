Title: Почему питоновый ConfigParser отстой
Slug: why-configparser-sucks
Date: 2010-11-29 18:51
Category: reviews
Tags: python
Lang: ru

Нет, он конечно работает. Но почему в нем так по-идиотски сделаны дефолты,
что:

* невозможно задать разные дефолты для одноименных значений, но в разных
секциях;
* в методе get тоже невозможно дефолты передать по-человечески.

Ну ладно, думаю, наверное тож какой-нибудь индус писал, как и logging.py.

![][Resized]

Полез в SVN, сделал annotate. И что вы думаете? Нет! Белые люди писали, даже
сам Guido van Rossum к этому руку приложил.

[Image]: http://farm1.static.flickr.com/90/275450585_2c5cc73085_o.jpg
[Resized]: http://resizer.co/?image=http%3A%2F%2Ffarm1.static.flickr.com%2F90%2F275450585_2c5cc73085_o.jpg&w=600
