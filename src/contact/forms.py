# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['sender_email'].required = True
        self.fields['sender_full_name'].required = True
        self.fields['body'].required = True
        self.fields['message_type'].required = True

    class Meta:
        model = Contact
        fields = (
            'sender_email', 
            'sender_full_name', 
            'sender_telephone', 
            'message_type',
            'body'
        )
