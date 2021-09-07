from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='Gallery'
urlpatterns=[
    path('', views.homepage, name='landing'), 
    path('gallery/', views.gallery, name='gallery'),
    path('search/', views.search, name='search'),
    path('location/<str:city>', views.search, name='search')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)