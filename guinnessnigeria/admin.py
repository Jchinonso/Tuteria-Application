from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django import forms

from preferences.admin import PreferencesAdmin

from ckeditor.widgets import CKEditorWidget

from guinnessnigeria import models


class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageAdminForm

try:
    admin.site.unregister(FlatPage)
except:
    pass


class FrontPageBannerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {
            'fields': ('image', 'state', 'description', 'url', 'order')
        }),
    )

    list_display = [
        'order',
        'image',
        'url',
        'state',
    ]

admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(models.SitePreferences, PreferencesAdmin)
admin.site.register(models.FrontPageBanner, FrontPageBannerAdmin)
admin.site.register(models.SocialMedia)
