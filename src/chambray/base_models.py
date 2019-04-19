from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel


class AbstractBaseModel(models.Model):
    created = models.DateTimeField(
        auto_now=True, 
        editable=False, 
        verbose_name='Created at')
    updated = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Update at'
    )
    sort_order = models.PositiveIntegerField(
        default=1000,
        verbose_name='Displaying order'
    )

    panels = [
        FieldRowPanel([
            FieldPanel('sort_order', classname='col6'),
        ], classname='title')
    ]

    class Meta:
        ordering = ['sort_order', ]
        abstract = True
