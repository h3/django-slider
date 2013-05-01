from django import template
from slider.conf import settings
from slider.models import SliderImage

register = template.Library()

@register.assignment_tag
def get_slider_iamges(slider, limit=10, shuffle=True):
    rs = SliderImage.objects.filter(is_visible=True, slider__slug=slider)
    if shuffle:
        return rs.order_by('?')[0:limit]
    else:
        return rs[0:limit]

@register.inclusion_tag(settings.TEMPLATE)
def render_slider(slider, *args, **kwargs):
    span     = kwargs.get('span', 12)
    limit    = kwargs.get('limit', 10)
    shuffle  = kwargs.get('shuffle', False)
    show_nav = kwargs.get('show_nav', "True")
    size     = kwargs.get('size', '940x300')
    default  = kwargs.get('default', settings.DEFAULT)
    show_nav = False if show_nav.lower() == 'false' else True

    if type(shuffle) != type(True):
        shuffle  = False if shuffle.lower() == 'false' else True

    images   = get_slider_iamges(slider, limit=limit, shuffle=shuffle)

    return {
        'slider_images': images,
        'size': size,
        'show_nav': show_nav,
        'slider': slider,
        'default': default,
    }
