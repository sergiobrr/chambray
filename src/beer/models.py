from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel,\
	InlinePanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtailmetadata.models import MetadataPageMixin, MetadataMixin
from colorful.fields import RGBColorField
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalManyToManyField
from chambray.base_models import AbstractBaseModel

# Create your models here.

class BeerCategory(AbstractBaseModel):
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
	] + AbstractBaseModel.panels

	class Meta:
		ordering = ['sort_order', 'name', ]
		verbose_name = 'Beer Category'
		verbose_name_plural = 'Beer Categories'
		app_label = 'beer'

	def __str__(self):
		return self.name


class Beer(AbstractBaseModel):
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
	infographic_icon = models.ForeignKey(
		'wagtaildocs.Document',
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='+',
		verbose_name='Graphic icon for beer spec',
		help_text='It shows bitterness, strength and colour'
	)
	contrast_background = RGBColorField(
		default='#FBD872',
		verbose_name='Color used to contrast photos and graphics'
	)
	has_polykeg = models.BooleanField(
		default=False, 
		verbose_name='Polikeg available'
	)
	short_description = models.TextField(
		verbose_name='Short description',
		default='Short description goes here'
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
	alcoholic_content = models.CharField(max_length=255,
		null=False,
		blank=False,
		verbose_name="ABV")
	ibu = models.CharField(max_length=255,
		null=False,
		blank=False,
		verbose_name="IBU",
		default='15.5')
	food_pairings = models.CharField(max_length=255,
        null=True,
        blank=True,
        verbose_name='Food pairings')
	serving_temperature = models.CharField(max_length=255,
		null=False,
		blank=False,
		verbose_name="Serving Temperature")
	ingredients = models.CharField(max_length=512,
		null=False,
		blank=False,
		default=u'Pay atention => Only the best natural ingredients.',
		verbose_name='How to store Lord Chambray')

	panels = [
		FieldPanel('name', classname='title'),
		FieldRowPanel([
			FieldPanel('beer_category', classname='col4'),
			FieldPanel('claim', classname='col4'),		
			FieldPanel('contrast_background', classname='col4')
		]),
		FieldPanel('short_description', classname='full'),
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
				FieldPanel('food_pairings', classname='col6'),
				FieldPanel('ingredients', classname='col12')
			]),
		], heading='Tasting', classname="collapsible collapsed"),
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('alcoholic_content', classname='col4'),
				FieldPanel('ibu', classname='col4'),
				FieldPanel('serving_temperature', classname='col4')
			]),
			DocumentChooserPanel('spec_sheet', classname='col6'),
			DocumentChooserPanel('infographic_icon', classname='col6'),
		], heading="Specs", classname="collapsible collapsed"),   	
	] + AbstractBaseModel.panels

	class Meta:
		ordering = ['sort_order', 'name', ]
		verbose_name = 'Beer'
		verbose_name_plural = 'Beers'
		app_label = 'beer'

	def __str__(self):
		return self.name


class BeerContainer(AbstractBaseModel):
	name = models.CharField(max_length=255, verbose_name='Container name')
	volume = models.IntegerField(default=0, verbose_name='Volume in cl')
	svg_icon = models.ForeignKey(
		'wagtaildocs.Document',
		null=True,
		blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
	)

	panels = [
		FieldRowPanel([
			FieldPanel('name', classname='col4'),
			FieldPanel('volume', classname='col4'),
			DocumentChooserPanel('svg_icon', classname='col4'),
		]),
	] + AbstractBaseModel.panels

	class Meta:
		ordering = ['sort_order', 'name', ]
		verbose_name = 'Beer Container'
		verbose_name_plural = 'Beer Containers'
		app_label = 'beer'

	def __str__(self):
		return self.name


class BeerAvailability(AbstractBaseModel):
	beer = models.ForeignKey(
		'Beer',
		on_delete=models.CASCADE,
		related_name='availabilities_type',
		verbose_name='Beer'
	)
	container = models.ForeignKey(
		'BeerContainer',
		on_delete=models.CASCADE,
		related_name='beers_available',
		verbose_name='Container'
	)

	panels = [
		FieldRowPanel([
			FieldPanel('beer', classname='col6'),
			FieldPanel('container', classname='col6')
		]),
	] + AbstractBaseModel.panels

	def __str__(self):
		return 'Beer %s available in %s' % (self.beer.name, self.container.name)

	def admin_list(self):
		return 'Available in %s - Volume %d cl.' % (self.container.name, self.container.volume) 

	class Meta:
		verbose_name = 'Beer Availability'
		verbose_name_plural = 'Beer Availabilities'
		unique_together = ('beer', 'container')
		app_label = 'beer'


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
