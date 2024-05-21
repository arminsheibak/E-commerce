from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("store/", include("store.urls")),
    # djoser
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    # django debug toolbar conf
    path("__debug__/", include("debug_toolbar.urls")),
]
