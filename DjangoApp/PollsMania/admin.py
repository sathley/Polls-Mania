__author__ = 'Sushant'
from django.contrib import admin
from pollsmania.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)
