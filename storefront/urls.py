from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # django debug toolbar conf
    path("__debug__/", include("debug_toolbar.urls")),
]
