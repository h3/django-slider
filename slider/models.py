from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete

from easy_thumbnails.fields import ThumbnailerImageField
from slider.conf import settings
from slider.utils import file_cleanup

class Slider(models.Model):
    slug = models.SlugField(_('Slug'), max_length=50)
    def __unicode__(self):
        return unicode(self.slug)

    
class SliderImage(models.Model):
    photo      = ThumbnailerImageField(_('Photo'), upload_to='slider-images/', 
                     resize_source=dict(size=settings.MAX_UPLOAD_SIZE))
    
    slider     = models.ForeignKey(Slider)
    title      = models.CharField(_('Title'), max_length=250, blank=True, null=True)
    caption    = models.CharField(_('Caption'), max_length=250, blank=True, null=True)
    link       = models.URLField(_('Link'), max_length=250, blank=True, null=True)
    target     = models.CharField(_('Link target'), max_length=10, default='_self', choices=settings.LINK_TARGETS)
    position   = models.PositiveIntegerField(_('Position'), default=0)
    crop       = models.CharField(_('Crop'), max_length=50, default='smart', choices=settings.CROP_CHOICES)
    sharpen    = models.BooleanField(_('Sharpen'), default=False)
    upscale    = models.BooleanField(_('Upscale'), default=False)
    is_visible = models.BooleanField(_('Is visible'), default=True)

    class Meta:
        verbose_name = _('Slider image')
        verbose_name_plural = _('Slider images')
        ordering = ('position',)

post_delete.connect(file_cleanup, sender=SliderImage, 
        dispatch_uid="SliderImage.file_cleanup")
