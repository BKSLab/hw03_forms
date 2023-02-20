from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


# @register.simple_tag()
# def post_edit_check():
#     return True
