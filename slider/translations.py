from modeltranslation.translator import translator, TranslationOptions
from slider.models import SliderImage

class SliderImageTranslationOptions(TranslationOptions):
    fields = ('title', 'caption', 'link')
translator.register(SliderImage, SliderImageTranslationOptions)
