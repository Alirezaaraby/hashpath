from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/v1/read/', views.snippet_detail, name='api.read'), #localhost:8000/article/api/v1/read/id
]
urlpatterns = format_suffix_patterns(urlpatterns)