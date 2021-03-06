Title: Библиотечка HamlPy
Slug: hamlpy
Date: 2010-12-06 09:15
Category: reviews
Tags: python
Lang: ru

Смотрел вчера библиотечку [HamlPy][].

Это Python реализация шаблонизатора Haml, который используется в Ruby. Однако,
HamlPy не просто генерит HTML, но и способен генерировать шаблоны.

По сути, это еще один уровень абстракции, позволяющий чуть более лаконично
описывать разметку. Например вот это:

    :::haml
    %ul#atheletes
        - for athelete in athelete_list
            %li.athelete= athelete.name

Будет скомпилировано вот в такой HTML:

    :::html
    <ul id='atheletes'>
        {% for athelete in athelete_list %}
            <li class='athelete'>{{ [athelete.name][1] }}</li>
        {% endfor %}
    </ul>

Я немного подергал библиотечку из консоли. На мой взгляд она несколько
сыровата. Кроме того, если ее использовать с Django проектом, то нужно либо
генерить шаблоны на этапе выкладки, либо написать кастомный загрузчик шаблона,
который будет делать это на-лету в момент первого обращения.

В-общем, может быть во что-то это и разовьется. Пока что, идея генерить таким
образом CSS, как это сделано в Compass, мне нравится больше, поскольку от
этого действительно есть польза.

[HamlPy]: https://github.com/jessemiller/HamlPy
