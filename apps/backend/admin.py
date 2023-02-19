from django.contrib import admin
from apps.backend.models import JobScraped


class JobScrappedAdmin(admin.ModelAdmin):
    list_display = (
        "id", "title", "company", "announcement", "description"
    )
    ordering = ("id",)

# Register your models here.


admin.site.register(JobScraped, JobScrappedAdmin)
