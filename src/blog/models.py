from django.db import models
from puput.models import EntryPage, BlogPage
from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtailgeowidget.blocks import GeoBlock
from wagtail.core import blocks, fields
import datetime
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from wagtail.search import index
# Create your models here.


class EventDetailBlock(blocks.StructBlock):
	"""
	Represents the details of an event
	from start date to address and
	location on a map
	"""
	start_date = blocks.DateBlock()
	start_time = blocks.TimeBlock()
	end_date = blocks.DateBlock()
	end_time = blocks.TimeBlock()
	address = blocks.CharBlock()
	location = GeoBlock(
		address_field='address', 
		required=False
	) 

	class Meta:
		icon = 'site'
		template = 'blog/event_details.html'
		default = {
			'start_date': datetime.date.today(),
			'start_time': datetime.datetime.now().time(),
			'end_date': datetime.date.today(),
			'end_time': datetime.datetime.now().time(),
			'address': 'Mgarr Road, Xewkija XWK 9014, Malta'
		}
		label = 'Event details'
		

class EventPage(EntryPage):
	details = fields.StreamField([('details', EventDetailBlock()),])

	content_panels = [
		StreamFieldPanel('details'),
	] + EntryPage.content_panels


BlogPage.subpage_types.append(EventPage)
BlogPage.parent_page_types = ['home.HomePage', ]


@register_snippet
class TextSnippet(models.Model):
	'''
	Snippet used for rendering anywhere
	a text paragraph using a templatetags
	with a name as parameter
	'''
	name = models.CharField(
		max_length=255,
		verbose_name='Text Snippet name',
		null=False,
		blank=False,
		unique=True
	)
	body = RichTextField(verbose_name=_('body'))
	classnames = models.CharField(
		max_length=255,
		verbose_name='List of classname for css',
		null=True,
		blank=True
	) 

	panels = [
		MultiFieldPanel([
				FieldPanel('name', classname='full'),
				FieldPanel('body', classname='full'),
				FieldPanel('classnames', classname='full'),
			],
			heading=_("Content")
		)
	]

	search_fields = [
		index.SearchField('name', partial_match=True),
		index.SearchField('body', partial_match=True)
	]

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Paragraph snippet'
		verbose_name_plural = 'Paragraph snippets'
		ordering = ['name', ]
