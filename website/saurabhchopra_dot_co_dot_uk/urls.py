from .views import index, favicon
from django.urls import path, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('', index, name="index"),
    re_path(r'^favicon\.ico$', favicon),
]
