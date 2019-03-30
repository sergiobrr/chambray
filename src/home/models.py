from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Page, Collection
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images import get_image_model
from wagtailschemaorg.models import BaseLDSetting
from wagtailschemaorg.registry import register_site_thing
from wagtailschemaorg.utils import extend
from phonenumber_field.modelfields import PhoneNumberField


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

	parent_page_types = []
	subpage_types = ['beer.BeerCategoryIndexPage', ]


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
			"address": {
				"@type": "PostalAddress",
				"streetAddress": self.address.streetAddress,
				"addressLocality": self.address.addressLocality,
				"addressRegion": self.address.addressRegion,
				"postalCode": self.address.postalCode,
				"addressCountry": self.address.addressCountry
			},
			"contactPoint": {
				"@type": "ContactPoint",
				"contactType": self.contactPoint.contactType,
				"telephone": self.contactPoint.telephone.as_e164,
				"email": self.contactPoint.email
			},
            "telephone": self.contactPoint.telephone.as_e164,
			"sameAs": [
				self.same_as.facebook,
				self.same_as.instagram,
				self.same_as.twitter,
				self.same_as.youtube
			]
		})
