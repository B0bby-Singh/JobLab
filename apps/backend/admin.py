from django.contrib import admin
from apps.backend.models import JobScraped, Resume


class JobScrappedAdmin(admin.ModelAdmin):
    list_display = (
        "id", "title", "company", "announcement", "description"
    )
    ordering = ("id",)


class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "id", "file_name", "text"
    )
    ordering = ("id",)

# Register your models here.

admin.site.register(JobScraped, JobScrappedAdmin)
admin.site.register(Resume, ResumeAdmin)
