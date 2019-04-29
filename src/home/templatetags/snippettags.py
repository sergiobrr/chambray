from django import template as Template
from home.models import BaseSnippet
from django.utils.html import format_html

register = Template.Library()

@register.simple_tag
def render_basesnippet(identifier=None):
    response = None
    context = {}
    if identifier and BaseSnippet.objects.filter(identifier=identifier).exists():
        template_name = 'home/snippets/' + identifier + '.html'
        try:
            template = Template.loader.get_template(template_name)
            context.update({
                'snippet': BaseSnippet.objects.get(identifier=identifier)
            })
            response = format_html(template.render(context))
        except:
            pass

    return response