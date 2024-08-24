from django.contrib import admin
from django.urls import include, path

from core.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("contactme/", include("contactme.urls")),
    path("category-menu/", include("category_menu.urls")),
    path("sellers/", include("sellers.urls")),
]
