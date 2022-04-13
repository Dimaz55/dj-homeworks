from django.contrib import admin

# Register your models here.
from django.contrib.admin import register

from phones.models import Phone


@register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}