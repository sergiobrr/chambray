from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register,\
	ModelAdminGroup
from .models import BeerCategory, Beer


class BeerCategoryAdmin(ModelAdmin):
	model = BeerCategory
	menu_label = 'Beer Category'
	menu_icon = 'folder-inverse'
	list_display = ('name', 'claim')
	list_filter = ('name', 'claim')
	search_fields = ('name', 'claim')


class BeerAdmin(ModelAdmin):
	model = Beer
	menu_label = 'Beer'
	menu_icon = 'pick'
	list_display = ('name', 'beer_category', 'has_polykeg', 'start_availability', 'alcoholic_content', 'created')
	list_filter = ('name', 'has_polykeg', 'alcoholic_content')
	search_fields = ('name', 'claim')


class BeerGroupAdmin(ModelAdminGroup):
	menu_label = 'Brewery products'
	menu_icon = 'download'
	menu_order = 000
	items = (BeerCategoryAdmin, BeerAdmin)


modeladmin_register(BeerGroupAdmin)

