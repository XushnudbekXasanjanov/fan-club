from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',Index,name='index'),
    path('blog/',Blogs,name='blog'),
    path('contact/',Contact,name='contact'),
    path('matches/',Matches,name='matchs'),
    path('players/',AllPlayers,name='players'),
    path('single/',BlogSingle,name='single')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)