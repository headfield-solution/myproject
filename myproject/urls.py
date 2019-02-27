
from django.urls import path
from . import view1
urlpatterns = [
    path('',view1.homepage,name='home'),
    path('count',view1.count,name='count'),
    path('about',view1.about, name='about')
]
