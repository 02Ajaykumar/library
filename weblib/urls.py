from django.urls import path
from . import views
from .models import Category,Book

urlpatterns = [path("home/",views.home,name="home"),
               path("home/<str:name>/",views.category_view),
               path("search/",views.search),
               path("bookview/<str:name>",views.bookview)]