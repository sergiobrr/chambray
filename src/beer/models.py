from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel,\
	InlinePanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtailmetadata.models import MetadataPageMixin, MetadataMixin

# Create your models here.

class BeerCategory(models.Model):
	name = models.CharField(
		max_length=255,
		unique=True,
		verbose_name='Category name'
	)
	claim = models.TextField(
		verbose_name='Category claim',
		null=True,
		blank=True
	)

	panels = [
		FieldPanel('name', classname='title'),
		FieldPanel('claim', classname='full')
	]

	class Meta:
		ordering = ['name', ]
		verbose_name = 'Beer Category'
		verbose_name_plural = 'Beer Categories'
		app_label = 'beer'

	def __str__(self):
		return self.name


class Beer(models.Model):
	beer_category = models.ForeignKey(
		BeerCategory,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='beers',
		verbose_name='Beer Category'
	)
	name = models.CharField(
		max_length=255,
		unique=True,
		verbose_name='Beer name'
	)
	claim = models.TextField(
		verbose_name='Beer claim',
		null=True,
		blank=True
	)
	spec_sheet = models.ForeignKey(	
		'wagtaildocs.Document',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	bottle_image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	glass_image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	conil_image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	tap_image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	label = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	has_polykeg = models.BooleanField(
		default=False, 
		verbose_name='Polikeg available'
	)
	start_availability = models.DateField(auto_now=False,
		auto_now_add=False,
		null=True,
		blank=True,
		verbose_name='Start availability date'
	)
	end_availability = models.DateField(auto_now=False,
		auto_now_add=False,
		null=True,
		blank=True,
		verbose_name='End availability date'
	)
	tasting_style = models.CharField(max_length=255,
		null=True,
		verbose_name='Tasting Style')
	tasting_appearance = models.CharField(max_length=255,
		null=True,
		verbose_name='Tasting See')
	tasting_smell = models.CharField(max_length=255,
		null=True,
		verbose_name='Tasting Smell')
	tasting_taste = models.CharField(max_length=255,
		null=True,
		verbose_name='Tasting Taste')
	tasting_bitter = models.PositiveSmallIntegerField(null=True,
		verbose_name='Tasting Bitter')
	tasting_sweet = models.PositiveSmallIntegerField(null=True,
		verbose_name='Tasting Sweet')
	alcoholic_content = models.CharField(max_length=255,
		null=False,
		blank=False,
		verbose_name="ABV")
	ibu = models.CharField(max_length=255,
		null=False,
		blank=False,
		verbose_name="IBU",
		default='15.5')
	srm = models.SmallIntegerField(null=False,
		blank=False,
		default=1,
		verbose_name='SRM')
	og = models.SmallIntegerField(null=False,
		blank=False,
		default=1,
		verbose_name='OG')
	degree_plato = models.CharField(max_length=10,
		null=False,
		blank=False,
		default='1.0',
		verbose_name='Degree Plato')
	colour = models.CharField(max_length=255,
		null=False,
		blank=False,
		verbose_name="Colour")
	serving_temperature = models.CharField(max_length=255,
		null=False,
		blank=False,
		verbose_name="Serving Temperature")
	how_to_store = models.CharField(max_length=255,
		null=False,
		blank=False,
		default=u'Store upright in a dark, cool place. Refrigerate 24 to 48 hours before serving.',
		verbose_name='How to store Lord Chambray')
	created = models.DateTimeField(auto_now_add=True, editable=False)
	updated = models.DateTimeField(auto_now=True, editable=False)

	panels = [
		FieldPanel('name', classname='title'),
		FieldRowPanel([
			FieldPanel('beer_category', classname='col6'),
			FieldPanel('claim', classname='col6')
		]),
		DocumentChooserPanel('spec_sheet'),
		ImageChooserPanel('bottle_image'),
		ImageChooserPanel('glass_image'),
		ImageChooserPanel('conil_image'),
		ImageChooserPanel('tap_image'),
		ImageChooserPanel('label'),
		FieldRowPanel([
			FieldPanel('start_availability', classname='col4'),
			FieldPanel('end_availability', classname='col4'),
			FieldPanel('has_polykeg', classname='col4'),
		]),
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('tasting_style', classname='col6'),
				FieldPanel('tasting_appearance', classname='col6'),
			]),
			FieldRowPanel([
				FieldPanel('tasting_smell', classname='col6'),
				FieldPanel('tasting_taste', classname='col6'),
			]),
			FieldRowPanel([
				FieldPanel('tasting_bitter', classname='col6'),
				FieldPanel('tasting_sweet', classname='col6'),
			]) 
		], heading='Tasting', classname="collapsible collapsed"),
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('alcoholic_content', classname='col4'),
				FieldPanel('ibu', classname='col4'),
				FieldPanel('srm', classname='col4')
			]),
			FieldRowPanel([
				FieldPanel('degree_plato', classname='col4'),
				FieldPanel('colour', classname='col4'),
				FieldPanel('serving_temperature', classname='col4')
			]),
			FieldPanel('how_to_store', classname='full'),
		], heading="Specs", classname="collapsible collapsed")   	
	]

	class Meta:
		ordering = ['name', ]
		verbose_name = 'Beer'
		verbose_name_plural = 'Beers'
		app_label = 'beer'

	def __str__(self):
		return self.name


class BeerCategoryIndexPage(MetadataPageMixin, Page):
	
	parent_page_types = ['home.HomePage', ]
	subpage_types = ['beer.BeerCategoryPage', ]


class BeerCategoryPage(MetadataPageMixin, Page):
 	category = models.ForeignKey(
 		BeerCategory,
 		null=True,
 		blank=True,
 		on_delete=models.SET_NULL,
 		verbose_name='Page for category:'
	)
 	parent_page_types = ['beer.BeerCategoryIndexPage', ]
 	content_panels = Page.content_panels + [
 		FieldPanel('category'), 
 	]
 	subpage_types = ['beer.BeerPage', ]

 	def get_dict(self):
 		print('########################')
 		print(self.__dict__)
 		print('########################')
 		return self.__dict__


class BeerPage(Page):
	beer = models.ForeignKey(
		Beer,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		verbose_name='Beer to detail in the page'
	)

	content_panels = Page.content_panels + [
		FieldPanel('beer', classname='full')
	]

	parent_page_types = ['beer.BeerCategoryPage', ]
	subpage_types = []	