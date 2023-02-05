from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("drinks/", views.drink_list, name= 'drinks'),
    path("drinks/<str:id>", views.drink_detail, name= 'drink_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
