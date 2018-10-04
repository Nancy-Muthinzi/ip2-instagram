from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.login,name = 'login'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^home/',views.home,name='home')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)