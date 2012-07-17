from django.conf import settings
from django.utils.translation import ugettext_lazy as _


TEMPLATE = getattr(settings, 'SLIDER_TEMPLATE', 'slider/bootstrap.html')

MAX_UPLOAD_SIZE = getattr(settings, 'SLIDER_MAX_UPLOAD_SIZE', (1600, 600))

ADMIN_THUMBNAIL_OPTIONS = getattr(settings, 'SLIDER_ADMIN_THUMBNAIL_OPTIONS', 
                            {'size': (300, 120), 'quality': 80, 'crop': 'smart'})

CROP_CHOICES = getattr(settings, 'SLIDER_CROP_CHOICES', (
    ('smart', _('Smart')),
    ('0,',    _('Left')),
    ('50,50', _('Center')),
    ('-0,',   _('Right')),
    (',0',    _('Top center')),
    ('0,0',   _('Top left')),
    ('-0,0',  _('Top right')),
    (',-0',   _('Bottom center')),
    ('0,-0',  _('Bottom left')),
    ('-0,-0', _('Bottom right')),
))

LINK_TARGETS = getattr(settings, 'SLIDER_LINK_TARGETS', (
    ('_self',   _('Same window')),
    ('_blank',  _('New window')),
    ('_parent', _('Parent window')),
))
