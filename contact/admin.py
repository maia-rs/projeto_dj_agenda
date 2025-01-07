from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)

class ContacAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','show',)
    ordering = ('id',)
    #list_filter = ('create_date',)
    search_fields = ('id','first_name','last_name',)
    list_per_page = 10
    list_max_show_all = 15
    list_editable = ('first_name','last_name','show',)
    list_display_links = ('id','phone')

@admin.register(models.Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)
    