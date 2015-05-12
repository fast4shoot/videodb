from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape = True)
@stringfilter
def comment_paragraphs(value, autoescape = True):
	if autoescape:
		esc = conditional_escape
	else:
		esc = lambda x: x
		
	return mark_safe("<p>" + value.replace("\n", "</p><p>") + "</p>")
