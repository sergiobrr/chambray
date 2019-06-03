from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Page, Collection, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel,\
	InlinePanel, FieldRowPanel
from wagtail.images import get_image_model
from wagtailschemaorg.models import BaseLDSetting
from wagtailschemaorg.registry import register_site_thing
from wagtailschemaorg.utils import extend
from phonenumber_field.modelfields import PhoneNumberField
from wagtail.snippets.models import register_snippet
from django.utils.html import format_html
from wagtail.core.models import Page, Orderable
from wagtail.search import index
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class HomePage(Page):
	image_collection = models.ForeignKey(
		Collection,
		blank=True,
		null=True,
		on_delete=models.SET_NULL,
		related_name='home_page',
		verbose_name='Collections of images for the carousel'
	)
	logo_image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	slide_interval = models.IntegerField(
		default=5,
		verbose_name='Interval in seconds for the homepage slider'
	)
	body = RichTextField(
		null=True,
		blank=True,
		verbose_name='Text sliding - star wars style :-)... in the home page'
	)

	content_panels = Page.content_panels + [
		FieldPanel('image_collection'),
		ImageChooserPanel('logo_image'),
		FieldPanel('slide_interval'),
		FieldPanel('body', classname='full')
	]

	def get_collection_images(self):
		if self.image_collection is None:
			return []
		else:
			return get_image_model().objects\
				.filter(collection=self.image_collection)

	parent_page_types = ['wagtailcore.page']
	# subpage_types = ['beer.BeerCategoryIndexPage', ]
	subpage_types = ['beer.BeerCategoryIndexPage', 'puput.BlogPage']


@register_setting(icon='code')
class SocialMediaSettings(BaseSetting):
	facebook = models.URLField(
		help_text='Your Facebook page URL',
		max_length=255,
		verbose_name='Facebook Url',
		null=True,
		blank=True
	)
	instagram = models.URLField(
		help_text='Your instagram page URL',
		max_length=255,
		verbose_name='Instagram Url',
		null=True,
		blank=True
	)
	twitter = models.URLField(
		help_text='Your twitter page URL',
		max_length=255,
		verbose_name='Twitter Url',
		null=True,
		blank=True
	)
	youtube = models.URLField(
		help_text='Your YouTube channel or user account URL',
		max_length=255,
		verbose_name='Youtube Url',
		null=True,
		blank=True
	)

	def __str__(self):
		return 'Media settings - id: %d' % self.pk

	def get_ldjson(self):
		return [
			self.facebook,
			self.instagram,
			self.twitter,
			self.youtube
		]


@register_setting(icon='home')
class AddressSettings(BaseSetting):
	streetAddress = models.CharField(
		max_length=255,
		verbose_name='Street'
	)
	addressLocality = models.CharField(
		max_length=255,
		verbose_name='City'
	)
	addressRegion = models.CharField(
		max_length=4,
		verbose_name='Province/Region code es: TO for Torino'
	)
	postalCode = models.CharField(
		max_length=10,
		verbose_name='Zip code'
	)
	addressCountry = models.CharField(
		max_length=10,
		verbose_name='State ISO code, es IT'
	)

	def __str__(self):
		return '%s, %s' % (self.streetAddress, self.addressCountry)

	def get_ldjson(self):
		return {
			"@type": "PostalAddress",
			"streetAddress": self.streetAddress,
			"addressLocality": self.addressLocality,
			"addressRegion": self.addressRegion,
			"postalCode": self.postalCode,
			"addressCountry": self.addressCountry
		}

	def get_single_line_address(self):
		return '%s %s, %s %s %s' % (
			self.streetAddress,
			self.addressLocality,
			self.addressRegion,
			self.postalCode,
			self.addressCountry
		)


@register_setting(icon='mail')
class ContactPointSettings(BaseSetting):
	contactType = models.CharField(
		max_length=255,
		verbose_name='Contact type es. Customer Support'
	)
	telephone = PhoneNumberField(
		verbose_name='Telephone number es +441719897979'
	)
	email = models.EmailField(
		verbose_name='Email address'
	)

	def __str__(self):
		return '%s at %s' % (self.contactType, self.email)

	def get_ldjson(self):
		return {
			"@type": "ContactPoint",
			"contactType": self.contactType,
			"telephone": self.telephone.as_e164,
			"email": self.email
		}


@register_setting(icon='cog')
@register_site_thing
class BrewerySettings(BaseLDSetting):
	# Canonical URL: http://schema.org/Brewery
	acceptsReservations = models.BooleanField(
		verbose_name='Accepts reservation',
		default=True
	)
	currenciesAccepted = models.CharField(
		max_length=255,
		verbose_name='Currencies Accepted',
		help_text='Es [EUR, GBP]'
	)
	name = models.CharField(
		max_length=100,
		verbose_name='name'
	)
	legal_name = models.CharField(
		max_length=100,
		verbose_name='Legal name'
	)
	vat_id = models.CharField(
		max_length=40,
		verbose_name='Vat ID number'
	)
	url = models.URLField(
		max_length=255,
		verbose_name='Site Url'
	)
	logo = models.URLField(
		max_length=255,
		verbose_name='Logo Url'
	)
	description = models.TextField(
		verbose_name='Description'
	)
	openingHours = models.CharField(
		max_length=255,
		verbose_name='Opening hours',
		help_text='Days are specified with two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su. Times are specified using 24:00 time. Example: "Tu,Th 16:00-20:00"'
	)
	priceRange = models.CharField(
		max_length=5,
		verbose_name='How cheap is the brewery',
		help_text='The price range of the business, for example €€€'
	)
	foundingDate = models.CharField(
		max_length=4,
		verbose_name='Year of foundation'
	)
	address = models.ForeignKey(
		AddressSettings,
		verbose_name='Organization address',
		null=True,
		on_delete=models.SET_NULL
	)
	contactPoint = models.ForeignKey(
		ContactPointSettings,
		verbose_name='Contact point',
		null=True,
		on_delete=models.SET_NULL
	)
	same_as = models.ForeignKey(
		SocialMediaSettings,
		verbose_name='Same as Social media accounts',
		null=True,
		on_delete=models.SET_NULL
	)

	def ld_entity(self):
		return extend(super().ld_entity(), {
			"@type": "Brewery",
			"acceptsReservations": self.acceptsReservations,
			"currenciesAccepted": self.currenciesAccepted,
			"name": self.name,
			"legalName": self.legal_name,
			"vatID": self.vat_id,
			"url": self.url,
			"image": self.url,
			"logo": self.logo,
			"priceRange": self.priceRange,
			"servesCuisine": "no",
			"description": self.description,
			"foundingDate": self.foundingDate,
			"openingHours": self.openingHours,
			"address": self.address.get_ldjson(),
			"contactPoint": self.contactPoint.get_ldjson(),
            "telephone": self.contactPoint.telephone.as_e164,
			"sameAs": self.same_as.get_ldjson()
		})


@register_snippet
class BaseSnippet(index.Indexed, ClusterableModel):
	description = models.CharField(
		unique=True,
		max_length=255,
		verbose_name='Logical description'
	)
	identifier = models.CharField(
		max_length=255,
		unique=True,
		verbose_name='Unique identifier to use in template'
	)

	panels = [
		MultiFieldPanel([
			FieldRowPanel([
				FieldPanel('description', classname='col6'),
				FieldPanel('identifier', classname='col6'),
			]),
		], heading='Displaying properties', classname='collapsible'),
		InlinePanel('link_lists', label="Links")
	]

	search_fields = [
		index.SearchField('description', partial_match=True),
		index.SearchField('identifier', partial_match=True)
	]

	def __str__(self):
		return self.description


@register_snippet
class LinkSnippet(index.Indexed, models.Model):
	identifier = models.CharField(
		max_length=255,
		unique=True,
		verbose_name='Unique identifier to use in template'
	)
	link_text = models.CharField(
		max_length=255,
		verbose_name='Text to display'
	)
	url = models.URLField(
		max_length=512,
		verbose_name='Url for external page'
	)

	panels = [
		FieldPanel('identifier', classname='full'),
        FieldPanel('link_text', classname='full'),
        FieldPanel('url', classname='full'),
    ]

	search_fields = [
        index.SearchField('link_text', partial_match=True),
        index.SearchField('identifier', partial_match=True),
    ]

	def to_html(self, css_classes=None):
		return format_html(
			'<a href="%s" class="%s" target="_blank">%s</a>' % (
													self.url, 
													css_classes, 
													self.link_text
												)
		)

	def __str__(self):
		return '%s - %s' % (self.identifier, self.link_text)


@register_snippet
class LinkPlacement(Orderable, models.Model):
	container=ParentalKey(
		BaseSnippet,
		on_delete=models.CASCADE,
		related_name='link_lists'
	)
	content=models.ForeignKey(
		LinkSnippet,
		on_delete=models.CASCADE,
		related_name='containers'
	)

	class Meta:
		verbose_name = 'Link positioning'
		verbose_name_plural = 'Link positionings'

	def __str__(self):
		return content.identifier + ' => on ' + container.identifier
	
