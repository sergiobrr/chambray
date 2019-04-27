from django.http import HttpResponse
from django.template import loader
from wagtail.documents.models import Document
from beer.models import Beer
# Create your views here.

def shop_landing_page(request):
    template_name = 'shop/shop_landing_page.html'
    documents = Document.objects.filter(collection__name='shop_images')
    context = {
        'beers': Beer.objects.all(),
        'items': documents
    }
    template = loader.get_template(template_name)
    return HttpResponse(
        template.render(context, request),
        content_type='text/html'
    )
