Title: Filtering choices in Django's ModelForm
Slug: filtering-choices
Date: 2010-06-04 13:12
Tags: python, django, snippet
Category: texts
Lang: en
Description: Example, how to filter values in the drop down, based on row level permissions.

    :::python
    # ...
    # There are models Subscription and MailList defined above.
    # MailList has a many to many field 'managers'. This field
    # defines which manager is able to edit/add subscriptions to
    # a maillist.
    # 
    # To filter choices in the Django's admin, I use following code:

    class SubscriptionAdmin(admin.ModelAdmin):
        list_display = ('id', 'mail_list', 'email', 'name')

        def get_form(self, request, obj=None, **kwargs):
            form_class = super(SubscriptionAdmin, self).get_form(request, obj = obj, **kwargs)

            class ModelFormWithPermissions(form_class):
                def __init__(self, *args, **kwargs):
                    super(ModelFormWithPermissions, self).__init__(*args, **kwargs)

                    self.fields['mail_list'].queryset = \ 
                        MailList.objects.filter(
                            managers__id = request.user.id
                        )   

            return ModelFormWithPermissions

    site.register(Subscription, SubscriptionAdmin)

    # This code creates a special ModelForm class which know
    # about the current user, his 'id' and permissions.


Here is a [gist file](http://gist.github.com/425182).