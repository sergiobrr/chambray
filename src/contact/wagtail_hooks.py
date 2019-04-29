from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Contact
from django.utils.safestring import mark_safe


class ContactAdmin(ModelAdmin):
    model = Contact
    menu_label = 'Contact Message'
    menu_icon = 'mail'
    list_display = ('sender_email', 'sender_full_name', 'subject', 'created')
    search_fields = ('sender_email', 'sender_full_name', 'subject', 'body')
    list_filters = ('message_type', )

modeladmin_register(ContactAdmin)