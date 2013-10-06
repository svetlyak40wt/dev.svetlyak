Title: Фильтр для отладки Django шаблонов
Slug: django-dir-filter
Date: 2010-12-09 14:03
Category: texts
Tags: python, django, snippets
Lang: ru

Написал тут, довольно полезный однострочный скрипт для отладки Django шаблонов.

Иногда бывает, что хочется узнать какие методы и данные есть у той или иной
переменной в контексте шаблона. И если сам список переменных шаблона можно
посмотреть с помощью debug_toolbar, то заглянуть внутрь не получается.

Для этого у меня есть однострочный template фильтр:

    :::python
    from django import template
    register.filter('dir', lambda x: dir(x))

А использовать его надо так:

В шаблоне пишем, например:

    {{ cl|dir }}

Рефрешим страничку, и видим такую портянку:

    :::python
    ['__class__', '__delattr__', '__dict__', '__doc__', '__getattribute__',
    '__hash__', '__init__', '__module__', '__new__', '__reduce__',
    '__reduce_ex__', '__repr__', '__setattr__', '__str__', '__weakref__',
    'can_show_all', 'date_hierarchy', 'filter_specs', 'formset',
    'full_result_count', 'get_filters', 'get_ordering', 'get_query_set',
    'get_query_string', 'get_results', 'has_filters', 'is_popup', 'list_display',
    'list_display_links', 'list_editable', 'list_filter', 'list_per_page',
    'list_select_related', 'lookup_opts', 'model', 'model_admin', 'multi_page',
    'opts', 'order_field', 'order_type', 'page_num', 'paginator', 'params',
    'pk_attname', 'query', 'query_set', 'result_count', 'result_list',
    'root_query_set', 'search_fields', 'show_all', 'title', 'to_field',
    'url_for_result']

Это интерфейс объекта ChangeList, который есть на каждой странице со списком
объектов в джанговской админке.

