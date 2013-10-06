Title: Используем SELECT FOR UPDATE в Django
Slug: select-update-django
Date: 2010-11-16 13:18
Tags: django, sql
Category: texts
Lang: ru

Только что написал простой хелпер для использования выражения `SELECT FOR UPDATE` в Django:

    :::python
    from django.db import DEFAULT_DB_ALIAS

    def select_for_update(queryset):
        """ Returns query, rewrited to use SELECT ... FOR UPDATE.
            Can be used in transaction to get lock on selected rows.
            Database must support this SQL statements.

            Example:
            >>> query = select_for_update(MyModel.objects.filter(blah = 'minor'))
            >>> unicode(query.query)
            "SELECT * FROM myapp_mymodel WHERE blah = 'minor' FOR UPDATE"
        """
        sql, params = queryset.query.get_compiler(DEFAULT_DB_ALIAS).as_sql()
        return queryset.model._default_manager.raw(sql + ' FOR UPDATE', params)

