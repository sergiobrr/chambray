from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register,\
	ModelAdminGroup
from .models import BeerCategory, Beer, BeerContainer, BeerAvailability
from django.utils.safestring import mark_safe


class BeerCategoryAdmin(ModelAdmin):
	model = BeerCategory
	menu_label = 'Beer Category'
	menu_icon = 'folder-inverse'
	list_display = ('sort_order', 'name', 'claim')
	list_filter = ('name', 'claim')
	search_fields = ('name', 'claim')


class BeerAdmin(ModelAdmin):
	model = Beer
	menu_label = 'Beer'
	menu_icon = 'pick'
	list_display = ('sort_order', 'name', 'beer_category',\
                 'availabilities', 'alcoholic_content', 'created')
	list_filter = ('beer_category', )
	search_fields = ('name', 'claim')

	def availabilities(self, beer):
		return mark_safe(
			'<br>'.join([a.admin_list() for a in beer.availabilities_type.all()])
		)


class BeerContainerAdmin(ModelAdmin):
	model = BeerContainer
	menu_label = 'Beer Container'
	menu_icon = 'download'
	list_display = ('sort_order', 'name', 'volume')
	list_filter = ('name', )
	search_fields = ('name', )


class BeerAvailability(ModelAdmin):
	model = BeerAvailability
	menu_label = 'Beer availability'
	menu_icon = 'link'
	list_display = ('sort_order', 'beer', 'container', )
	list_filter = ('beer', 'container', )
	search_fields = ('beer', 'container', )


class BeerGroupAdmin(ModelAdminGroup):
	menu_label = 'Brewery products'
	menu_icon = 'radio-full'
	menu_order = 000
	items = (
		BeerCategoryAdmin, 
		BeerAdmin, 
		BeerContainerAdmin,
		BeerAvailability
	)


modeladmin_register(BeerGroupAdmin)

