from django import template
from blog.models import TextSnippet
from django.conf import settings

register = template.Library()


#TextSnippet tag
@register.inclusion_tag('blog/tags/text_snippet.html', takes_context=True)
def render_text_snippet(context, name):
	snippet = {
		'name': 'no snippet',
		'body': 'no body',
		'classnames': 'error no-snippet' 
	}
	if TextSnippet.objects.filter(name=name).exists():
		snippet = TextSnippet.objects.get(name=name)
	return {
		'context': context,
		'snippet': snippet
	}


@register.simple_tag
def get_social_links():
	return {
		'facebook': settings.FACEBOOK_HOME,
		'instagram': settings.INSTAGRAM_HOME,
		'twitter': settings.TWITTER_HOME
	}

