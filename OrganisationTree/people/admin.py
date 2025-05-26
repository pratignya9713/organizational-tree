from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager')
    list_filter = ('manager',)
    search_fields = ('name',)
