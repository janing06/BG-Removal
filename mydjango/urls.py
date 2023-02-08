from django.contrib import admin
from django.urls import path
from pages.views import home
from removebg.views import removeBackground,bg_removal

from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home, name='home'),
    path("remove/",removeBackground, name="remove"),
    path("removal/",bg_removal, name="removal"),
]
