from django.db import models
from chambray.base_models import AbstractBaseModel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel,\
    InlinePanel, FieldRowPanel
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from wagtail.search import index
# Create your models here.


class Contact(AbstractBaseModel):
    INFO = 'info'
    BUSINESS = 'business'
    VISIT = 'visit'
    MESSAGE_CATEGORY_CHOICES = (
        ('visit', 'Visit brewery'),
        ('info', 'Info on beers'),
        ('business', 'Business occasion')
    )
    sender_full_name = models.CharField(
        max_length=255,
        verbose_name='Sender full name'
    )
    sender_email = models.EmailField(
        max_length=255,
        verbose_name='Sender email'

    )
    sender_telephone = models.CharField(
        max_length=255,
        verbose_name='Sender phone number',
        null=True,
        blank=True
    )
    message_type = models.CharField(
        max_length=20,
        choices=MESSAGE_CATEGORY_CHOICES,
        default=INFO
    )
    subject = models.CharField(
        max_length=255,
        verbose_name='Message subject'
    )
    body = models.TextField(
        verbose_name='Message body'
    )

    panels = [
        FieldRowPanel([
            FieldPanel('sender_full_name', classname='col6'),
            FieldPanel('sender_email', classname='col6')
        ]),
        FieldRowPanel([
            FieldPanel('sender_telephone', classname='col6'),
            FieldPanel('message_type', classname='col6')
        ]),
        FieldPanel('subject', classname='full'),
        FieldPanel('body', classname='full')
    ] + AbstractBaseModel.panels

    search_fields = [
        index.SearchField('sender_full_name', partial_match=True),
        index.SearchField('sender_email', partial_match=True),
        index.SearchField('subject', partial_match=True),
        index.SearchField('body', partial_match=True)
    ]

    class Meta:
        app_label = 'contact'
        ordering = ['-created', 'sender_email']
        verbose_name = 'Contact message'
        verbose_name_plural = 'Contact messages'

    def __str__(self):
        return 'From %s on %s' % (
            self.sender_email, 
            self.created.strftime('%d/%M/%Y')
        )

    def get_formatted_message(self):
        from_email = settings.DEFAULT_FROM_EMAIL
        subject = settings.EMAIL_SUBJECT_PREFIX + self.subject
        
        text_body = self.email + ' ha mandato un messaggio con il contenuto: \n'\
            + self.body + '.\n Dati del messaggio:\n -Mittente: '\
            + self.sender_full_name + '\n -Telefono: ' + self.sender_telephone\
            + '\n -Tipo di messaggio: ' + self.message_type + '\n -Data invio: '\
            + self.created.strftime('%d/%M/%Y') + '.'
        
        html_content = '<h4>' + self.email + ' ha mandato un messaggio con il contenuto: </h4>'\
            + '<p> + ' + self.body + '</p><br/><h4>Dati del messaggio:</h4><ul><li>Mittente: '\
            + self.sender_full_name + '</li><li>Telefono: ' + self.sender_telephone + '</li>'\
            + '<li>Tipo di messaggio: ' + self.message_type + '</li><li>Data invio: '\
            + self.created.strftime('%d/%M/%Y') + '</li></ul>'
        
        message = EmailMultiAlternatives(
            subject, 
            text_body, 
            from_email, 
            settings.RECIPIENTS
        )

        message.attach_alternative(html_content, 'text/html')
        return message


