from django.contrib import admin
from .models import Vacancy, Resume

class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        'state', 'organization', 'slug', 'address', 'employment', 'description',
        'skills', 'requirements', 'duties', 'conditions',
    )
    list_display_links = (
        'state', 'organization', 'description',
    )
    search_fields = (
        'state', 'organization', 'description',
    )

class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        'state', 'slug',
    )
    list_display_links = (
        'state', 'slug',
    )
    search_fields = (
        'state', 'slug',
    )

admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Resume, ResumeAdmin)

# Register your models here.
