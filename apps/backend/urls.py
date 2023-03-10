from django.urls import path
from apps.backend.views import ResumeParserAPI

urlpatterns =[
    path('resume_parse/', ResumeParserAPI.as_view(), name="resume parser "), 
]