from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleScope, Tag


class ArticleScopeInLineFormSet(BaseInlineFormSet):
    def clean(self):
        is_main_counter = 0
        for form in self.forms:
            data = form.cleaned_data
            if 'is_main' in data and data['is_main']:
                is_main_counter += 1
        if is_main_counter is not 1:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 1
    formset = ArticleScopeInLineFormSet


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

