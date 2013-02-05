from django.contrib import admin
from django.utils.translation import ugettext as _
from django.conf import settings as django_settings

from slider.utils import AdminThumbnailMixin, file_cleanup
from slider.conf import settings
from slider.models import *

if 'modeltranslation' in django_settings.INSTALLED_APPS:
    try:
        from grappellifit.admin import TranslationAdmin
        BaseAdmin = TranslationAdmin
    except:
        try:
            from modeltranslation.admin import TranslationAdmin
            BaseAdmin = TranslationAdmin
        except:
            BaseAdmin = admin.ModelAdmin
else:
    BaseAdmin = admin.ModelAdmin


class SliderAdmin(admin.ModelAdmin):
    list_display = ('slug',)
admin.site.register(Slider, SliderAdmin)


class SliderImageAdmin(BaseAdmin, AdminThumbnailMixin):
    list_display = ('thumbnail', 'title', 'slider', 'position', 'crop', 'sharpen', 'upscale', 'is_visible',)
    list_editable = ('title', 'position', 'is_visible',)
    list_filter = ('slider', 'is_visible', 'sharpen', 'upscale')
    search_fields = ('title', 'caption')
    thumbnail_options = settings.ADMIN_THUMBNAIL_OPTIONS
    thumbnail_image_field_name = 'photo'
    thumbnail_alt_field_name = 'title'
admin.site.register(SliderImage, SliderImageAdmin)
